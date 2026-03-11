# numbers = {*""}
# numbers={*{}}
numbers = set()
print(numbers,type(numbers))

# numbers.add(1)
# print(numbers)

while len(numbers) < 4:
    next_value = int(input("Please enter your next value"))
    numbers.add(next_value)
print(numbers)

#create a set from list to remove duplicates
data = ["blue","red","green","red",'blue',"white","green"]
unique_data = set(data)
print(unique_data)


#create a list of unique colors, keeping the other they appeared
unique_data = list(dict.fromkeys(data))
print(unique_data)