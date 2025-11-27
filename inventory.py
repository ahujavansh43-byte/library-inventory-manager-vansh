from book import Book

class LIBRARYInventory:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def display_all(self):
        if not self.books:
            print("No books in inventory.")
        else:
            for book in self.books:
                print(book)

    def save_books(self):
        pass  # Placeholder if file saving is needed later