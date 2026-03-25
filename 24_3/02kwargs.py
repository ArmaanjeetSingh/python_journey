# def print_backward(*args,**kwargs):
#     print(kwargs)
#     kwargs.pop('end',None)
#     for word in args[::-1]:
#         print(word[::-1],end ='',**kwargs)

def print_backward(*args,**kwargs):
    end_character = kwargs.pop('end','\n')
    sep_character = kwargs.pop('sep',' ')
    kwargs.pop('end',None)
    for word in args[:0:-1]:#change the range
        print(word[::-1],end =sep_character,**kwargs) #print the first word separately
    print(args[0][::-1],end=end_character,**kwargs)
    # print(end=end_character)


def backward_print(*args,**kwargs):
    sep_character = kwargs.pop('sep',' ')
    print(sep_character.join(words[::-1] for words in args[::-1]),**kwargs)


with open('backwards.txt','w') as open_file:
    print_backward("Hello","Planet","take","earth","me","to","leader",end='\n')
    print('Another string')

backward_print("Hello","Planet","take","earth","me","to","leader",end='',sep='\n**\n')
print_backward("Hello","Planet","take","earth","me","to","leader",end='\n',sep='\n**\n')