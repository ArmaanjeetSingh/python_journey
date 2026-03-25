import sqlite3

class SalesDB:
    def __init__(self, db_name="sales"):
        self.conn = sqlite3.connect(db_name)

    def get_employees_report(self):
        cursor = self.conn.execute("""SELECT e.first_name,e.lastname,d.DepartmentName FROM Employees e 
        JOIN Departments d ON d.DepartmentID  = e.DepartmentID""")
        result = cursor.fetchall()
        return [row for row in result]

if __name__ == '__main__':
    sales = SalesDB()
    sales.get_employees_report()