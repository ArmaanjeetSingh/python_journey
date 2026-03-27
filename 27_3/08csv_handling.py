import csv,json
with open('cereal_grains.csv','r',newline='') as cereals_file, open("test.json","w",encoding='utf-8') as testfile:
    reader = csv.reader(cereals_file)
    testfile.write('[')
    for row in reader:
        json_string = json.dumps(row)
       
        print(json_string+',',file=testfile)
    testfile.write(']')