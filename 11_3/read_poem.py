# jabber = open("jabberwocky.txt")
# print(jabber)

# for line in jabber:
#     # print(line,end='')
#     print(line.strip())
#     # print(len(line))

# jabber.close()


#Avoids resource leaks and makes code robust
with open('Jabberwocky.txt','r') as jabber:
    # for line in jabber:
    #     print(line.rstrip())
    lines = jabber.readlines()
print(lines)
print(lines[-1:])
for line in reversed(lines):
    print(line,end=' ')#do processing in reversed order