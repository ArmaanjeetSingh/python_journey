answer = 5
print("please guess a betwwen 1 and 10 : ")
guess = int(input())

if guess < answer:
    print("please guess higher")
elif guess > answer:
    print("please guess lower")
else:
    print("You go it first time")
    
#string comparison
tree1 = 'Mango'
tree2 = 'Banana'

if tree1 == tree2:
    print("The trees are the same")
else:
    print("The trees are different")
    
    
if guess < answer:
    print("please guess higher")
    guess = int(input())
    if guess ==  answer:
        print("Well done, you guessed it")
    else:
        print("incorrect guess")
elif guess > answer:
    print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done you guessed it")
    else:
        print("incorrect guess")
else:
    print("You go it first time")