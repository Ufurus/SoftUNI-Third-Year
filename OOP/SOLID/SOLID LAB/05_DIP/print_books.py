class Book:
    def __init__(self, content: str):
        self.content = content

class Formatter:
    def format(self, book: Book) -> str:
        return book.content

class PaperFormatter:
    def format(self, book: Book):
        return book.content[:2]

class Printer:
    def get_book(self, book: Book, formatter: Formatter) -> str:
        formatted_book = formatter.format(book)
        return formatted_book

f = Formatter()
pf = PaperFormatter()
b = Book("Hello There")
pr = Printer()
print(pr.get_book(b, f))