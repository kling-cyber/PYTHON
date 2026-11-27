
#sqllite is a database
#sqllite is a open source database
#sqllie is inbuilt module
#sqllite defaultmodule support in python 
import sqlite3

#create a connection to the database
conn = sqlite3.connect('App.db')
print("Database created successfully")

#create a cursor object to execute SQL commands
cursor = conn.cursor()  

#create a table in the database Users
cursor.execute('''CREATE TABLE IF NOT EXISTS users
             (uid INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              password TEXT NOT NULL,
              mobile integer NOT NULL,
              gender TEXT NOT NULL,
              hobby TEXT NOT NULL,
              pincode integer NOT NULL,
              email TEXT NOT NULL,
              created_data text NOT NULL)''')

#save the changes and close the connection
conn.commit()
print("Table created successfully")

#create table country 
cursor.execute('''CREATE TABLE IF NOT EXISTS country
             (cid INTEGER PRIMARY KEY AUTOINCREMENT,    
              country_name TEXT NOT NULL,
              created_data text NOT NULL)''')  

#save the changes and close the connection
conn.commit()
print("Table created successfully")

#create table state
cursor.execute('''CREATE TABLE IF NOT EXISTS state  
              (sid INTEGER PRIMARY KEY AUTOINCREMENT,    
                  state_name TEXT NOT NULL,
                  cid integer NOT NULL,
                  created_data text NOT NULL)''')   

#save the changes and close the connection
conn.commit()
print("Table created successfully")

#create table city
cursor.execute('''CREATE TABLE IF NOT EXISTS city  
              (ctid INTEGER PRIMARY KEY AUTOINCREMENT,    
                  city_name TEXT NOT NULL,
                  sid integer NOT NULL,
                  created_data text NOT NULL)''')

#save the changes and close the connection
conn.commit()
print("Table created successfully")

#close the connection
conn.close()

#create a normalization of type of task based on cattegory and subcategory
#customers | colors | size | products | cart | orders 

conn = sqlite3.connect('App2.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute('''CREATE TABLE IF NOT EXISTS customers
             (customer_id INTEGER PRIMARY KEY AUTOINCREMENT,    
              customer_name TEXT NOT NULL,
              customer_email TEXT NOT NULL,
              customer_password TEXT NOT NULL,
              created_data text NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS category
             (category_id INTEGER PRIMARY KEY AUTOINCREMENT ,
             category_name TEXT NOT NULL,
             created_data text NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subcategory
             (subcategory_id INTEGER PRIMARY KEY AUTOINCREMENT,
             subcategory_name TEXT NOT NULL,
             category_id integer NOT NULL,
             created_data text NOT NULL,
             FOREIGN KEY (category_id) REFERENCES category(category_id))''')    

cursor.execute('''CREATE TABLE IF NOT EXISTS colors 
             (color_id INTEGER PRIMARY KEY AUTOINCREMENT,
             color_name TEXT NOT NULL,
             created_data text NOT NULL)''') 

cursor.execute('''CREATE TABLE IF NOT EXISTS size 
                (size_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    size_name TEXT NOT NULL,
                    created_data text NOT NULL)''') 

cursor.execute('''CREATE TABLE IF NOT EXISTS products
                (product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name TEXT NOT NULL,
                    product_price integer NOT NULL,
                    product_description TEXT NOT NULL,
                    subcategory_id integer NOT NULL,
                    color_id integer NOT NULL,
                    size_id integer NOT NULL,
                    created_data text NOT NULL,
                    FOREIGN KEY (subcategory_id) REFERENCES subcategory(subcategory_id),
                    FOREIGN KEY (color_id) REFERENCES colors(color_id),
                    FOREIGN KEY (size_id) REFERENCES size(size_id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS cart
                (cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id integer NOT NULL,
                    product_id integer NOT NULL,
                    quantity integer NOT NULL,
                    created_data text NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                    FOREIGN KEY (product_id) REFERENCES products(product_id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                (order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id integer NOT NULL,
                    product_id integer NOT NULL,
                    quantity integer NOT NULL,
                    order_status TEXT NOT NULL,
                    created_data text NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                    FOREIGN KEY (product_id) REFERENCES products(product_id))''')

conn.commit()
print("Table created successfully")
conn.close()

