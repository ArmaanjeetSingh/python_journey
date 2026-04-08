class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name : {self.name}, Age : {self.age}")


class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks = marks

    def show_info(self):
        print(f"Name : {self.name}, Age : {self.age}, Marks : {self.marks}")

    def show_result(self):
        return "Pass" if self.marks >= 40 else "Fail"

    @staticmethod
    def role():
        print("Student")


class Teacher(Person):
    def __init__(self,name,age,sub):
        super().__init__(name,age)
        self.sub = sub

    def show_info(self):
        print(f"Name : {self.name}, Age : {self.age}, Subject : {self.sub}")

    def teach(self):
        print(f"{self.name} teaching subject {self.sub}")

    @staticmethod
    def role():
        print("Teacher")

if __name__ == '__main__':
    # student1 = Student("Armaan",13,54)
    # teacher1 = Teacher("Sharma",48,"Maths")
    # student1.show_info()
    # teacher1.show_info()
    people_list = [Student("Armaan",13,54),Teacher("Sharma",48,"Maths"),Student("Simran",15,36)]
    for person in people_list:
        person.show_info()
