import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", 3306)),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
        return connection
    except Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None


def fetch_books():
    connection = get_db_connection()
    if connection is None:
        return []

    try:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT b.id, b.title, b.author, b.description, b.price, c.name as category, p.name as publisher
        FROM books b
        LEFT JOIN categories c ON b.category_id = c.id
        LEFT JOIN publishers p ON b.publisher_id = p.id
        WHERE b.status = 1
        """
        cursor.execute(query)
        books = cursor.fetchall()
        return books
    except Error as e:
        print(f"Error fetching books: {e}")
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
