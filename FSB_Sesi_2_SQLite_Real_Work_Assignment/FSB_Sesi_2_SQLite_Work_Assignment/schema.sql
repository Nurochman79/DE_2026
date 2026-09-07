-- SOURCE OF TRUTH: lengkapi constraints
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;
CREATE TABLE users(user_id TEXT, -- TODO PRIMARY KEY
 name TEXT,email TEXT,city TEXT);
CREATE TABLE products(product_id TEXT, -- TODO PRIMARY KEY
 name TEXT, -- TODO NOT NULL
 price REAL, -- TODO NOT NULL CHECK >=0
 category TEXT);
CREATE TABLE transactions(tx_id TEXT, -- TODO PRIMARY KEY
 user_id TEXT,product_id TEXT,quantity INTEGER,tx_date TEXT
 -- TODO NOT NULL, CHECK, dan 2 FOREIGN KEY
);
