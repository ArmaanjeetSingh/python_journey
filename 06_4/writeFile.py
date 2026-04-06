import json,csv

data = [{"name": "Aman", "age": 21},{"name":"Rahul","age":25}]

with open("data.json", "w") as f:
    json.dump(data, f)

data = {"x": None, "y": True}
print(json.dumps(data))

with open("data.json",'r') as f,open("data.csv","w",newline='') as f1:
    data = json.load(f)
    print(data)
    writer = csv.DictWriter(f1,fieldnames=["name","age"])
    writer.writeheader()
    writer.writerows(data)

data_csv = {}
with open("data.csv","r") as f:
    data = csv.DictReader(f)
    print(data)
    for row in data:
        name,age = row.values()
        data_csv['name'] = name
        data_csv['age'] = age
    print(data_csv)

data_list = []
with open('data.csv','r') as f,open('data.json','w',newline='') as f2:
    data = csv.reader(f)
    for row in data:
        print(row)
        data_list.append(row)
    json.dump(data_list,f2,indent=4)
