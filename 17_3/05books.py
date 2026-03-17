class Book :
    def __init__(self,title,author,price):
        self._title = title
        self._author = author
        self._price = price

    #create getter methods
    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_price(self):
        return self._price

    #create setter methods
    def set_price(self,new_price):
        if new_price > 0:
            self._price = new_price


def add_book(library):
        title = input("Enter title : ")
        author = input("Enter author : ")
        price = int(input("Enter price : "))
        book = Book(title, author, price)
        library.append(book)    
        
def search_book(library,title):
        for book in library:
            if book.get_title() == title:
                 print("Book found:", book.get_author(), book.get_price())
library = []

while True:

    print("1 Add Book")
    print("2 Show Books")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book(library)

    elif choice == "2":
        for book in library:
            print(book.get_title(), book.get_author(), book.get_price())

    elif choice == "3":
        break