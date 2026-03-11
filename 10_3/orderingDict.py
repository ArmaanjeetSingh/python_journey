menu = {
    "Burgers": {
        "Veg Burger": 120,
        "Chicken Burger": 180
    },
    "Pizza": {
        "Margherita": 250,
        "Farmhouse": 350
    },
    "Drinks": {
        "Coke": 50,
        "Cold Coffee": 120
    }
}

available_options = [
    "Show categories",
    "Show items in category",
    "Add item to cart",
    "View cart",
    "Remove item from cart",
    "Checkout",
    "Exit"
]
cart = {}

while True:
    for index,value in enumerate(available_options,start=1):
        print(f"{index} : {value}")
    
    current_choice = input("Enter your choice ")
    if current_choice.isdigit():
        choice = int(current_choice)
        if 1<= choice <= len(available_options):
            print("You chose {}".format(available_options[choice-1]))


            if choice == 1:
                for category in menu:
                    print(category)

            elif choice == 2:
                categories = list(menu.keys())

                for index,category in enumerate(menu.keys(),start=1):
                    print(f"{index} - {category}")

                category_choice = int(input("Enter category choice "))
                if 1<=category_choice <=len(menu):
                    selected_category = categories[category_choice-1]

                    print("You selected {}".format(selected_category))

                    for item,price in menu[selected_category].items():
                        print(item," : ",price)
                else:
                    print("Invalid category choice")

            elif choice == 3:
                print("Add item to cart")
                categories = list(menu.keys())

                for index,category in enumerate(menu.keys(),start=1):
                    print(f"{index} - {category}")

                category_choice = int(input("Enter category choice "))

                if 1<=category_choice <=len(menu):
                    selected_category = categories[category_choice-1]

                    print("You selected {}".format(selected_category))

                    items = list(menu[selected_category].keys())
                    for item,price in menu[selected_category].items():
                        print(item," : ",price)

                    item_choice = int(input("Enter item choice for cart "))
                    if 1<=item_choice<=len(items):
                        selected_item = items[item_choice-1]
                        print("You selected ",selected_item,'with price',menu[selected_category][selected_item])

                        cart.setdefault(selected_item,0)
                        cart[selected_item] += 1
                        print("Added to cart....")


            elif choice == 4:
                print("View your cart for purchases")
                total_bill = 0
                for item,price in cart.items():
                    total_bill += price
                    print(f"{item} = {price}")

                print("Payment amount : ",total_bill)

            elif choice == 5:
                for index,(item,price) in enumerate(cart.items(),start=1):
                    print(f"{index}. {item} = {price}")
                items = [i for i in cart.keys()]

                remove_choice = int(input("Enter your remove choice "))
                if 1<= remove_choice<=len(items):
                    remove_item = items[remove_choice-1]

                    cart.pop(remove_item)
                    print(remove_item,"is removed from cart")



            elif choice == 7:
                break

        else:
            print("Invalid option")