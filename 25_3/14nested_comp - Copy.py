burgers = ["beef","chicken","spicy bean"]
toppings = ["cheese","egg","beans","spam"]

for meals in [(burger,topping) for burger in burgers for topping in toppings]:#comprehensions with two iterators part
    print(meals)

for nested_meals in [[(burger,topping) for burger in burgers]for topping in toppings]:#here is comprehension , whose expression is itself a comprehension
    print(nested_meals)
print()

for nested_meals in [[(burger,topping)for topping in toppings] for burger in burgers]:
    print(nested_meals)

nested_table = [[(i,i*j)for j in range(1,11)] for i in range(1,11)]
print(nested_table)
print()

nested_table1 = [(i,i*j)for i in range(1,11) for j in range(1,11)]
print(nested_table1)
for x,y in [(i,i*j)for i in range(1,11) for j in range(1,11)]:
    print(x,y)

print()

for x in ([(i,i*j)for i in range(1,11)] for j in range(1,11)):
    print(x)

print("-"*80)
print("Nested loop")
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
 
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
for loc in sorted(locations):
    exits_to_destination_1 = []
    for xit in exits:
        if loc in exits[xit].values():
            exits_to_destination_1.append((xit,locations[xit]))
    print("Locations leading to {}".format(loc),end='\t')
    print(exits_to_destination_1)
print()

for loc in sorted(locations):
    exits_to_destination_2 = [(xit,locations[xit])for xit in exits if loc in exits[xit].values()]
    print("Locations leading to {}".format(loc),end='\t')
    print(exits_to_destination_2)

exits_to_destination_3 = [[(xit,locations[xit])for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
print(exits_to_destination_3)


print()

for index,loc in enumerate(exits_to_destination_3):
    print("Locations leading to {}".format(index),end='\t')
    print(loc)
