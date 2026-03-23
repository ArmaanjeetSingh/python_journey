# def average(f_value,*args,last_value):
#     mean = 0
#     print(type(args))
#     print("args is {}".format(args))
#     print("*args is ",*args)
#     for arg in args:
#         mean += arg
#     return mean/len(args)

# print(average(1,2,3,4,5))

# def build_tuple(*args):
#     return args
# message_tuple = build_tuple("Hello","Planet","take","earth","me","to","leader")
# print(type(message_tuple))
# print(message_tuple)

# number_tuple = build_tuple(1,2,3,4,5,6)
# print(type(number_tuple))
# print(number_tuple)

def print_backward(*args,**kwargs):
    for word in args[::-1]:
        print(word[::-1],end ='',**kwargs)

with open('backwards.txt','w') as open_file:
    print_backward("Hello","Planet","take","earth","me","to","leader",file=open_file)