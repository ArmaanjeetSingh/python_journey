
# data = [104,105,12,130,130,150,160,170,183,185,187,188,191] no outlying values
# data = [4,5,104,105,12,130,130,150,160,170,183,185,187,188,191] lower putlying values
# data = [104,105,12,130,130,150,160,170,183,185,187,188,191,350,360] higher outlying values
data = []
min_valid = 100
max_valid = 200

#process the low values in list
stop = 0
for index,value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
    
print(stop)
del data[:stop]
print(data)


#process the high values in the list
start = 0
for index in range(len(data)-1,-1,-1):
    if data[index] <= max_valid:
        #We have index of last item to keep
        start = index + 1
        break
print(start)
del data[start:]
print(data)
