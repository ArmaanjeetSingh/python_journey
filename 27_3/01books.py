class Book:
    def __init__(self,title,author,copies):
        self.data = {
            "title":title,
            "author":author ,
            "copies":copies,
            "available":True 
        }


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_book = []

    def add_book(self,title,author,copies):
        self.books.append(Book(title,author,copies))  
        return f"{title} has been added to Library"

    def show_books(self):
        for book in self.books:
            print(f"{book.data['title']} written by {book.data['author']} with {book.data['copies']} copies")

    def borrow_book(self,title):
        for index,book in enumerate(self.books):
            if title.casefold() == book.data['title'].casefold():
                if book.data['copies'] > 0:
                    bool.data['copies'] -= 1
                    print(f'{title} borrowed successfully')
                else:
                    print(f"{title} is out of stock")


    def return_book(self,title):
        for book in self.books:
            if title.casefold() == book.data['title'].casefold():
                book.data['copies'] += 1
                print("Book returned {}".format(book.data['title']))

        print("Book not found")


if __name__ == '__main__':
    lib = Library()
    lib.add_book("Harry Potter", "JK Rowling", 5)
    lib.add_book("Atomic Habits", "James Clear", 3)

    lib.show_books()

    lib.borrow_book("Harry Potter")
    lib.return_book("Harry Potter")    


                

