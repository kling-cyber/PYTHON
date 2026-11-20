import sqlite3
import pandas as pd
conn = sqlite3.connect('database.db')
#creating a database table library management system 
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT NOT NULL,
    availability_status TEXT NOT NULL
)''')
conn.commit()
#insert database value 
cur.execute('''insert into books (title,author,category,availability_status) values ('The Great Gatsby','F. Scott Fitzgerald','Fiction','Available')'''    )
conn.commit()
#insert many values
books = [
    ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 'Available'),
    ('1984', 'George Orwell', 'Dystopian', 'Available'),        
    ('Pride and Prejudice', 'Jane Austen', 'Romance', 'Available'),
    ('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 'Available'),
    ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 'Available')]
for book in books:
    cur.execute('''insert into books (title,author,category,availability_status) values (?,?,?,?)''', book)
conn.commit()
#use pandas show values
df = pd.read_sql_query("SELECT * FROM books", conn)
print(df)
conn.commit()

conn.close()