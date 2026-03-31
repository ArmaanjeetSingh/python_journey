import functools
student_record  = {101:{"name":"Rahul","age":15,"marks":[34,56,78,43,84]},
                   102:{"name":"Simran","age":14,"marks":[74,59,88,43,63]},
                   103:{"name":"Rohit","age":15,"marks":[65,59,72,33,91]},
                   104:{"name":"Saurabh","age":16,"marks":[74,49,28,13,53]},
                }
count_roll = 104
available_options = ['Add student','Remove student','Show Student',"Total of Marks",'Sort By marks']
valid_choices = [str(i+1) for i in range(len(available_options))]


def show_students():
    for roll_no,details in student_record.items():
        print(f"Roll No. : {roll_no} : Name : {details['name']}, Age : {details['age']}")


def show_options():
    for index,val in enumerate(available_options,start=1):
        print(index,':',val)
    print('0 : exit')

def total_marks():
    for roll,detail in student_record.items():
        student_record[roll]['total'] = 0
        for k,v in detail.items():
            if k == 'marks':
                student_record[roll]['total'] += functools.reduce(lambda acc,x: acc+x,v,0)//len(v)
        print('Student : {} Total marks : {}'.format(detail['name'],student_record[roll]['total']))

def sort_by_marks():
    try :
        sorted_list = sorted(student_record.items(),key = lambda x:x[1]['total'],reverse = True)
    except KeyError:
        total_marks()
        sort_by_marks()
    else: 
        for roll,details in sorted_list:
            print(roll,' : ',details['name'],details['total'])
    


while True:
    show_options()
    choice = input("Enter your choice ")
    if choice == '0':
        print("Exit")
        break
    elif choice in valid_choices:
        print(available_options[int(choice)-1])
        if choice == '3':
            show_students()

        elif choice == '1':
            print(available_options[int(choice)-1])
            count_roll += 1
            roll_no = count_roll 
            name = input("Enter student name ")
            age = input("Enter student age ") 
            marks = [int(input("Enter marks {} ".format(i+1))) for i in range(5)]
            student_record[roll_no] = {"name":name,"age":age,'marks':marks}
            print("Student record for {} is created".format(name))


        elif choice == '2':
            print(available_options[int(choice)-1])
            roll_no = int(input("Enter student roll number to be removed "))
            if not roll_no in student_record:
                print("Not found")
            details = student_record.pop(roll_no)
            # print(details)
            print(f'{details["name"]} is removed from records')


        elif choice == '4':
            print(available_options[int(choice)-1])
            total_marks()

        elif choice == '5':
            sort_by_marks()
    else:
        print("Invalid choices")
            

        
   
