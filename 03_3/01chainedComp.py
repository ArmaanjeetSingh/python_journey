#1. Write a program to check whether a number is between 10 and 50 (inclusive) using chained comparison.
number = int(input("Enter any  number"))
if 10 <= number < 50:
    print("{} exists between 10 and 50".format(number))
else:
    print("Out of range")
    
# Take three numbers from the user and check if the second number lies between the first and third numbers.
num1 = int(input("Enter number for starting of range"))
num2 = int(input("Enter number for ending of range"))
num3 = int(input("Enter number for exisitng check for given range"))
if num1 <= num3 < num2:
    print("{2} exists between {0} and {1}".format(num1,num2,num3))
else:
    print("Out of range")
    
    
#2. Check whether a year is between 1900 and 2100.
yr1 = int(input("Enter any year value"))
if 1900 <= yr1 < 2100:
    print(f"{yr1} exists between 1900 and 2100")
    if(yr1 % 4 == 0):
        print(f"{yr1} is also a leap year")
else :
    if(yr1 % 4 == 0):
        print(f"{yr1} is also a leap year")
    else:
        print("out of range and not leap")
 
#3. A number is divisible by 3 AND 5.
num = int(input("Enter number for divisbilty check"))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} divisble by both 3 and 5")
elif num % 3 == 0:
    print(f"{num} divisble by 3")
elif num % 5 == 0:
    print(f"{num} divisble by 5")
else:
    print("not divisible")
    
#4. Check if a number is positive AND even.
num = int(input("Enter number for check"))
if num >0 and num %2 == 0:
    print("{} is positive and even".format(num))
else:
    print("Condition not fulfilled")
    
#5.Check whether a substring exists inside a string.
text = "i am learning python programming language"
substring = "Python"
if substring.casefold() in text.casefold():
    print("Substring exists in case insensitive")
    
