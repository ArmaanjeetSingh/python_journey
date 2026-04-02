def log_deco(func):
    def wrap(*args):
        print('Values ',args)
        result = func(*args)
        print('Result ',result)
    return wrap

def greater_first(func):
   def wrap(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)

   return wrap

@log_deco
def add(a,b):
    return a + b

@log_deco
@greater_first
def sub(a,b):
    return a-b


@log_deco
@greater_first
def divide(a,b):
    return a/b

sub = greater_first(sub)
divide = greater_first(divide)
print(sub)
result = divide(2,4)
print(result)

result2 = sub(2,4)
print(result2)


result3 = add(4,7)
print(result3)