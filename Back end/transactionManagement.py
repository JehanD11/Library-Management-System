from database import create_connection
from user import Book

class Transaction:
    @staticmethod
    def borrow_book(user_id, book_id):
        """
        Borrow a book by a user. Decreases the book's quantity by 1 and logs the transaction.
        """
        conn = create_connection()
        cursor = conn.cursor()

        # Check if the book is available
        cursor.execute("SELECT quantity FROM Books WHERE id = %s", (book_id,))
        book = cursor.fetchone()
        if not book or book[0] <= 0:
            conn.close()
            return "Book is not available for borrowing."

        try:
            # Record the borrowing transaction
            cursor.execute("""
                INSERT INTO Transactions (user_id, book_id, type)
                VALUES (%s, %s, 'borrow')
            """, (user_id, book_id))

            # Decrease the book quantity
            cursor.execute("""
                UPDATE Books SET quantity = quantity - 1 WHERE id = %s
            """, (book_id,))

            conn.commit()
            return "Book borrowed successfully!"
        except Exception as e:
            conn.rollback()
            return f"Error borrowing book: {e}"
        finally:
            conn.close()

    @staticmethod
    def return_book(user_id, book_id):
        """
        Return a book by a user. Increases the book's quantity by 1 and logs the transaction.
        """
        conn = create_connection()
        cursor = conn.cursor()

        try:
            # Record the return transaction
            cursor.execute("""
                INSERT INTO Transactions (user_id, book_id, type)
                VALUES (%s, %s, 'return')
            """, (user_id, book_id))

            # Increase the book quantity
            cursor.execute("""
                UPDATE Books SET quantity = quantity + 1 WHERE id = %s
            """, (book_id,))

            conn.commit()
            return "Book returned successfully!"
        except Exception as e:
            conn.rollback()
            return f"Error returning book: {e}"
        finally:
            conn.close()

    @staticmethod
    def get_user_transactions(user_id):
        """
        Get all transactions for a specific user.
        """
        conn = create_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT Transactions.id, Books.title, Transactions.type, Transactions.date 
                FROM Transactions
                JOIN Books ON Transactions.book_id = Books.id
                WHERE Transactions.user_id = %s
                ORDER BY Transactions.date DESC
            """, (user_id,))
            transactions = cursor.fetchall()
            return transactions
        except Exception as e:
            return f"Error retrieving transactions: {e}"
        finally:
            conn.close()

    @staticmethod
    def get_all_transactions():
        """
        Get all transactions across all users.
        """
        conn = create_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT Transactions.id, Users.username, Books.title, Transactions.type, Transactions.date
                FROM Transactions
                JOIN Books ON Transactions.book_id = Books.id
                JOIN Users ON Transactions.user_id = Users.id
                ORDER BY Transactions.date DESC
            """)
            transactions = cursor.fetchall()
            return transactions
        except Exception as e:
            return f"Error retrieving all transactions: {e}"
        finally:
            conn.close()
