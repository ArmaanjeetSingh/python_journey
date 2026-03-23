from parts import materials,products
purchase_list = {}

valid_products = {str(index):val for index,val in enumerate(products,start=1)}


while True:
    for choice,val in valid_products.items():
        print(choice," : ",val)
    
    user_choice = int(input("Enter product index to manufacture "))

    if user_choice == 0:
        break

    if 1<= user_choice<= len(valid_products):
        selected_product = valid_products[str(user_choice)]
        manufac_parts = products.get(selected_product)
        print(manufac_parts)

        for material,qty in manufac_parts.items():
            available = materials.get(material, 0)
            print(available)
            if available >=qty :
                materials[material] -= qty
                print(material,' =',available)
        
