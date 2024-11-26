from models.user import User
from models.book import Book
from models.transaction import Transaction

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add User")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View All Books")
        print("6. View User Transactions")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            role = input("Role (admin/member): ")
            User.add_user(username, email, password, role)
            print("User added successfully!")
        
        elif choice == 2:
            title = input("Book Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            quantity = int(input("Quantity: "))
            Book.add_book(title, author, isbn, quantity)
            print("Book added successfully!")
        
        elif choice == 3:
            user_id = int(input("User ID: "))
            book_id = int(input("Book ID: "))
            if Transaction.borrow_book(user_id, book_id):
                print("Book borrowed successfully!")
            else:
                print("Book unavailable!")
        
        elif choice == 4:
            user_id = int(input("User ID: "))
            book_id = int(input("Book ID: "))
            Transaction.return_book(user_id, book_id)
            print("Book returned successfully!")
        
        elif choice == 5:
            books = Book.get_all_books()
            for book in books:
                print(book)
        
        elif choice == 6:
            user_id = int(input("User ID: "))
            transactions = Transaction.get_user_transactions(user_id)
            for transaction in transactions:
                print(transaction)
        
        elif choice == 7:
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
