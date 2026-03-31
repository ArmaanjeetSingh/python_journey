import csv
class Student:
    def __init__(self,name,roll_no,marks:dict):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

class StudentManager:
    def __init__(self):
        self.student_list = []
        self.total = {}

    def add_student(self,name,roll_no,marks):
        self.student_list.append(Student(name,roll_no,marks))

    def display_students(self):
        for student in self.student_list:
            print(f'Name : {student.name}, Roll No : {student.roll_no}')
            for sub,mark in student.marks.items():
                print(f'Subject : {sub}, Marks : {mark}')

    def save_to_file(self):
        with open('my_student.csv','w',newline='') as file_output:
            writer = csv.DictWriter(file_output,fieldnames=['name','roll_no','marks'])
            writer.writeheader()
            for student in self.student_list:
                # row = [student.name,student.roll_no,student.marks]
                writer.writerows({
                    'name':student.name,
                    'roll_no':student.roll_no,
                    'marks':student.marks
                })
            

    def total_marks(self):

        for student in self.student_list:
            
            for sub,mark in student.marks.items():
                print(student.name,mark)
                self.total[student.name] = self.total.setdefault(student.name,0)+mark
            self.total[student.name] //=2
        
        for student in self.total:
            print(student," : ",self.total[student])




if __name__ == '__main__':
    std = StudentManager()
    std.add_student('Armaan',123,{"math":78,"science":54})
    std.add_student('Sahil',125,{"math":38,"science":59})
    std.display_students()
    std.total_marks()
    std.save_to_file()
    