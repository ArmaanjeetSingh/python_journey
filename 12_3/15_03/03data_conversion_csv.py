import csv

max_gold = 0
top_country = ""

with open(r"D:\denama\python\12_3\OlympicMedals_2020.csv","r",newline = '') as file:
    reader = csv.DictReader(file)
    for row in reader:
        gold = int(row["Gold"])

        if gold > max_gold:
            max_gold = gold
            top_country = row["Country"]

print(top_country,max_gold)