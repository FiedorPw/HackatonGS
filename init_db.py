import os
import psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        # user=os.environ['DB_USERNAME'],
        # password=os.environ['DB_PASSWORD'])
         user='admin',
         password='admin')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS students;')
cur.execute('CREATE TABLE students (id serial PRIMARY KEY,'
                                 'imie varchar (150) NOT NULL,'
                                 'nazwisko varchar (50) NOT NULL,'
                                 'nr_indeksu integer NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP,'
                                 'haslo varchar (20) NOT NULL);'
                                 )
# Insert data into the table
cur.execute('INSERT INTO students (imie, nazwisko, nr_indeksu, haslo)'
            'VALUES (%s, %s, %s, %s)',
            ('admin',
             'admin',
             1,
             'superAdmin')
            )
cur.execute('INSERT INTO students (imie, nazwisko, nr_indeksu, haslo)'
            'VALUES (%s, %s, %s, %s)',
            ('Stefan',
             'Betonowy',
             128691,
             'odwroconaMuszla')
            )
cur.execute('INSERT INTO students (imie, nazwisko, nr_indeksu,haslo)'
            'VALUES (%s, %s, %s, %s)',
            ('Andrzej',
             'Sygnałowy',
             318632,
             'muszlaMocy')
            )
cur.execute('INSERT INTO students (imie, nazwisko, nr_indeksu,haslo)'
            'VALUES (%s, %s, %s, %s)',
            ('Zbyslaw',
             'Telekomowy',
              438632,
             'korzenMuszla',
             )
            )
conn.commit()

#cursor któ©y pozwala pytongowi wykonywac commendy w bazie
cur.close()
conn.close()