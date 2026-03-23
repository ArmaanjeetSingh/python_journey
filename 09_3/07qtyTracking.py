from contents import pantry

recipes = {
    "omelette": {
        "eggs": 2,
        "salt": 1,
        "butter": 1
    },

    "egg sandwich": {
        "bread": 2,
        "eggs": 1,
        "butter": 1
    },

    "fried rice": {
        "rice": 2,
        "oil": 1,
        "onions": 1,
        "salt": 1
    },

    "mashed potatoes": {
        "potatoes": 3,
        "butter": 1,
        "salt": 1,
        "vinegar": 1
    },

    "tomato soup": {
        "tomatoes": 3,
        "salt": 1,
        "butter": 1
    },

    "garlic bread": {
        "bread": 2,
        "butter": 1,
        "garlic": 2,
        "sauce": 1
    },

    "tea": {
        "milk": 1,
        "tea": 1,
        "sugar": 1
    },

    "coffee": {
        "milk": 1,
        "coffee": 1,
        "sugar": 1
    }
}

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
        for item,required_qty in ingredients.items():
            quantity_in_pantry = pantry.get(item,0)
            if required_qty <= quantity_in_pantry:
                print(f"\t{item} is available in pantry")
            else:
                quantity_to_buy = required_qty - quantity_in_pantry
                print(f"\tYou don't have necessary ingredient {item}")
