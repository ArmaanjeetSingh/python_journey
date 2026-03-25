menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)

#     else:
#         meals.append("a meal was skipped")
# print(meals)

# meals = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
# print(meals)

# x = 15
# expression = "Twelve" if x==13 else"unknow"
# print(expression)

items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)
print()


for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal,item))
            break


for x in range(1,31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5== 0 else str(x)
    print(fizzbuzz)