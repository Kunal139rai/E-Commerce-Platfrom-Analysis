 # This file handles the database connection and disconnection.

# db_connection.py
import pymysql

def get_connection():
    try:
        # Database connection details
        host = 'localhost'
        port = 3306
        user = 'root'
        password = 'admin'
        database = 'ecommerce_db'

        # Establish a connection to the MySQL database
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        if connection.open:
            print("Successfully connected to the MySQL database.")

        return connection  # Return the connection object

    except Exception as e:
        print("Error while connecting to MySQL:", e)
        return None  # Return None if there's an error

def close_connection(connection, cursor=None):
    if cursor is not None:
        cursor.close()

    if connection is not None:
        connection.close()
        print("MySQL connection closed.")
