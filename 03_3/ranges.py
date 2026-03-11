for i in range(10,0,-2):
    print("i is now {}".format(i))
    
age = int(input("How old you are"))
if age in range(16,66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")
    
# Write a program to print out all the numbers from 0 to 100 that are divisible by 7.
for i in range(0,99):
    if i % 7 == 0:
        print(i)