# Display a menu with prices and allow users to order multiple items. Calculate the total bill with tax. 
# Use loops for ordering, dictionaries for storing menu, and conditionals for bill logic.

menu = {"Burger":20,"Pizza":45,"Coca cola":30,"Pasta":20}
ordered_items = []
while True:
    for index,val in enumerate(menu.items(),start=1):
        item,price = val
        print(f"{index} {item} : {price}")
    print("Type 'done' to finish order")

    user_item = input("Enter your food item ").casefold()
   

    if user_item == "done":
        print("-----BILL-------")
       
        if not ordered_items:
            print("no items assed to cart")
            break


        subtotal=total=0
        for item,qty,price in ordered_items:
            subtotal  += qty*price
            print(f'{item} x {qty} = {price}')

        tax = input("Enter tax type (gst/other) ").casefold()
        if tax.casefold() == "gst":
            subtotal += subtotal*0.18
        else:
            subtotal += subtotal*0.10

        if subtotal > 100:
            total = subtotal - subtotal*0.3
            print("Your disocunt is ",subtotal*0.3)

        print("You bill is ",total)

        break

    user_qty = int(input("Enter quantity for food item "))

    if user_item in menu:
        print(f"{user_item} added to order cart")
        ordered_items.append((user_item,user_qty,menu[user_item]))


    else:
        print("Invalid choice entered")
