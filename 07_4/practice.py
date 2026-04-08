class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, Result :{'Pass' if self.is_pass() else 'Fail'} Grade : {self.grade()}")

    def grade(self):
        if self.marks >= 80:
            return 'A'
        elif self.marks >= 60:
            return 'B'
        elif self.marks >= 40:
            return 'C'
        else:
            return 'Fail'

    def is_pass(self):
        return True if self.marks >= 40 else False


std = Student('Armaan',19)
std1 = Student('Rahul',87)
std.display()
std1.display()
print(std.grade())
print(std1.grade())
print(std.is_pass())