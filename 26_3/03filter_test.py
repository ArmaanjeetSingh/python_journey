import timeit
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

def for_meals():
    for meal in menu:
        if "spam" not in meal:
            return meal

def comp_meals():
    meals = [meal for meal in menu if not_spam in meal]
    return meals

def not_spam(meal_list:list):
    return "spam" not in meal_list

def filter_spam():
    spamless_meals = list(filter(not_spam,menu))
    return spamless_meals

if __name__ == '__main__':
    print(filter_spam())
    print(comp_meals())
    print(for_meals())
    print(timeit.timeit(comp_meals,number=100000))
    print(timeit.timeit(filter_spam,number=100000))
    print(timeit.timeit(for_meals,number=100000))