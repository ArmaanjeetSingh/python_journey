
class Author:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)


class Book:
    def __init__(self,title):
        self.title = title


authors = []
current_author = None

with open("library.txt","r",encoding='utf-8',newline='') as input_file:
    for line in input_file:
        author_name, book_title = line.strip().split('\t')
        if current_author is None:
            current_author = Author(author_name)

        elif current_author.name != author_name:
            authors.append(current_author)
            current_author = Author(author_name)

        new_book = Book(book_title)
        current_author.add_book(new_book)
authors.append(current_author)

for author in authors:
    print(author.name)
    for book in author.books:
        print("  ", book.title)