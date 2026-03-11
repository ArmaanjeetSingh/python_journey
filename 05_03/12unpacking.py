a = b = c= d = e =f = 42
print(e)

x, y, z = 1,2,76
print(x)
print(y)
print(z)

print("Unpacking a tuple")
data = 1,2,76
x,y,z = data #python tuple can be unpacked and unmutable and can't crash
print(x)
print(y)
print(z)

print("unpacking a list")
data_list = [12,13,14,15]
# data_list.append(16) value error as it is mutable
p,q,r,t = data_list
print(p,q,r,t)


for t in 