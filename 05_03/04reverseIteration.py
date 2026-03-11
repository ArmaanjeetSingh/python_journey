data = [104,101,4,105,308,103,5,107,100,306,106,102,108]
min_valid = 100
max_valid = 200

top_index = len(data) - 1

for index,value in enumerate(reversed(data)):
    if value < min_valid or max_valid < value:
       print(top_index - index,value)
       del data[top_index - index]
print(data)