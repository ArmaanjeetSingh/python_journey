class Employee(object):
    def __init__(self,name,salary):
        self._name = name
        self._salary = salary

    def calculate_bonus(self):
        return 0

    def total_salary(self):
        return self._salary + self.calculate_bonus()

    def get_name(self):
        return self._name

    def increase_salary(self, percent):

        self._salary += self._salary * percent


class EmployeeManager:
    def __init__(self):
        self._employee_role={'manager':Manager,'developer':Developer,'intern':Intern}
        self._employees = {}

    def load_from_dict(self,employees):
        for emp_id, details in employees.items():
            role = details["role"].casefold()
            emp_map = self._employee_role.get(role)

            if emp_map:
                self._employees[emp_id] = emp_map(details["name"], details["salary"])

    def add_employee(self, emp_id, obj):
        self._employees[emp_id] = obj

    def remove_employee(self, emp_id):
        if emp_id in self._employees:
            del self._employees[emp_id]

    def display_all(self):
        for emp_id, obj in self._employees.items():
            print(f"{emp_id} : {obj.get_name()} {obj.total_salary()}")


class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)

    def calculate_bonus(self):
        return self._salary * 0.2

class Developer(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)

    def calculate_bonus(self):
        return self._salary * 0.1

class Intern(Employee):
    def calculate_bonus(self):
        return self._salary * 0.05

if __name__ == '__main__':

    emp_manager = EmployeeManager()
    employees = {
    "E1": {"name": "Sumit", "role": "Manager", "salary": 50000},
    "E2": {"name": "Rahul", "role": "Developer", "salary": 40000}
    }

    manager = EmployeeManager()

    manager.load_from_dict(employees)

    print("Before increment:")
    manager.display_all()

    manager._employees["E1"].increase_salary(0.1)

    print("\nAfter increment:")
    manager.display_all()

    manager.remove_employee("E2")

    print("\nAfter removal:")
    manager.display_all()
        
