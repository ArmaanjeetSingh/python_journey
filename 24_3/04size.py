import sys

def my_range(n:int):
    start=0
    while start < n:
        print("my range is returning {}".format(start))
        yield start
        start+=1

big_range = my_range(5)

print("big range is {} bytes".format(sys.getsizeof(big_range)))

#create a list containing all values in big_range

big_list = []
for val in big_range:
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)