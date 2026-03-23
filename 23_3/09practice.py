import sqlite3
# from datetime import datetime
import datetime
from zoneinfo import ZoneInfo

class ExpenseTracker:
    def __init__(self):
        self.db = sqlite3.connect("expense.db")
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER,
            category TEXT,
            description TEXT,
            time TIMESTAMP
        )
        """)


    def add_expense(self,amount,category,description):
        current_time = self.get_current_time()

        self.db.execute(
            "INSERT INTO expenses (amount, category, description, time) VALUES (?, ?, ?, ?)",
            (amount, category, description, current_time)
        )
        self.db.commit()


    def view_expenses(self):
        for row in self.db.execute("SELECT id,amount,category,description,strftime('%d-%m-%Y %H:%M',time,'localtime') AS localtime FROM expenses;"):
            print(f"ID : {row[0]}, Amount : {row[1]}, Category : {row[2]}, Description : {row[3]}")


    def total_spent(self):
        cursor = self.db.execute("SELECT SUM(amount) FROM expenses")
        result = cursor.fetchone()[0]
        print("Total spent:", result)

    def category_total(self):
        cursor = self.db.execute("SELECT category,SUM(amount) FROM expenses GROUP BY category")
        result = cursor.fetchall()
        for (category,total) in result:
            print(f'Category : {category}, Total : {total}')

    
    def show_by_latest(self):
        cursor = self.db.execute("SELECT category,amount,description,strftime('%d-%m-%Y %H:%M',time,'localtime'),id AS localtime FROM expenses ORDER BY time DESC")
        for row in cursor:
            print(f"Category : {row[0]}, Amount : {row[1]}, Description : {row[2]}, time : {row[3]}, ID : {row[4]}")

    def delete_expense(self, id):
        self.db.execute("DELETE FROM expenses WHERE id = ?", (id,))
        self.db.commit()



    @staticmethod
    def get_current_time():
        return datetime.datetime.now(datetime.timezone.utc).isoformat()





if __name__ == '__main__':
    exp1 = ExpenseTracker()
    # exp1.add_expense(10,"bills","electricity")
    # exp1.add_expense(30,"bills","water supply")
    # exp1.add_expense(15,"bills","lpg supply")
    # exp1.add_expense(15,"emi","car")
    # exp1.add_expense(15,"emi","phone")
    exp1.view_expenses()
    exp1.category_total()
    exp1.show_by_latest()
