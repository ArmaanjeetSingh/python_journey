import csv,json
with open('my_cereals.csv','r',newline='') as file1, open('my_cereals.json','w',newline='') as file2:
    reader = csv.DictReader(file1,fieldnames=['Cereal','Calories','Protein','Fiber','Iron','Calcium'])
    next(reader) 
    data = []
    for row in reader:
        print(row)
        data.append(row)
    writer = json.dump(data,file2,indent=4)

    