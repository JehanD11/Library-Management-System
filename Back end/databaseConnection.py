import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",  
        user="root",       
        password="password",  
        database="library_db"
    )
    return connection
