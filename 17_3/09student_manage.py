class Student:

    def __init__(self,name,marks:dict):
        self._name = name
        self._marks  = marks

    def get_details(self):
        print("Name : ",self._name)
        for sub,mark in self._marks.items():
            print("Subject : {}, Marks : {}".format(sub,mark))

    def calculate_average(self):
        if not self._marks:
            return 0
        total =  0
        for sub,mark in self._marks.items():
           total += mark
        return total//len(self._marks) 


class SchoolStudent(Student):
    def __init__(self,name,marks:dict,grade):
        super().__init__(name,marks)
        self._grade = grade

    def get_details(self):
        super().get_details()
        print('Grade : ',self._grade)

class CollegeStudent(Student):
    def __init__(self,name,marks:dict,major:str):
        super().__init__(name,marks)
        self._major = major

    def calculate_average(self):
        passed_marks = [m for m in self._marks.values() if m >= 40]
        if not passed_marks:
            return 0
        return sum(passed_marks)/len(passed_marks)

students = [
    Student("A", {"math": 80, "science": 90}),
    SchoolStudent("B", {"math": 70, "science": 60}, "A"),
    CollegeStudent("C", {"math": 30, "science": 70}, "CSE")
]

for s in students:
    s.get_details()
    print("Average:", s.calculate_average())