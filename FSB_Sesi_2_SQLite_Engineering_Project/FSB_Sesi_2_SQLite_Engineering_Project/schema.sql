DROP TABLE IF EXISTS transactions;DROP TABLE IF EXISTS products;DROP TABLE IF EXISTS users;
CREATE TABLE users(user_id TEXT PRIMARY KEY,name TEXT,email TEXT,city TEXT);
CREATE TABLE products(product_id TEXT PRIMARY KEY,name TEXT NOT NULL,price REAL NOT NULL CHECK(price>=0),category TEXT);
CREATE TABLE transactions(tx_id TEXT PRIMARY KEY,user_id TEXT NOT NULL,product_id TEXT NOT NULL,quantity INTEGER NOT NULL CHECK(quantity>0),tx_date TEXT,FOREIGN KEY(user_id) REFERENCES users(user_id),FOREIGN KEY(product_id) REFERENCES products(product_id));