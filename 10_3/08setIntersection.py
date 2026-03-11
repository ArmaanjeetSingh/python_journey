def primes_generator(limit):
    for num in range(2, limit + 1):
        is_prime = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            yield num
def squares_generator(limit):
    for num in range(1, limit + 1):
        yield num ** 2

evens = set(range(0,50,2))
odds = set(range(1,50,2))
print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odds.intersection(primes))
print(evens.intersection(squares))

#pass an iterbale to method
even_squares = evens.intersection(squares_generator(100))
print(even_squares)

#set difference
print(odds.difference(primes))
print(primes - evens)
