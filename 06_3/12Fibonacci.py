def fibonacci(n):
    """return the `int` fibonaci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1,n_minus2 = 1,0

    result = None
    for f in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result

    return result

def is_palindrome(string : str)->bool:
    return string[::-1].casefold()==string.casefold()

for i in range(36):
    print(i,fibonacci(i))

p = is_palindrome("hello")
print(p)