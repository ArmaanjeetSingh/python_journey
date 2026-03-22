import sys
def getint():
    while True:
        try :
            number = int(input("Please enter a number "))

        except EOFError:
            sys.exit(0)

        except ValueError:
            print("Invalid number entered, please try again")

        finally:
            print("Always executes")

first_num = getint()
second_num = getint()
try :
    print("{} divided by {} is {}".format(first_num,second_num,first_num/second_num))

except ZeroDivisionError:
    print("Can't divide by zero")

else:
    print("Division performed successfully")