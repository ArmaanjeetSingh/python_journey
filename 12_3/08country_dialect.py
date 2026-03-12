import csv

input_filename = r"D:\denama\python\11_3\country_info.txt"

with open(input_filename, encoding='utf-8',newline='') as countries_data :
    sample = countries_data.read()
    country_dialect = csv.Sniffer().sniff(sample)
    countries_data.seek(0)
    # country_reader = csv.reader(countries_data,delimiter='|')
    country_reader = csv.reader(countries_data,dialect=country_dialect)
    for row in country_reader:
        print(row)
print("*"*80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace'
            ]
for attribute in attributes:
    print(f'{attribute} :{repr(getattr(country_dialect,attribute))}')