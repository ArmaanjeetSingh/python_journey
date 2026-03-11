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

shopping_list = {}
def my_deepcopy(d:dict)->dict:
    new_dict = {}
    for key,value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict
    
def add_shopping_item(data:dict, item:str, amount:str)->None:
    """Add tuple containing `item` and `amount to `data dict`

    Args:
        data (dict): 
        item (str): _description_
        amount (str): _description_

    """
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item,0) + amount


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
                add_shopping_item(shopping_list,item,quantity_to_buy)

for things in shopping_list.items():
    print(things)

potatoes = pantry.setdefault("potatoes",0)
print(f" potato : {potatoes}")

chicken = pantry.setdefault("chicken",0)
print(f"chicken : {chicken}")

ketchup = pantry.get("ketchup",0)
print(ketchup)


for key,value in sorted(pantry.items()):
    print(key,value)