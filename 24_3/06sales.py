import sqlite3

class SalesDB:
    def __init__(self, db_name="sales.db"):
        self.conn = sqlite3.connect(db_name)

    def get_employees_report(self):
        cursor = self.conn.execute("""SELECT e.FirstName,e.LastName,d.DepartmentName FROM Employees e 
        JOIN Departments d ON d.DepartmentID  = e.DepartmentID""")
        result = cursor.fetchall()
        return [f"{row[0]} {row[1]} {row[2]}" for row in result]


    def get_total_sales_by_product(self,product_name):
        productID = self.conn.execute("SELECT ProductID FROM Products WHERE ProductName = ? ",(product_name,)).fetchone()[0]
        if productID:
            cursor = self.conn.execute("SELECT SUM(Quantity) FROM Sales WHERE ProductID = ? ",(productID,))
            result = cursor.fetchall()
            return [row[0] for row in result]


    def sales_by_region(self,region_name):
        regionID = self.conn.execute("SELECT RegionID FROM Regions WHERE RegionName = ?",(region_name,)).fetchone()[0]
        if regionID:
            cursor = self.conn.execute("SELECT p.ProductName, s.Quantity,s.saleDate FROM Sales s INNER JOIN Products p ON p.ProductID = s.SaleID")
            result = cursor.fetchall()
            return [f"{row[0]} {row[1]} {row[2]}" for row in result]

    def add_new_sale(self,region_name,product_name,quantity,date):
        region_row = self.conn.execute("SELECT RegionID FROM Regions WHERE RegionName = ?",(region_name,)).fetchone()
        product_row = self.conn.execute("SELECT ProductID FROM Products WHERE ProductName = ?",(product_name,)).fetchone()

        if region_row and product_row:
            regionID = region_row[0]
            productID = product_row[0]
            self.conn.execute("INSERT INTO Sales (ProductID,RegionID,Quantity,SaleDate) VALUES (?,?,?,?)",(productID,regionID,quantity,date))

            self.conn.commit()

    def department_sal_costs(self):
        cursor = self.conn.execute("""
        SELECT d.DepartmentName, SUM(e.Salary) FROM Employees AS e 
        INNER JOIN Departments AS d
        ON d.DepartmentID = e.DepartmentID
        GROUP BY e.DepartmentID ; 
        """)
        result = cursor.fetchall()
        return [row for row in result]


    def get_monthly_sales_trend(self):

        query = """
        SELECT 
            strftime('%m', SaleDate) AS Month, 
             SUM(Quantity) AS TotalUnits
        FROM Sales
        GROUP BY Month
        ORDER BY Month ASC;
        """
        cursor = self.conn.execute(query)
        return cursor.fetchall()



if __name__ == '__main__':
    sales = SalesDB()
    print(sales.get_employees_report())
    print(sales.get_total_sales_by_product('Widget A'))
    print(sales.sales_by_region('South'))
    print(sales.add_new_sale('South','Widget C',5,'23-03-2026'))
    print(sales.department_sal_costs())
    print(sales.get_monthly_sales_trend())