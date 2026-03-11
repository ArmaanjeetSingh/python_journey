numbers = (0,1,2,3,4,5)

print(numbers,sep = ';')
print(*numbers,sep = ';') #unpacked values of numbers
print(0,1,2,3,4,5,sep = ';')

def test_star(*args):
    print(args)
    for x in args:
        print(x)

test_star(0,1,2,3,4)
print()
test_star()


def sum_numbers(*a:float)->float:
    sum = 0
    for i in a:
        sum += i
    return sum
print(sum_numbers(1,2,3))
print(sum_numbers(1,2,3,7.8,2.9,3.1))
