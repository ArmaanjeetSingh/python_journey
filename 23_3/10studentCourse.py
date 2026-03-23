import sqlite3

class StudentCourseSystem:
    def __init__(self):
        self.db = sqlite3.connect("school.db")
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS students(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT
        ) """)
        
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT
        )
        """) 

        self.db.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           student_id INTEGER,
           course_id INTEGER,
           FOREIGN KEY (student_id) REFERENCES students(id),
           FOREIGN KEY (course_id) REFERENCES courses(id)
        )""")

    def add_student(self,name):
        self.db.execute("""
        INSERT INTO students(name) VALUES (?) """,(name,))
        self.db.commit()

    def add_course(self,course_name):
        self.db.execute(
            "INSERT INTO courses(course_name) VALUES (?)",(course_name,))
        self.db.commit()

    def enroll(self,student_id,course_id):
        self.db.execute("INSERT INTO enrollments (student_id,course_id) VALUES(?,?)",(student_id,course_id))
        self.db.commit()

    def show_enrollments(self):
        cursor = self.db.execute(""" 
        SELECT s.name, c.course_name FROM students AS s
        INNER JOIN enrollments AS e ON s.id = e.student_id
        INNER JOIN courses AS c ON c.id = e.course_id
        """)
        result = cursor.fetchall()
        for row in result:
            print(f"{row[0]} is enrolled in {row[1]}")

    def view_students(self):
        for row in self.db.execute("SELECT * FROM students"):
            print(row)

    def view_courses(self):
        for row in self.db.execute("SELECT * FROM courses"):
            print(row)


if __name__ == '__main__':
    system = StudentCourseSystem()
    # system.add_student("John")
    # system.add_student("Alice")

    # system.add_course("Math")
    # system.add_course("Python")

    # system.enroll(1, 1)
    # system.enroll(1, 2)
    # system.enroll(2, 1)

    system.show_enrollments()
    system.view_courses()

