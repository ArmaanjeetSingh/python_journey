def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def is_palindrom_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


sentence = input("Please enter a word to check: ")
if is_palindrom_sentence(sentence):
    print("{} is a palindrome".format(sentence))
else:
    print("{} is not a palindrome".format(sentence))







# sentence = "Was it a car, or a cat, I saw?"
# print(sentence.split())
# separators = ",?|\"'!@#$%^&*()"
# l1 = [char for char in sentence if char not in separators]
# print(l1)
# j1 = ''.join(l1)
# print(j1.trim())
# print(j1[::-1].casefold()==j1.casefold())
# sentence2 = "Do geese see god"