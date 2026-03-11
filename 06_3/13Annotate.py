def is_palindrome(string : str)->bool:
    """palindrome check for string

    Args:
        string (str): _description_

    Returns:
        bool: _description_
    """    
    return string[::-1].casefold()==string.casefold()

def is_palindrom_sentence(sentenc: str) -> bool:
    """is_palindrom_sentence

    Args:
        sentence (_type_): string input sentence

    Returns:
        _type_:Bool result for palindrome check
    """    
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


def fibonacci(n:int)->int:
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


sentence = input("Please enter a word to check: ")
if is_palindrom_sentence(sentence):
    print("{} is a palindrome".format(sentence))
else:
    print("{} is not a palindrome".format(sentence))
