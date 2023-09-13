import sqlite3

conn = sqlite3.connect("db.sqlite3")

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        `name` TEXT NOT NULL,
        city TEXT,
        country TEXT,
        date_birth DATE,
        email TEXT,
        phone TEXT,
        group_name TEXT
    );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_name TEXT,
    score DECIMAL(3, 2),
    FOREIGN KEY (student_id) REFERENCES Students(id)
);
""")


cursor.execute("""INSERT INTO students(name, city, country, group_name)
VALUES ('Mask', 'Sity1', 'USA', 'group1'),
       ('Bill', 'Sity1', 'USA1', 'group1'),
       ('Jobs', 'Sity2', 'Ukraine', 'group1');
""")

cursor.execute("""INSERT INTO grades('student_id', 'subject_name', 'score')
VALUES ('1', 'subject1', 5),
       ('2', 'subject2', 7),
       ('3', 'subject3', 9),
       ('4', 'subject3', 8),
       ('4', 'subject3', 5);
""")

cursor.execute("""INSERT INTO grades (student_id, subject_name, score)
VALUES (4, 'subject1', 8);
""")
cursor.execute("""INSERT INTO `grades` (student_id, subject_name, score)
VALUES (4, 'subject1', 5);
""")



cursor.execute("""
CREATE TABLE IF NOT EXISTS VegetablesFruits(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    color TEXT,
    calories REAL,
    description TEXT
);
""")


cursor.execute("""
INSERT INTO VegetablesFruits(name, type, color, calories, description) VALUES
    ('Яблоко', 'фрукт', 'красное', 10.0, 'Красное яблоко'),
    ('Банан', 'фрукт', 'желтый', 20.0, 'Желтый банан'),
    ('Морковь', 'овощ', 'оранжевый', 30.0, 'Оранжевая морковь'),
    ('Лимон', 'фрукт', 'желтый', 40.0, 'Желтый лимон.');
    """)

conn.commit()

conn.close()