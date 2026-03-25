def fibonacci():
    current,previous = 0,1
    while True:
        yield current
        current, previous = current + previous, current


# fib = fibonacci()
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

# for f in fib:
#     print(f)

def print_odd():
    i = 1
    while True:
        yield i
        i += 2

def pi_series():
    odds = print_odd()
    approximation = 0
    while True:
        approximation += (4/next(odds))
        yield approximation
        approximation -= (4/next(odds))
        yield approximation

approx_pi = pi_series()
for x in range(1000000):
    print(next(approx_pi))
