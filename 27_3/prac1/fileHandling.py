import csv,json
countries = {}
max_gold = 0
max_count = ''
with open('OLympicMedals_2020.csv','r',newline='',encoding='utf-8') as temp_file:
    reader = csv.DictReader(temp_file)
    for row in reader:
       if max_gold < int(row['Gold']):
          max_gold = int(row['Gold'])
          max_count = row['Country']
    #    countries[row['Country']] = int(row['Gold'])
# print(max_gold,max_count)
# print(countries) 

with open('OlympicMedals_2020.csv','r',newline='') as medals_file:
    reader = csv.DictReader(medals_file)
    for row in reader:
        row['total'] = int(row['Gold'])+int(row['Silver'])+int(row['Bronze'])
        print(row)


with open(r"D:\denama\python\27_3\28_3\OlympicMedals_2020.csv",'r',newline='') as medals_file, open('medals.json','w',newline='') as medals:
    reader = csv.DictReader(medals_file)
    data = []
    for row in reader:
        data.append(row)
    json.dump(data, medals, indent=4)


