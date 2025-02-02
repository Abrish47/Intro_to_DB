-- task_6.sql
-- Script to insert multiple rows into the customer table in the alx_book_store database.

-- Use the database specified as an argument.  This is handled by the mysql command-line client.
-- Example usage: mysql -u <user> -p <password> alx_book_store < task_6.sql

INSERT INTO customer (customer_id, customer_name, email, address)
VALUES
    (2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
    (3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
    (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');

-- Optional: Verify the insertion
SELECT * FROM customer;  -- This will display all rows in the customer table after the insert.  Remove or comment out for production.
