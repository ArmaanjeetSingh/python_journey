import random

def get_integer(prompt):
    """
    The `get_integer` function prompts the user for input, validates that it is a numeric value, and
    returns it as an integer.
    
    :param prompt: The `get_integer` function takes a `prompt` parameter, which is a string that will be
    displayed to the user when input is required. 
    :return: The `get_integer` function is returning the user input as an integer after converting it
    from a string.
    """
    
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            # The line `return int(temp)` in the `get_integer` function is converting the user input,
            # which is a string, into an integer before returning it. This ensures that the function
            # returns an integer value that can be used for comparisons or calculations in the rest of
            # the program.
            return int(temp)
        else:
            print("Please enter a valid number")
        
        
highest = 1000
answer = random.randint(1,highest)
print(answer)

guess = 0
print("Please guess a number between 1 and {}".format(highest))

# The code snippet you provided is implementing a number guessing game in Python.
# The `while guess != answer:` line in the code snippet is setting up a while loop that will continue
# to run as long as the variable `guess` is not equal to the variable `answer`.
while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        break
    if guess == answer:
        print("Well done guessed correctly")
        break
    else:
        if guess < answer:
            print("Enter higher guess")
        else:
            print("Enter lower guess")
# print(input.__doc__)
# print(get_integer.__doc__)

help(get_integer)