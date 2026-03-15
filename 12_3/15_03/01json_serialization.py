import json

with open(r"D:\denama\python\12_3\temperature_anomaly.json","r") as file:
    data = json.load(file)
print(type(data))
print(data.keys())
print()

#Accessing metadata information
print(data["description"]["title"])
print(data["description"]["units"])
print(data["description"]["base_period"])
print()


#Access Temperature Data
temp_data = data["data"]
print(temp_data["2008"])
print(temp_data["2012"])

#Convert Values to Float
for year,value in temp_data.items():
    temp_data[year] = float(value)

print(temp_data["2016"])
print()


max_temp = 0
hot_year = ""
#Finding the hottest year
for year,value in temp_data.items():
    if max_temp < value:
        max_temp = value
        hot_year = year

print(hot_year," is the hottest year of all")

print(max(temp_data.items(), key=lambda item: float(item[1])))

temp_data = data["data"]

for year, temp in temp_data.items():
    temp = float(temp)

    if temp > 0.8:
        print(year, temp)



recent = {}
for year,temp in data["data"].items():
    if int(year) >= 2000:
        recent[year] = temp
with open("temp_data_after_2000.json","w") as writeFile:
    json.dump(recent,writeFile,indent=4)
