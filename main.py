class Book:
    def __init__(self, title, author, available=True):
        self.__title = title
        self.__author = author
        self.__available = available

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    def borrow(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True


class Library:
    def __init__(self):
        self.__books = {}

    def add_book(self, book):
        self.__books[book.get_title()] = book

    def get_book(self, title):
        return self.__books.get(title)

    def list_available_books(self):
        return [book for book in self.__books.values() if book.is_available()]


class User:
    def __init__(self, name):
        self.__name = name

    def borrow_book(self, library, title):
        book = library.get_book(title)
        if book and book.borrow():
            print(f"{self.__name} kitobni oldi: {title}")
            return True
        print(f"{title} mavjud emas yoki allaqachon olingan.")
        return False

    def return_book(self, library, title):
        book = library.get_book(title)
        if book:
            book.return_book()
            print(f"{self.__name} kitobni qaytardi: {title}")
            return True
        print(f"{title} kutubxonada topilmadi.")
        return False
