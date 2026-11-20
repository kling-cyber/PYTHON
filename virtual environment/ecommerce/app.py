import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3333,
        user="root",
        password="",
        database="ecommerce-app-db"
    )

    print("Connected to MySQL database!")

    cur = connection.cursor()

    # Create country table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS country (
            cid INT AUTO_INCREMENT PRIMARY KEY,
            cname VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create state table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS state (
            sid INT AUTO_INCREMENT PRIMARY KEY,
            sname VARCHAR(255) NOT NULL,
            cid INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cid) REFERENCES country(cid)
        )
    """)

    # Create city table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS city (
            city_id INT AUTO_INCREMENT PRIMARY KEY,
            city_name VARCHAR(255) NOT NULL,
            state_id INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (state_id) REFERENCES state(sid)
        )
    """)

    connection.commit()
    print("All three tables created successfully!")
    connection.close()
except Error as e:
    print("Database error:", e)
