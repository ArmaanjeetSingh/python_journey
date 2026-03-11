from vehicles import vehicles
print(vehicles)

del vehicles["creta"]
# del vehicles["f1"] key error
result = vehicles.pop("f1","None")
print(result)


result2 = vehicles.pop("city","not present")
print(result2)
print()

for key,value in vehicles.items():
    print(key,value)