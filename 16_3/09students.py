class Student:

    def __init__(self,name:str):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

class Course:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

students = []
current_student = None


with open("students.txt","r",encoding="utf-8",newline='') as input_file:
    for line in input_file:
        student_name,course_name,marks = line.strip('\n').split("\t")
        marks = int(marks)

        if current_student is None:
            current_student = Student(student_name)


        elif current_student.name != student_name:
            students.append(current_student)
            current_student = Student(student_name)

        new_course = Course(course_name, marks)

        current_student.add_course(new_course)
students.append(current_student)

for student in students:
    print(student.name)
    for course in student.courses:
        print("  ",course.name,course.marks)