from database import create_connection

class User:
    @staticmethod
    def add_user(username, email, password, role):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Users (username, email, password, role)
        VALUES (%s, %s, %s, %s)
        """, (username, email, password, role))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_users():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()
        conn.close()
        return users

    @staticmethod
    def authenticate_user(email, password):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        conn.close()
        return user
