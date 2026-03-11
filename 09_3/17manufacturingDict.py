from parts import materials,products
purchase_list = {}
valid_products = {str(index):val for index,val in enumerate(products,start=1)}

while True:
    for choice,val in valid_products.items():
        print(f"{choice} - {val}")
    print("0 - exit")
    
    user_choice = input("Enter product index to manufacture ")

    if user_choice in valid_products:
        selected_product = valid_products[user_choice]
        manufac_parts = products[selected_product]

        for material,qty in manufac_parts.items():
            available = materials.get(material, 0)
            if available >=qty :
                materials[material] -= qty
                print(material,' =',available)
            else:
                print(material,'need to purchase')
                missing = qty - available
                purchase_list[material] = purchase_list.get(material,0) + missing


    if choice == '0':
        break

    else:
        print("Invalid choice")

for item, qty in purchase_list.items():
    print(item, qty)