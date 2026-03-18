def greet_pythons(items:list)->None:
    greeting = 'hello'#free variable
    print(f'The ID of `greeting` in greet_pythons is {id(greeting)}')

    def make_greetings(item:str)->str:
        # greeting = 'Hi' #biding to inner scope
        print(f'The ID of `greeting` in make_greeting is {id(greeting)}')
        return f'{greeting} {item}'
       
    for item in items:
        print(make_greetings(item))
        # print(locals())
    greeting = 'hello'#free variable
    print(f'The ID of `greeting` in greet_pythons is {id(greeting)}')

# names = ['John','Eric','Terry','Michael']
names = ['John']
greet_pythons(names)
print(dir())

#local : geeting, item --> make_greetings
#enclosing : local : greeting,item,items,make_greeting
#global : greet_python,names