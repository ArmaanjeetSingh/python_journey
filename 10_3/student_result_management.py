students = {
    101: {"name": "Rahul", "marks": {"math": 78, "python": 85, "dbms": 70}},
    102: {"name": "Aman", "marks": {"math": 88, "python": 90, "dbms": 80}},
    103: {"name": "Simran", "marks": {"math": 92, "python": 87, "dbms": 84}}
}

def print_all_students()->None:
    for roll_no,details in students.items():
        for key,val in details.items():
            if key == "name":
                print(f"{roll_no} : {val}")
            else:
                for sub,mark in val.items():
                    print(sub,'=',mark)
        print()

def total_marks()->None:
    for roll_no,details in students.items():
        for key,val in details.items():
            if key == "name":
                print(f"{roll_no} : {val}")
            else:
                total_marks = sum([i for i in val.values()])
                print("Total marks = ",total_marks)


def find_topper() -> None:
    highest_total = 0
    topper = ""

    for details in students.values():
        total = sum(details["marks"].values())

        if total > highest_total:
            highest_total = total
            topper = details["name"]

    print("Topper:", topper)
    print("Marks:", highest_total)




# print_all_students()
# total_marks()
find_topper()