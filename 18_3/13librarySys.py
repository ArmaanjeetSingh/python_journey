class Book:
    def __init__(self,id,title,author):
        self._id = id
        self._title = title
        self._author = author
        self._available = True

    def is_available(self):
        return self._available

    def borrow(self):
        if self._available:
            self._available = False
            return True
        return False
    def return_book(self):
        self._available = True


class User:
    def __init__(self,user_id,name):
        self._id = user_id
        self._name = name
        self._borrowed_books = []

    def borrow_book(self,book):
        self._borrowed_books.append(book)

    def return_book(self,book):
        self._borrowed_books.remove(book)

    def show_book(self):
        return [b._title for b in self._borrowed_books]


class Library:
    def __init__(self):
        self._books = {}
        self._users = {}
        self._requests = []

    def add_book(self,book):
        self._books[book._id] = book

    def register_user(self, user):
        self._users[user._id] = user


    def issue_book(self,user_id,book_id):
        user = self._users.get(user_id)
        book = self._books.get(book_id)

        if not user or not book:
            print("Invalid user or book")
            return

        if book.borrow():
            user.borrow_book(book)
            print(f"{book._title} issued to {user._name}")
        else:
            print("Book not available, added to queue")
            self._requests.append((user_id, book_id))

    def return_book(self, user_id, book_id):
        user = self._users.get(user_id)
        book = self._books.get(book_id)

        if user and book:
            book.return_book()
            user.return_book(book)
            print(f"{book._title} returned")

            self.process_queue(book_id)

    def process_queue(self, book_id):
        i = 0
        while i < len(self._requests):
            u_id, b_id = self._requests[i]

            if b_id == book_id:
                print(f"Notifying user {u_id} for book {book_id}")
                self._requests.pop(i)
                return
            i += 1

    def show_available_books(self):
        for book in self._books.values():
            if book.is_available():
                print(book._title)

if __name__ == "__main__":
    lib = Library()
    b1 = Book(1,"Python",'Guido')
    b2 = Book(2,"DSA","CLRS")

    lib.add_book(b1)   
    lib.add_book(b2)

    u1 = User(101, "Rajesh")
    u2 = User(102, "Rahul")

    lib.register_user(u1)
    lib.register_user(u2)

    lib.issue_book(101, 1)
    lib.issue_book(102, 1)

    lib.return_book(101,1)
