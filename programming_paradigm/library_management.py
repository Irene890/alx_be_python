# # implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation

class Book:
    def __init__(self, title: str, author: str):
        #public_attributes
        self.title = title
        self.author = author
        #private_attribute
        self._is_checked_out = False

    def checkout(self):
        if not self._is_checked_out:
            self._is_checked_out = True

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False

    def is_available(self) -> bool:
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        #list to store all books
        self._books = []
    def add_book(self, book: Book):
        self._books.append(book)

    def _find_a_book(self, title: str) -> Book | None:
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title: str):
        book = self._find_a_book(title)
        if book:
            book.checkout()

    def return_book(self, title: str):
        book = self._find_a_book(title)
        if book:
            book.return_book()

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(str(book))
