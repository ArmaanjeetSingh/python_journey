import json,csv
with open(r"D:\denama\python\27_3\28_3\temp_data_after_2000.json",'r',newline='') as temp_file, open(f'data.csv','w',newline='') as data:
    reader = json.load(temp_file)
    writer = csv.DictWriter(data,fieldnames=['year','temp'])
    writer.writeheader()

    for year,temp in reader.items():
        writer.writerow({
            'year':year,
            'temp':temp
        })