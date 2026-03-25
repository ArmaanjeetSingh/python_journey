print(__file__)
numbers = [1,2,3,4,5,6,7]
squares = []

number = int(input("Enter a number, and I'll tell you squares "))
for number in numbers:
    squares.append(number**2)

index_pos = numbers.index(number)
print(squares)
print(squares[index_pos])