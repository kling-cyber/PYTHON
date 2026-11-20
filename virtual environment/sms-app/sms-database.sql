BEGIN TRANSACTION;
CREATE TABLE college (id INTEGER PRIMARY KEY AUTOINCREMENT, college_name TEXT NOT NULL, college_id INTEGER NOT NULL UNIQUE);
CREATE TABLE course (id INTEGER PRIMARY KEY AUTOINCREMENT, course_name TEXT NOT NULL, course_id INTEGER NOT NULL UNIQUE, department_id INTEGER NOT NULL, faculty_id INTEGER, FOREIGN KEY (department_id) REFERENCES department(id), FOREIGN KEY (faculty_id) REFERENCES faculty(id));
CREATE TABLE department (id INTEGER PRIMARY KEY AUTOINCREMENT, department_name TEXT NOT NULL, department_id INTEGER NOT NULL UNIQUE, college_id INTEGER NOT NULL, FOREIGN KEY (college_id) REFERENCES college(id));
CREATE TABLE faculty (id INTEGER PRIMARY KEY AUTOINCREMENT, faculty_name TEXT NOT NULL, faculty_id INTEGER NOT NULL UNIQUE, department_id INTEGER NOT NULL, FOREIGN KEY (department_id) REFERENCES department(id));
CREATE TABLE student (id INTEGER PRIMARY KEY AUTOINCREMENT, student_name TEXT NOT NULL, student_id INTEGER NOT NULL UNIQUE, student_address TEXT NOT NULL, student_age INTEGER NOT NULL, department_id INTEGER NOT NULL, course_id INTEGER, faculty_id INTEGER, FOREIGN KEY (department_id) REFERENCES department(id), FOREIGN KEY (course_id) REFERENCES course(id), FOREIGN KEY (faculty_id) REFERENCES faculty(id));
COMMIT;
