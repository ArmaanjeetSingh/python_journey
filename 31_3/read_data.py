import csv,json
box = {}
with open('data.txt','r',newline='') as file1:
    reader = file1.read().strip('\n\r').split()
    for fruit in reader:
        box[fruit] = box.get(fruit,0)+1
print(box)

word_dict = {}
with open('content.txt','r',newline='') as file2:
    reader = file2.readline().split()
    print(reader)
    for word in reader:
        word_dict[word] = len(word)
print(sorted(word_dict.keys(),key=lambda x:len(x),reverse=True)[:1])



with open('content.txt','r',newline='') as f1:
    reader = f1.read().strip('\n\r').split()
    print(reader)


with open('students.csv','r',newline='') as f2:
    reader = csv.DictReader(f2,fieldnames=['name','marks'])
    next(reader)
    max_mark = 0
    for row in reader:
        max_mark = max(max_mark,int(row['marks']))
        print(row)
    print(max_mark)

data = {"name": "armaan", "age": 20}
data_upload = []
with open('data.json','w',newline='') as f2:
    for k,v in data.items():
        data_upload.append((k,v))
    json.dump(data_upload,f2,indent=4)
     