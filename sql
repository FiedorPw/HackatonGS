DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id serial PRIMARY KEY,
    imie varchar(150) NOT NULL,
    nazwisko varchar(50) NOT NULL,
    nr_indeksu integer NOT NULL,
    date_added date DEFAULT CURRENT_TIMESTAMP,
    haslo varchar(20) NOT NULL
);


INSERT INTO students (imie, nazwisko, nr_indeksu, haslo) VALUES
('admin', 'admin', 1, 'superAdmin'),
('Stefan', 'Betonowy', 128691, 'odwroconaMuszla'),
('Andrzej', 'Sygnałowy', 318632, 'muszlaMocy'),
('Zbyslaw', 'Telekomowy', 438632, 'korzenMuszla');
