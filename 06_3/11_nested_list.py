menu = [
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam"],
    ["egg","spam","bacon"],
    ["spam","spam","sausage","egg"],
    ["spam","bacon","sausage","egg"],
    ["spam","bacon","sausage","egg","tomato"]
]
#print meals that have no spam at all
for items in menu:
    if "spam" not in items:
        print(items)


#Find total spam count in all meals.
count = 0
for items in menu:
    if "spam" in items:
        count += 1
print(count)


#Print the largest meal.
max_len = 0
index = 0
for i in range(len(menu)):
    if max_len < len(menu[i]):
        max_len = len(menu[i])
        index = i
    else:
        continue
print(max_len)
print(menu[i])

#Remove "spam" from every meal
for items in menu:
    items= [item for item in items if item != "spam"]
    print(items)


#Print menu with meal numbers using enumerate
for index,meal_list in enumerate(menu):
    print(f"Meal {index+1} : {meal_list}")


#Remove bacon and sausage from every meal.
non_veg = ["bacon","sausage"]
for meal in menu:
    meal = [item for item in meal if item not in non_veg]
    print(meal)

#Sort each meal alphabetically
for meal in menu:
    meal.sort(key=lambda x:x)
print(menu)

#Find meals containing BOTH egg and bacon
items = ['egg','beacon']
for meal in menu:
    if items in meal:
        print(meal)
    