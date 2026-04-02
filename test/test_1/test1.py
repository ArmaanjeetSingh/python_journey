# myName = 'My name is armaan'
# print(len(myName.split()))
# print(len(myName.replace(' ','')))
# count = 0
# for i in myName:
#     if type(i) == 'char':
#         count += 1
# print(count)

# list_char = myName.split()
# list_length = [len(i) for i in list_char]
# print(sum(list_length))

n = int(input("Enter your number"))
flag = 0
for i in range(2,int(n**0.5)):
    if  n % i == 0:
        flag =1
if not flag:
    print('Prime number')
else:
    print('composite')