class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_info(self):
        print(f"{self.title} - {self.author} ({self.year})")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("Список книг у бібліотеці:")
        for book in self.books:
            book.show_info()


library = Library()
library.add_book(Book("Кобзар", "Тарас Шевченко", 1840))
library.add_book(Book("Енеїда", "Іван Котляревський", 1798))
library.show_books()