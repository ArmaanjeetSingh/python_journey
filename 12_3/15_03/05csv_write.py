import csv

data = [
    ["Country", "Gold"],
    ["USA", 39],
    ["China", 38],
    ["Japan", 27]
]

with open("top_countries.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerows(data)