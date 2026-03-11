students = []
choice = "-"
operations = ["Add Student","Remove Student","View Students","Sort By Marks","Show Topper"]
while choice != '0':
    for index, operation in enumerate(operations):
        print(index + 1,' : ',operation)
        
    user_choice = input("Enter your choice ")
    if user_choice == '0':
        break
    
    elif user_choice == '1':
        student_name = input("Enter student name to add ")
        marks = int(input("Enter marks "))
        students.append([student_name,marks])
        print("Details added {}".format(student_name))
        
    elif user_choice == '2':
        student_name = input("Enter student name to remove ")
        names = [name for name, marks in students]
        if student_name in names:
           students = [student for student in students if student[0] != student_name]
           print("removed student")
        else:
          print("Student not found")
          
    elif user_choice == '3':
        for index,student in enumerate(students):
            print(index + 1,':',student[0],'-',student[1])
            
    elif user_choice == '4':
        students.sort(key=lambda x:x[1])
        sorted_students = sorted(students,key=lambda x: x[1],reverse=True)
        print('Top 3 students :',sorted_students[:3])
        
    elif user_choice == '5':
        topper = max(students,key=lambda x:x[1])
        print('Topper : ',topper)