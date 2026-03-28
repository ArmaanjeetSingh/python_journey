import random
def print_name(name,count):
    for _ in range(count):
        print(name)
def print_rand_list():
    num_list = []
    for _ in range(5):
        nums = random.randint(1,5)
        num_list.append(nums)
    return num_list

for i in range(5):
    for j in range(i):
        print("*",end='')
    print()
# print_name('Armaan',5)