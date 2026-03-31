
data = [5,4,3,2,1]
n = len(data)
for i in range(n):
    for j in range(n-i-1):
        if data[j] > data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]

print(data)


