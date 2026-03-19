class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self, *args):
        self.books = list(args)

    def find_book(self, title):
        try:
            return [el for el in self.books if el.title == title][0]
        except IndexError:
            return 'Book doesnt exist'

book1 = Book('Tomcat', 'Pesho')
book2 = Book('Cougar 2', 'Tomas Hill')
book3 = Book('Turkerneste', 'Omae Zihad')

lib = Library(book1, book2)
print(lib.find_book('Tomcat'))