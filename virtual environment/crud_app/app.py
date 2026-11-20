import mysql.connector
import pandas as pd
import numpy as np
import openpyxl
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3333,
        user="root",
        password="",
        database="crud-app-db"
    )

    if conn.is_connected():
        print("Connected to MySQL database!")
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                uid INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(225),
                age INT,
                address TEXT
            )
        """)
        cur.execute(
            """
            inset
            """
        )
        print("Table 'users' created successfully!")

except Error as e:
    print("Error while connecting to MySQL:", e)
