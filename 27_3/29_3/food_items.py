ingredients = {
    "milk":10,
    "flour":5,
    "corn":12,
    "spices":15,
    "butter":34,
    "curd":12,
    "ghee":8,
    "ilachi":6,
    "water":18
}

recipe = {
    "tea":[("water",2),("milk",5),("ilachi",3)],
    "curry":[("curd",2),("spices",4),("ghee",4)],
    "roti":[("water",10),("flour",16)]
}
cooked_dishes = {}
available_choices = ['Cook dish','Add new dish','Show Recipe']
valid_choices = [str(i+1) for i in range(len(available_choices))]

def show_recipe():
    for item,detail in recipe.items():
        print("item : {}".format(item.upper()),end= ' ')
        for ingredient,qty in detail:
            print(f"{ingredient} : {qty}",end=' ')
        print()

def show_options():
    for index,val in enumerate(available_choices,start=1):
        print(index,' - ',val)
    print('0 -  Exit')

def check_for_ing(item,qty):
    flag = True
    if not item.casefold() in ingredients:
        flag = False
        print("Item {} is not present".format(item.upper()))
        return flag
    if not qty < ingredients[item.casefold()]:
        flag = False
        print("Out of stock,.. Insufficient quantity for {}".format(item))
        return flag
    return flag 

def use_ingredient(item,qty):
    ingredients[item] -= qty
    print('Ingridient {} is used from stock and remaining quantity {}'.format(item,ingredients[item]))


while True:
    show_options()
    choice = input("Enter your choice ")
    if choice == '0':
        print('Exit')
        break

    elif choice in valid_choices:
        if choice == '3':
            show_recipe()

        if choice == '1':
            print(available_choices[int(choice)-1])
            for index,key in enumerate(recipe,start=1):
                print(index,' : ',key.capitalize())
            current_choice = input("Enter your item to cook ")
            for item,val in recipe.items():
                if item.casefold() == current_choice.casefold():
                    print(f'{item} will be cooked... checking for stock of ingredients')
                    for it,qty in val:
                        print(f'{it} : {qty}')
                        flag = check_for_ing(it,qty)
                    if not flag:
                        print("Insufficient stock")
                    else:
                        for it,qty in val:
                            use_ingredient(it,qty)
                        print("You dish {} will be served".format(item))

        
        if choice == '2':
            print(available_choices[int(choice)-1])
            current_choice = input("Enter the item you want to add")
            recipe[current_choice] = {}
            print("Enter its recipe ")
            no_of_ingrdients = int(input("Enter number of ingredients"))
            for i in range(no_of_ingrdients):
                item = input("Enter ingredient name ")
                qty  = int(input("Enter required quantity "))
                flag = check_for_ing(item,qty)
                if not flag:
                    print("Cann't add this dish")
                recipe[current_choice] = {(item,qty)}



