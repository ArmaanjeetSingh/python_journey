age = int(input("How old are you ? "))

if age >= 16 and age <= 65:
    print("have a good day at work")
    
#check if number is positive, negative or zero
num = int(input("Enter any number"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")
    
#check if number is even or odd
num = int(input("Enter any number"))
if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")

#Find the largest among two numbers
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
if num1 > num2:
    print("{0} is greatest".format(num1))
elif num2 > num1:
    print("{0} is greatest".format(num2))
else:
    print("Both are equal")
    
#grade calculator
score = float(input("Enter your grade"))
if score >= 90:
    grade = "A"
elif score >= 75 and score < 90:
    grade = "B"
elif score >= 50 and score < 75:
    grade = "C"
elif score >= 35 and score < 50:
    grade = "D"
else :
    grade = "Fail"
print(grade)

#simple calculator
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
op = input("Enter operator")
if op == "+":
    print("Sum : ",num1 + num2)
elif op == "*":
    print("product : ",num1 * num2)
elif op == "-":
    print("difference : ",num1 - num2)
elif op == "/":
    print("Division : ",num1/num2)
else:
    print("invalid operator")