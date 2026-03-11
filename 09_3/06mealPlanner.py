from contents import pantry,recipes

# display_dict = {str(index+1) for index,meal in enumerate(recipes)}
display_dict = {}

for index,recipe_name in enumerate(recipes,start=1):
        # print(f"{index} - {recipe_name}")
        display_dict[str(index)] = recipe_name

while True:
    print("Please choose your recipe")
    print("-"*40)
    for key,value in display_dict.items():
        print(f"{key} - {value}")

   
    current_choice = input("Enter your choice ")
    if current_choice == '0':
        break

    elif current_choice in display_dict:
        selected_item = display_dict[current_choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients...")
        ingredients = recipes[selected_item]
        for item in ingredients:
            if item in pantry:
                print(f"\t{item} is available in pantry")
            else:
                print(f"\tYou don't have necessary ingredient {item}")
