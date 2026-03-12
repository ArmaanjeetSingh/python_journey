from students import students

def show_all_students()->None:
    for student_id,info in students.items():
        print(f"ID : {student_id} Name : {info['name']}")

def add_new_student(student_id:int,student_name:str)->None:
    students.setdefault(student_id,{"name":student_name,"courses":{}})
    print(f"{student_name} is added with roll number {student_id}")


def add_courses(student_id:int,course:str,marks:int,grade:str)->None:
    student = students.get(student_id)

    if student:
        student["courses"][course] = {
            "marks":marks,
            "grade":grade
        }
    else:
        print("Student not found")

def view_student_details(student_id:int)->None:
    student = students.get(student_id)

    if not student:
        print("Student not found")
        return

    print("Name : ",student["name"])
    for course,data in student["courses"].items():
        print(course,data["marks"],data["grade"])


def update_marks(student_id:int,course:str,new_marks:int)->None:
    student = students.get(student_id)
    print(student)
    if student and course in student["courses"]:
        student["courses"][course]["marks"] = new_marks 

    else:
        print("Course or student not found")

def remove_course(student_id:int,course:str)->None:
    student = students.get(student_id)

    if student:
        removed = student["courses"].pop(course,None)

        if removed:
            print("Course removed")
        else:
            print("Course not found")

def remove_student(student_id):

    if student_id in students:
        del students[student_id]
        print("Student deleted")


while True:

    print("\n1 Show Students")
    print("2 Add Student")
    print("3 Add Course")
    print("4 View Student")
    print("5 Update Marks")
    print("6 Remove Course")
    print("7 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_all_students()

    elif choice == "2":
        sid = int(input("ID: "))
        name = input("Name: ")
        add_new_student(sid, name)

    elif choice == "3":
        sid = int(input("Student ID: "))
        course = input("Course: ")
        marks = int(input("Marks: "))
        grade = input("Grade: ")
        add_courses(sid, course, marks, grade)

    elif choice == "4":
        sid = int(input("Student ID: "))
        view_student_details(sid)

    elif choice == "6":
        sid = int(input("Student ID: "))
        course = input("Course: ")
        remove_course(sid,course)

    elif choice == "7":
        break