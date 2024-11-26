import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",  # Update with your host
        user="root",       # Update with your username
        password="password",  # Update with your password
        database="library_db"  # Your database name
    )
    return connection
