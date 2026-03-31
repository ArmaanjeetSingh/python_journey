import json, csv

with open('medals.json', 'r') as medals_json, open('medals1.csv', 'w', newline='') as medals_csv:

    reader = json.load(medals_json)

    writer = csv.DictWriter(
        medals_csv,
        fieldnames=['Rank', 'Country', 'Gold', 'Silver', 'Bronze', 'Total']
    )
    
    writer.writeheader()

    for row in reader:
        print(row['Rank'], row['Country'])
        writer.writerow(row)   