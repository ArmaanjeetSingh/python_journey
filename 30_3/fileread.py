import csv,json
with open('my_cereals.csv','r',newline='') as fil1,open('my_cereals1.json','w',newline='') as file2:
    reader = csv.DictReader(fil1,fieldnames=['Cereal','Calories','Protein','Fiber','Iron','Calcium'])
    print(reader)
    next(reader)#next line
    # for row in reader:
    #     print(row)
    
    data= []
    for row in reader:
        data.append(row)
    print(data)
    json.dump(data,file2,indent=4)