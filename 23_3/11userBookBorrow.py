import sqlite3
import datetime

class LibrarySystem:
    def __init__(self):
        self.db = sqlite3.connect("library.db")
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
        )
         """)
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
        )
         """)
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS borrowed(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        book_id INTEGER,
        borrow_date TIMESTAMP,
        due_date TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(book_id) REFERENCES books(id)
        )
         """)

    @staticmethod
    def get_current_time():
        return datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    def add_user(self,user_name):
        self.db.execute("INSERT INTO users (name) VALUES (?)",(user_name,))
        self.db.commit()

    def add_book(self,title):
        self.db.execute("INSERT INTO books (title) VALUES (?)",(title,))
        self.db.commit()

    def borrow_book(self,user_id,book_id):
        borrow_date = datetime.datetime.now(datetime.timezone.utc)
        due_date = borrow_date + datetime.timedelta(days=7)
        self.db.execute("INSERT INTO borrowed (user_id,book_id,borrow_date,due_date)  VALUES (?,?,?,?)",(user_id,book_id,borrow_date.isoformat(),due_date.isoformat()))
        self.db.commit()

    def return_book(self,user_id,book_id):
        
        self.db.execute("DELETE FROM borrowed WHERE book_id = ?, user_id = ?",(book_id,user_id))
        self.db.commit()
        # print(f'{}')

    def show_borrowed_books(self):
        cursor = self.db.execute("""
        SELECT u.name,b.title, strftime('%d-%m-%Y',br.borrow_date,'localtime'), strftime('%d-%m-%Y', br.due_date, 'localtime') FROM users AS u
        JOIN borrowed AS br ON u.id = br.user_id
        JOIN books AS b ON b.id = br.book_id;
        """)
        result = cursor.fetchall()
        for row in result:
            print(f'{row[0]} borrowed book {row[1]} on {row[2]}, has to return on {row[3]}')

    def show_overdue(self):
        current_date = self.get_current_time()
        cursor = self.db.execute("""
        SELECT u.name,b.title,strftime('%d-%m-%Y', br.due_date, 'localtime') FROM users AS u
        JOIN borrowed AS br ON u.id = br.user_id
        JOIN books AS b ON b.id = br.book_id
        WHERE br.due_date < ?
        """,(current_date,))
        for row in cursor:
            print(f"User {row[0]} has overdue book {row[1]},Due: {row[2]}")

if __name__ == '__main__':
    lb = LibrarySystem()
    # lb.add_user("Sohan")
    # lb.add_book("Marvel Comic")
    # lb.borrow_book(1, 1)
    # lb.add_user("Mohan")
    # lb.add_book("Harry potter book")
    # lb.borrow_book(2,2)
    lb.show_borrowed_books()
    lb.show_overdue()
