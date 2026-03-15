import csv

max_protein = 0
best_cereal = ""

with open(r"D:\denama\python\12_3\cereal_grains.csv","r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        print(row)
        cereal = row[0]
        protein = float(row[3])
    if protein > max_protein:
            max_protein = protein
            best_cereal = cereal

print(best_cereal, max_protein)