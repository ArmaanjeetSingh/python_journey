import json,csv
with open('my_cereals.json','r',newline='') as file1,open('my_cereals3.csv','w',newline='') as file2:
    reader = json.load(file1)
    print(reader)
    for row in reader:
        print(row)
    writer = csv.DictWriter(file2,fieldnames=['Cereal','Calories','Protein','Fiber','Iron','Calcium'])
    writer.writeheader()#fielnames --> header of csv file

    writer.writerows(reader)
    # for row in reader:
    #     writer.writerow(row)
