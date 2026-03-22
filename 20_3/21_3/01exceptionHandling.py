def factorial(n):
    #n! can be also defined as n * (n-1)!
    """calculate n recursively """
    if n <=1 :
        return 1
    else:
        print(n/0)
        return n * factorial(n-1)

try :
   print(factorial(1000))

except RecursionError:
    print("This program exceeded its capacity of calculation")

except ZeroDivisionError:
    print("The number can't be divide by zero")
print("Program terminated")