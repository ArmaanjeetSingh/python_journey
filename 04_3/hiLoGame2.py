import random
lowest = 1
highest = 100

answer = random.randint(lowest,highest)
print("Please guesss a number between {} and {}".format(lowest,highest))

guess = 0
while guess != answer :
    guess =int(input("Enter your guess : "))
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done! You guessed it correctly.")