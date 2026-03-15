import csv

# with open(r"D:\denama\python\12_3\OlympicMedals_2020.csv","r",newline = '') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row[1],row[2])

with open(r"D:\denama\python\12_3\OlympicMedals_2020.csv","r",newline = '') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

    print(row["Country"])
    print(row["Gold"])