import copy
lion_list = ["scary","big","cat"]
elephant_list = ["big","grey","wrinkled"]
teddy_list = ["cuddly","suffered"]
animals = {
    "lion":lion_list,
    "elephant":elephant_list,
    "teddy":teddy_list
}

#Perform a shallow copy
#things = animals.copy()

#Perform a deep copy
things = copy.deepcopy(animals)



# things = animals.copy()#shallow copy
# things = {
#     "lion":lion_list,
#     "elephant":elephant_list,
#     "teddy":teddy_list 
# }
# animals["teddy"] = "toy"

print(id(things["teddy"]))
print(id(animals["teddy"]))

print()
teddy_list.append("toy")
# things["teddy"].append("toy")
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via `things`")
print(id(things["teddy"]))
print(id(animals["teddy"]))
print(id(teddy_list))