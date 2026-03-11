orders = [
    [101, "Rahul", [["Burger",2], ["Fries",1]]],
    [102, "Aman", [["Pizza",1], ["Coke",2]]],
    [103, "Simran", [["Burger",2], ["Coke",2]]],
    [104, "Deepak", [["Pizza",1], ["Fries",1]]],
    [105, "Harry", [["Burger",2], ["Pizza",2]]]
]

available_choices = [
    "Add new order",
    "View all orders",
    "Search order by ID",
    "Add item to existing order",
    "Remove item from order",
    "Exit"
]

valid_choices = [str(i+1) for i in range(len(available_choices))]

while True:

    for index, choice in enumerate(available_choices, start=1):
        print(f"{index}. {choice}")

    user_choice = input("Enter your choice: ")

    if user_choice not in valid_choices:
        print("Invalid choice")
        continue

    if user_choice == "1":
        items = []

        for i in range(num_items):
            item = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            items.append([item, qty])

        orders.append([order_id, customer_name, items])



    elif user_choice == "2":
        print("View all orders selected")
        for order_id,name,items in orders:
            print(f"Order ID: {order_id}")
            print(f"Customer : {name}")
            print("Items")
            for item,qty in items :
                print(f"{item} - {qty}")
                print(f"{item} - {qty}")

            print("*"*40)

    elif user_choice == "3":
        print("Search order by ID selected")
        order_id = int(input("Enter order ID for details"))
        found = 0
        for order_id, name, items in orders:
            print(f"Order ID: {order_id}")
            print(f"Customer: {name}")
            print("Items")

            for item, qty in items:
                print(f"{item} - {qty}")

            print("*"*40)
        if not found:
            print("Invalid choice")



    elif user_choice == "4":
        print("Add item to existing order selected")
        o_id = input("Enter Order ID")
        item_name = input("Enter Item Name")
        qty = int(input(("Enter Quantity")))
        for order_id,name,items in orders:
            if o_id == order_id:
                items.append([item_name,qty])
            

    elif user_choice == "5":
        print("Remove item from order selected")
        order_id = int(input("Enter order ID for details "))
        item_name = input("Enter item name ")
        for o_id,name,items_list in orders:
            if o_id == order_id:
               for item in items_list:
                   if item_name.casefold() == item[0].casefold():
                      items_list.remove(item)
                      print("Item removed")
                      break
        

    elif user_choice == "6":
        print("Exiting program")
        break