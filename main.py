from inventory import LIBRARYInventory
from book import Book

LIBRARY = LIBRARYInventory()

def menu():
    while True:
        print("\n--- LIBRARY Inventory Manager ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            LIBRARY.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = LIBRARY.search_by_isbn(isbn)
            if book and book.issue():
                LIBRARY.save_books()
                print("Book issued successfully!")
            else:
                print("Book not available.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = LIBRARY.search_by_isbn(isbn)
            if book and book.return_book():
                LIBRARY.save_books()
                print("Book returned!")
            else:
                print("Invalid operation.")

        elif choice == "4":
            LIBRARY.display_all()

        elif choice == "5":
            term = input("Enter title to search: ")
            results = LIBRARY.search_by_title(term)
            if results:
                for b in results:
                    print(b)
            else:
                print("No books found.")

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")

menu()