name = input("please enter your name")
age = int(input("How old are you, {0} ?".format(name)))
print(age)

if age >= 18:
    print("You are eligible for voting")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18-age))
    
if age < 18:
    print("Please come back in {0} years".format(18-age))
else:
    print("You are eligible for voting")
    print("Please put an X in the box")


if age < 18:
    print("Please come back in {0} years".format(18-age))
elif age > 125:
    print("invalid age")
else:
    print("You are eligible for voting")
    print("Please put an X in the box")