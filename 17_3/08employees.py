class Employee :

    def __init__(self,name,salary):
        self._name = name
        self._salary =  salary

    def get_details(self):
        print(f"Name : {self._name}, Base salary: {self.calculate_salary()}")

    def calculate_salary(self):
        return self._salary

class Manager(Employee):

    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self._bonus = bonus

    def calculate_salary(self):
        return self._salary + self._bonus


class Developer(Employee):

    def __init__(self,name,salary,overtime):
        super().__init__(name,salary)
        self._overtime = overtime

    def calculate_salary(self):
        return self._salary + (self._overtime *500)
employees = [
    Manager("Vinayak", 50000, 10000),
    Developer("Arjun", 40000, 10)
]

for emp in employees:
    emp.get_details()
    print(f"Total Salary: {emp.calculate_salary()}")
    print("-" * 40)