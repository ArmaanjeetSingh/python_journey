class Employee:
    def __init__(self,emp_id,name,age,salary,tasks:list):
        self._emp_id = emp_id
        self._name = name
        self._age = age
        self._salary = salary
        self.tasks = tasks

    def get_details(self):
        return f"Emp ID : {self._emp_id} Name : {self._name} Age : {self._age}"

    def calculate_salary(self):
        return f"{self._name} has salary {self._salary}"

    def get_tasks(self):
        for item in self.tasks:
            print(item)

class Manager(Employee):
    def __init__(self,emp_id,name,age,tasks,salary,bonus):
        super().__init__(emp_id,name,age,salary,tasks)
        self._bonus = bonus

    def calculate_salary(self):
        return f"{self._name} has salary {self._salary + self._bonus*0.2}"


class Developer(Employee):
    def __init__(self,emp_id,name,age,tasks,salary,overtime):
        super().__init__(emp_id,name,age,salary,tasks)
        self.overtime = overtime

    def calculate_salary(self):
        return f"{self._name} has salary {self.salary+500*overtime}"

if __name__ == '__main__':
    # emp = Employee(101,'armaan',22,2000,['check network','clock in'])
    emp1 = Manager(102,'rohit',25,['check network','clock in'],3000,500)
    emp2 = Developer(103,'rahul',28,['fix bug','add feature'],2500,2)
    print(emp1.get_details())
    print(emp1.calculate_salary())
    emp2.get_tasks()