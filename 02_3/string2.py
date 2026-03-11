parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])

#challenge
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print(parrot[-11])
print(parrot[-10])

#slicing
print(parrot[0:6])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])



print(parrot[-4:-2])
print(parrot[0:6:2])#Nr
print(parrot[0:6:3])#Nw


number = "9,223;372:036 854,775;807"
separators = number[1:4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])