class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = False

    def issue(self):
        if not self.is_issued:
            self.is_issued = True
            return True
        return False

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            return True
        return False

    def _str_(self):
        status = "Issued" if self.is_issued else "Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"