menu = [
    ("Burgers", [
        ["Veg Burger", 120],
        ["Chicken Burger", 180]
    ]),
    
    ("Pizza", [
        ["Margherita", 250],
        ["Farmhouse", 350]
    ]),
    
    ("Drinks", [
        ["Coke", 50],
        ["Cold Coffee", 120]
    ])
]
orders = []

available_options = [
    "View Food Categories",
    "View Items in Category",
    "Place Order",
    "Search Food",
    "View Bill",
    "Sort Menu by Price",
    "Exit"
]
valid_choices = [str(i+1) for i in range(len(available_options))]
orders = []

while True:
    print("="*40)
    for index,option in enumerate(available_options):
        print(f"{index+1} : {option}")
    
    current_choice = input("Enter your choice ")
    if current_choice in valid_choices:
        print(current_choice)

        if current_choice == valid_choices[0]:
            print("*"*40)
            print("Food Categories are as follows")
            for index,(catgeory_name,food_list) in enumerate(menu):
                print(f"{index+1} : {catgeory_name}")
            

        elif current_choice == valid_choices[1]:
            print("Food Categories are as follows")
            for index,(category_name,food_list) in enumerate(menu):
                print(f"{index+1} : {category_name}")

            category_choice = int(input("Enter your category choice index "))

            if 1 <= category_choice <= len(menu):
                category_name, food_list = menu[category_choice-1]

                print(f"Items in {category_name}")

                for index,(food_name,price) in enumerate(food_list,start=1):
                    print(f"{index} : {food_name} - {price}")
            else:
                print("Invalid category choice")


        elif current_choice == valid_choices[3]:
            found = 0
            print("Search food item")
            keyword = input("Enter keyword for search").casefold()
            for index,(category_name,food_list) in enumerate(menu):
                for food_name,price in food_list:
                    print(food_name)
                    if keyword in food_name.casefold():
                        print("Found at {} under category {}".format(food_name,category_name))

            if found == 0:
                print("No match found")


        elif current_choice == valid_choices[2]:
            for index,(category_name,food_list) in enumerate(menu):
                print(index+1," : ",category_name)

            order_choice = int(input("Enter choice for placing order "))
            if 1 <= order_choice <= len(menu):
                category_name,food_list = menu[order_choice-1]
                for food_name, price in food_list:
                    print(f"{food_name} : {price}")
                order_item = int(input("Enter food item for order "))
                order_item -= 1
                if 0 <= order_item <= len(food_list):
                    orders.append(food_list[order_item])
                    print(f"your order placed for {food_list[order_item][0]}")
                    

        


        
    else:
        print("Invalid choice")


