 
def calculate_area(length:float)->float:
    return length*length



if __name__ == '__main__':
    area = calculate_area(30)
    print(f'The area is {area}')

#if you import a module , entire module is executed
    print('GLobal namespace')
    namespace = globals().copy()
    for name,obj in namespace.items():
        print(name,obj)

    print(f'in 10_namespaces.py, __name__ is {__name__}')