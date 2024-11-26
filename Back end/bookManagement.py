from database import create_connection

class Book:
    @staticmethod
    def add_book(title, author, isbn, quantity):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Books (title, author, isbn, quantity)
        VALUES (%s, %s, %s, %s)
        """, (title, author, isbn, quantity))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_books():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def update_book_quantity(book_id, quantity_change):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Books SET quantity = quantity + %s WHERE id = %s", (quantity_change, book_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_book_by_id(book_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books WHERE id = %s", (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book
