import csv
class Employee:
    def __init__(self, data):
        self.data = {
            "id": data["id"],
            "name": data["name"],
            "department": data["department"],
            "salary": int(data["salary"])
        }
        
class EmployeeManager:
    def __init__(self):
        self.employees = []

    def load_csv(self):
        with open('emp.csv', 'r') as emp_file:
            reader = csv.DictReader(emp_file)

            for row in reader:
                emp = Employee(row)
                self.employees.append(emp)

    def show_all_employees(self):
        for emp in self.employees:
            print(f"{emp.data['id']} : {emp.data['name']}")
