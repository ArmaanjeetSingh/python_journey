import random

low = 1
high = 1000

print("Please think a number between {} and {}".format(1,1000))
input("Press ENTER to start")

guesses = 1

while True:
    guess = low + (high - low)//2
    
    high_low = input(
        "My guess is {}. Should I guess higher or lower? "
        "Enter h or l, or c if my guess is correct: ".format(guess)
    ).casefold()
    
    if high_low == "h":
        low = guess + 1
        guesses += 1
        
    elif high_low == "l":
        high = guess - 1
        guesses += 1
        
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break