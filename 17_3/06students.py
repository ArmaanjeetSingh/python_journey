class Student:

    def __init__(self,std_id,name,marks):
        self._id = std_id
        self._name = name
        self._marks = marks

    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_marks(self):
        return self._marks
    def set_marks(self,new_marks):
        if 0<=new_marks<=100:
            self._marks = new_marks
        else:
            print("Invalid marks")


students = dict()

def add_student(students):
    std_id = input("Enter student id ")
    name = input("Enter student name ")
    marks = int(input("Enter marks"))
    students[std_id] = Student(std_id,name,marks)

def show_students(students):
    for student_id,student in students.items():
        print(f"{student_id} : {student.get_name()} -- {student.get_marks()}")

def search_student(students, student_id):
    if student_id in students:
        student = students[student_id]
        print(f"{student_id} : {student.get_name()} -- {student.get_marks()}")
    else:
        print("Student not found")

def update_marks(students, student_id, new_marks):
    if student_id in students:
       student = students[student_id]
       student.set_marks(new_marks) 
    else:
        print("Student not found")


def delete_student(students ,student_id):
    if student_id in students:
        del students[student_id]
        print(f"{student_id} is deleted")


while True:
    print("1 Add Student")
    print("2 Show Students")
    print("3 Search Student")
    print("4 Update Marks")
    print("5 Delete Student")
    print("6 Exit")

    choice = input("Enter your choice ")
    if choice == "1":
        add_student(students)
    elif choice == "2":
        show_students(students)
    elif choice == "3":
        student_id = input("Enter student id ")
        search_student(students,student_id)
    elif choice == "4":
        student_id = input("Enter student id ")
        new_marks = int(input("Enter new marks"))
        update_marks(student,student_id,new_marks)
    elif choice == "5":
        student_id = input("Enter student id ")
        delete_student(student_id)
    elif choice == "6":
        break
    else:
        print("Invalid choice")

    