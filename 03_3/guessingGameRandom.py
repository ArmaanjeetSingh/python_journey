import random
highest = 10
answer = random.randint(1,highest)
print(answer)

print("please guess number between 1 an {}".format(highest))
guess = int(input())

# if guess == answer:
#     print("Hurray you guessed it first time")
# else:
#     if guess < answer:
#         print("please guess higher")
#     else:
#         print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else :
#         print("Sorry wrong guess")
count = 1        
while guess != answer:
    if guess == answer:
       print("Hurray you guessed it first time")
    else:
        if guess < answer:
            print("please guess higher")
        elif guess > answer:
            print("please guess lower")
        guess = int(input())
    count += 1
print("you got right in {}".format(count))