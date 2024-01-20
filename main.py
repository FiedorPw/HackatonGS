import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
os.environ['DB_USERNAME'] = 'admin'
os.environ['DB_PASSWORD'] = 'admin'

#SuperZbazowanaBaza#GS

#łaczymy sie username,password zapisanymi w global variables
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='flask_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

def get_from_database_by_name(db_connection,cur,text):
    try:
        query = f"SELECT * FROM students WHERE imie='{text}';"
        cur.execute(query)
        wyszukana_osoba = cur.fetchone()


        if wyszukana_osoba is None:
            wyszukana_osoba = ''

    except Exception as e:
        print(e)
        cur.execute("ROLLBACK")
        db_connection.commit()
        wyszukana_osoba = ''
    finally:
        cur.close()
        return wyszukana_osoba
    pass
@app.route('/', methods=['POST','GET'])
def index():
    #inicjalizacja kursora do pobierania danych z db
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    students = ""
    wyszukana_osoba = ""

    #wysyłamy strone przy ładowaniu
    if request.method == "GET":
        cur.execute('SELECT * FROM students OFFSET 1;')
        students = cur.fetchall()
        cur.close()
        db_connection.close()
    #odpowiedz na klika "Get student's data"
    if request.method == "POST":
        text = request.form['text']
        wyszukana_osoba = get_from_database_by_name(db_connection,cur,text)
    return render_template('index2.html', students=students, wyszukana_osoba=wyszukana_osoba)

@app.route('/login', methods=['GET', 'POST'])
def login():
    db_connection = get_db_connection()
    cur = db_connection.cursor()
    loggedIN = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = f"SELECT haslo FROM students WHERE imie='{username}';"
        cur.execute(query)
        password_from_db = cur.fetchone()
        #sprawdzamy czy dla podanego użytkownika hasło w bazie zgadza sie z podanym
        if password == str(password_from_db[0]):
            loggedIN = "you are logged in!"
            return redirect(url_for('index'))
        else:
            loggedIN = "wrong credentials"
    return render_template('login.html',loggedIN=loggedIN)
