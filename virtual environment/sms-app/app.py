import sqlite3

# connection with SQLite database
conn = sqlite3.connect('sms-database.db')
conn.execute('PRAGMA foreign_keys = ON;')
print("Opened database successfully")

# create tables for student management system
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS college (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    college_name TEXT NOT NULL,
    college_id INTEGER NOT NULL UNIQUE
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS department (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT NOT NULL,
    department_id INTEGER NOT NULL UNIQUE,
    college_id INTEGER NOT NULL,
    FOREIGN KEY (college_id) REFERENCES college(id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS faculty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faculty_name TEXT NOT NULL,
    faculty_id INTEGER NOT NULL UNIQUE,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES department(id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    course_id INTEGER NOT NULL UNIQUE,
    department_id INTEGER NOT NULL,
    faculty_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES department(id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL,
    student_id INTEGER NOT NULL UNIQUE,
    student_address TEXT NOT NULL,
    student_age INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    course_id INTEGER,
    faculty_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES department(id),
    FOREIGN KEY (course_id) REFERENCES course(id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(id)
)
""")

conn.commit()
print("Tables created successfully")
conn.close()
