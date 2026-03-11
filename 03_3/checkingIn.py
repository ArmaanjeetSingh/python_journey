parrot = "Norwegian Blue"

letter = input("Enter a character : ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("I don't need that letter")
    
activity = input("What would you like to do today")
if "cinema" not in activity.casefold():
    print("But I want to go to cinema")
    
    
    
#challenge practice
name = input("Enter your name")
age = int(input("Enter your age"))
if 18 <= age < 31:
    print(f"Hey {name} you can go on holiday")
else:
    print("Sorry no vacation")
    