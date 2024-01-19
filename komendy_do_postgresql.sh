






GRANT CREATE ON SCHEMA public TO admin;
GRANT CREATE ON SCHEMA public TO adminGRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin;
  #w bazie
  CREATE DATABASE flask_db;
  CREATE USER admin WITH PASSWORD 'admin';
  GRANT ALL PRIVILEGES ON DATABASE flask_db TO admin;



python3 -m venv env
source env/bin/activate
pip install Flask

#web serwer
#to wszysko aby zadziałało
sudo service postgresql start
export DB_USERNAME="admin"
export DB_PASSWORD="admin"
python3 init_db.py

export FLASK_DEBUG=1
export FLASK_APP=main
flask run

firefox-esr 127.0.0.1:5000

#to skryptem zeruje on baze do ,,defoultowych(to co jest napisane w init_db.py) czyli te tabele co tam są



#to z palca

  sudo -iu postgres psql
  psql -U flask_db -h admin
  #listuje
  \l
  #łączymy sie z naszą bazą
  \c flask_db
  #listujemy
  \dt
  #crud operacje
  SELECT * FROM your_table_name
  INSERT INTO your_table_name(column1, column2, ...) VALUES(value1, value2, ...);
  UPDATE your_table_name SET column1 = value1, column2 = value2, ... WHERE condition;
  DELETE FROM your_table_name WHERE condition;
  #wychodzi się
  \q
  
  
sudo ip addr del 192.168.1.10/24 dev eth0
sudo ip addr add 192.168.0.240/24 dev eth0
  
  
  
  
  
  
  
  
  
  
  
