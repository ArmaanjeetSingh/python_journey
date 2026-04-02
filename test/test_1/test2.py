def fact(x:int):
    if x  == 0 or x == 1:
        return 1
    return x * fact(x-1)

user_ip = int(input("Enter your number "))
result = fact(user_ip)
print('Your result is ',result)