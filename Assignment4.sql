-- Design a simple database schema for a customer management system.
-- Implement the schema using a relational database management system (e.g., MySQL, PostgreSQL, or SQLite).
-- Write SQL queries to perform basic CRUD (Create, Read, Update, Delete) operations on the database.
-- Bonus: Implement additional features, such as data validation, indexing, or query optimization.

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL CHECK (email LIKE '%@%.%'),
    phone TEXT CHECK (length(phone) >= 10 and length(phone) <= 15),
    address TEXT
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount REAL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)

);

CREATE INDEX idx_customer_email ON Customers (email);

-- crud orpertions

INSERT INTO Customers (first_name, last_name, email, phone, address)
VALUES ('James', 'Bond', 'Jamesbond007@gmail.com', '0000000007', 'Heaven');

INSERT INTO Orders (customer_id, order_date, total_amount)
VALUES ('1', '2024-04-30', 100.50);

SELECT * FROM Customers;

SELECT * FROM Orders;

UPDATE Customers
SET phone = '0070070007'
WHERE email = 'Jamesbond007@gmail.com';

UPDATE Orders
SET total_amount = 150.75
WHERE order_id = 1;

DELETE FROM Orders
WHERE order_id = 1;

DELETE FROM Customers
WHERE customer_id = 1;


