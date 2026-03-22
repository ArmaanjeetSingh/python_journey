courses = [
   ["Python", [["Python Basics", 2000], ["Advanced Python", 3500]]],
   ["Web Development", [["HTML & CSS", 1500], ["JavaScript", 2500]]],
   ["Data Science", [["Machine Learning", 4000], ["Data Analysis", 3000]]]
]

purchased_courses = []

available_options = ["View Categories",
        "View Courses in Category",
        "Buy Course",
        "Search Course",
        "Show Purchased Courses"]

while True:
    for index,option in enumerate(available_options,start=1):
        print(f'{index} :{option}')

    print("0 : Exit")

    current_choice = int(input("Enter your choice from above list "))

    if current_choice == 0:
        print("Exit")
        break


    if 1 <= (current_choice) <= len(available_options):
        if current_choice == 1:
            for index, (category,category_list) in enumerate(courses,start=1):
                print(f'{index} : {category}')

        elif current_choice == 2:
            for index, (category,category_list) in enumerate(courses,start=1):
                print(f'{index} : {category}')

            category_choice = int(input("Enter your category choice "))
            category_choice -= 1

            if 0 <= category_choice <= len(courses):
                for course,price in courses[category_choice][1]:
                    print(f'{course}:{price}')


        elif current_choice == 3:
            for index, (category,category_list) in enumerate(courses,start=1):
                print(f'{index} : {category}')


            category_choice = int(input("Enter your category choice "))
            category_choice -= 1

            if 0 <= category_choice <= len(courses):
                for course,price in courses[category_choice][1]:
                    print(f'{course}:{price}')

            course_index = int(input("Enter your course choice "))
            course_index -= 1

            if 0 <= course_index <= len(courses[category_choice][1]):
                purchased_courses.append(courses[category_choice][1][course_index])
                course_name,price = courses[category_choice][1][course_index]
                print(f'{course_name} added to courses')
