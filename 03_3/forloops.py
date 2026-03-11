parrot = "Norwegian blue"

for character in parrot:
    print(character)
    
number = "9,223;372:036 854,775;807"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
        
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

number = input("Please enter a series of no.s, using separators you like")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
        
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])


string = "Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?"
capital = ""
for char in string:
    if char.isupper():
        capital += char
print(capital)


for i in range(20):
    print("i is now {}".format(i))
    
for i in range(1, 21):
    print("{}".format(i))