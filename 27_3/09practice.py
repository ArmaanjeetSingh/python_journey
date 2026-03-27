import csv,json
with open ('sample.txt','r',newline='') as outputFile, open('write.txt','w',newline= '') as inputFile:
    reader = outputFile.read()
    print(len(reader))
    print(reader)
    # writer = inputFile.write(reader.upper())
data = []
with open('student.csv','r',newline='') as file,open('student.json','w',newline='') as file2:
    reader = csv.DictReader(file)
    print(reader)
    for line in reader:
        print(line['name'],line['age'])
        data.append({
            "name": line['name'],
            "age": int(line['age']),
            "marks": int(line['marks'])
        })

    json.dump(data, file2, indent=4)