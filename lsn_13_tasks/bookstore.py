class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def add_book(self, book: 'Book'):
        if isinstance(book, Book):
            self.books.append(book)
            if not (book.get_author in self.authors):
                self.authors.append(book.get_author)
        else:
            raise TypeError('book is not Book class object')

    def group_by_authors(self, author: 'Author'):
        if isinstance(author, Author):
            return [book for book in self.books if book.get_author == author]

    def group_by_year(self, year: int):
        if isinstance(year, int):
            return [book for book in self.books if book.get_year == year]

    def __repr__(self):
        return self.name

    def __str__(self):
        self.__repr__()

    @property
    def get_books(self):
        return self.books

    @property
    def get_authors(self):
        return self.authors


class Author:
    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books_list = []

    def write_book(self, name: str, year: int):
        for book in self.books_list:
            if book == name:
                raise NameError('Book name is already used')
        self.books_list.append(Book(name, year, self))

    def __repr__(self):
        return self.name

    def __str__(self):
        self.__repr__()

    @property
    def book_list(self):
        return self.books_list

    @book_list.setter
    def book_list(self, books: list):
        if isinstance(books, list):
            self.books_list = books
        else:
            raise TypeError('Books isn`t list')

    @property
    def get_name(self):
        return self.name

    @property
    def get_county(self):
        return self.country

    @property
    def get_birthday(self):
        return self.birthday


class Book:
    COUNTER_BOOKS = 0

    def __init__(self, name: str, year: int, author: Author):
        if isinstance(author, Author):
            self.author = author
            temp_holder = author.book_list
            temp_holder.append(self)
            author.book_list = temp_holder
        else:
            raise TypeError('author is not Author class object')
        self.name = name
        self.year = year

        Book.COUNTER_BOOKS += 1

    def __repr__(self):
        return self.name

    def __str__(self):
        self.__repr__()

    @property
    def get_author(self):
        return self.author

    @property
    def get_name(self):
        return self.name

    @property
    def get_year(self):
        return self.year


