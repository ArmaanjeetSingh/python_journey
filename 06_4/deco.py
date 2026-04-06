def my_deco(func):
    def wrapper():
        print("This is wrapper for decorator")
        func()
        print("End of function")
    return wrapper

def deco_with_args(func):
    def wrapper(*args,**kwargs):
        print("Before")
        result = func(*args,**kwargs)
        print(kwargs['k'])
        print("After")
        return result
    return wrapper


@deco_with_args
def add(a,b,k=0):
    print(a+b)
add(5,3,k=2)

@my_deco
def say_hello():
    print("Hello")


def log_decorator(func):
    def wrapper(*args,**kwargs):
        print("Inputs : ",args)
        print(kwargs)
        result = func(*args,**kwargs)
        print("Output :  ",result)
        return result
    return wrapper

@log_decorator
def multiply(a,b,k):
    return a*b

print(multiply(2,3))
#func = my_deco(func)
# say_hello = my_deco(say_hello)
# say_hello()
say_hello()