empty_list = []
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

digits = sorted("43289671")
print(digits)

digits = list("43289671")
print(digits)

more_numbers = list(numbers)
print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)
print(id(numbers))
print(id(more_numbers))


more_nums = numbers[:]
print(more_numbers)


more_num = numbers.copy()
print(more_numbers)