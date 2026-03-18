class Student:
    def __init__(self,id,name):
        self._name = name
        self._id = id
        self._courses = []

    def enroll(self,course):
        if course not in self._courses:
            self._courses.append(course)
        else:
            print(f"{course} already exists")

    def show_courses(self):
        return [course for course in self._courses]

class Course:
    def __init__(self,id,name,capacity):
        self._id = id
        self._name = name
        self._capacity = capacity
        self._students = []

    def add_student(self,student):
        if student not in self._students:
            self._students.append(student)
        else:
            print(f"{student} already exists")

    def is_available(self):
        return len(self._students) < self._capacity

class System:
    def __init__(self):
        self._students = {}
        self._courses = {}

    def add_student(id,student):
        if id not in self._students:
           self._students[id] = student

    def add_course(id,course):
        if id not in self._courses:
           self._courses[id] = course

    def enroll_student(self, student_id, course_id):
        student = self._students.get(student_id)
        course = self._courses.get(course_id)
        if not student or not course:
           print("Invalid student or course")
           return

        if course.is_available():
            course.add_student(student)
            student.enroll(course)
        else:
            print("Course full")



        