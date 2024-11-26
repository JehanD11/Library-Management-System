from database import create_connection
from models.book import Book

class Transaction:
    @staticmethod
    def borrow_book(user_id, book_id):
        book = Book.get_book_by_id(book_id)
        if book and book[4] > 0:  # Check if the book is available
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO Transactions (user_id, book_id, type, date)
            VALUES (%s, %s, 'borrow', NOW())
            """, (user_id, book_id))
            conn.commit()
            conn.close()
            Book.update_book_quantity(book_id, -1)
            return True
        return False

    @staticmethod
    def return_book(user_id, book_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Transactions (user_id, book_id, type, date)
        VALUES (%s, %s, 'return', NOW())
        """, (user_id, book_id))
        conn.commit()
        conn.close()
        Book.update_book_quantity(book_id, 1)

    @staticmethod
    def get_user_transactions(user_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT Transactions.id, Books.title, Transactions.type, Transactions.date 
        FROM Transactions
        JOIN Books ON Transactions.book_id = Books.id
        WHERE Transactions.user_id = %s
        """, (user_id,))
        transactions = cursor.fetchall()
        conn.close()
        return transactions
