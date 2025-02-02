import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (Change credentials if necessary)
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",  # Change to your MySQL username
            password="your_password"  # Change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Creating the database (IF NOT EXISTS ensures it won't fail if already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        # Ensure cursor and connection are properly closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Execute the function
create_database()
