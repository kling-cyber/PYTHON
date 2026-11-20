BEGIN TRANSACTION;
CREATE TABLE city (ctid INTEGER PRIMARY KEY AUTOINCREMENT, city_name TEXT NOT NULL, sid integer NOT NULL, created_data text NOT NULL);
CREATE TABLE country (cid INTEGER PRIMARY KEY AUTOINCREMENT, country_name TEXT NOT NULL, created_data text NOT NULL);
CREATE TABLE state (sid INTEGER PRIMARY KEY AUTOINCREMENT, state_name TEXT NOT NULL, cid integer NOT NULL, created_data text NOT NULL);
CREATE TABLE users (uid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, password TEXT NOT NULL, mobile integer NOT NULL, gender TEXT NOT NULL, hobby TEXT NOT NULL, pincode integer NOT NULL, email TEXT NOT NULL, created_data text NOT NULL);
COMMIT;
