def fizz_buzz(x : int) -> str:
   
    if x%15== 0:
        return ("fizz buzz")
    elif x%3 == 0 :
        return("fizz")
    elif x%5 == 0:
        return('buzz')
    else:
        return str(x)
        
input("Play Fizz Buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))