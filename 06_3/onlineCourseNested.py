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
valid_options = [str(i) for i in range(len(available_options))]

while True :
    for index,option in enumerate(available_options,start=1):
        print(f"{index} : {option}")
    print("0 : Exit")

    current_choice = int(input("Enter your choice "))

    if current_choice == 0:
        print("Exit")
        break
    
    if 1 <= current_choice <= len(available_options):

        if current_choice == 1:
            print("Categories are as follows")
            for index,(category,courses_list) in enumerate(courses):
                print(f"{index+1} {category}")


        elif current_choice == 2:
            for index,(category,courses_list) in enumerate(courses):
                print(f"{index+1} {category}")

            category_index = int(input("Enter index for category "))
            if 1 <= category_index <= len(courses):
                print("Courses for given {}".format(courses[category_index-1][0]))
                for course_name,price in courses[category_index-1][1]:
                    print(course_name,price)
             
            else:
                print("Invalid catgeory index")

        elif current_choice==3:
            for index,(category,courses_list) in enumerate(courses):
                print(f"{index+1} {category}")

            category_index = int(input("Enter index for category "))
            if 1 <= category_index <= len(courses):
                print("Courses for given {}".format(courses[category_index-1][0]))
                for course_index,(course_name,price) in enumerate(courses[category_index-1][1]):
                    print(course_index+1,course_name,price)


                course_index = int(input("Enter course index for puchase"))
                course_index -= 1
                if 0 <= course_index <= len(courses[category_index-1][1]):
                    purchased_courses.append(courses[category_index-1][1][course_index])
                    print(f"{courses[category_index-1][1][course_index][0]} added to purchased courses")
            else:
                print("Invalid catgeory index")




        elif current_choice==5:
            print("Purchased courses")
            total_price = 0
            for course_name,price in purchased_courses:
                print(f"{course_name} : {price}")
                total_price+=price
            print("Total price : ",total_price)

        elif current_choice ==4:
            print("Search course")
            found = 0
            keyword = input("Enter your keyword ").casefold()
            for index,(category_name,course_list) in enumerate(courses):
                if keyword in category_name.casefold():
                   found = 1
                   print(f"Category {index+1} : {category_name}")
                for course_name,price in course_list:
                    if keyword in course_name.casefold():
                        found = 1
                        print(f"Course : {course_name} under {category_name}")

            if not found:
                print("No match found")
                
                

                
             
            

