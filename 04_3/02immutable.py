a = True
b = "String"
c = b
print(id(c))
print(id(a))
print(id(b))

b = False
print(id(b))

c = "Correct"
d = c
print(id(c))
print(id(d))

c += "hello"
print(id(c))