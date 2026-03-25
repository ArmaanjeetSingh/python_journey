numbers = [1,2,3,4,5,6,7]

squares_comp = [i**2 for i in numbers]
squares_comp_set = {i**2 for i in numbers}

square_range = [num**2 for num in range(1,7)]
print(squares_comp)
print(squares_comp_set)
print(square_range)

number = int(input("Enter a number, and I'll tell you squares "))
index_pos = numbers.index(number)
print(squares_comp)
print(squares_comp[index_pos])