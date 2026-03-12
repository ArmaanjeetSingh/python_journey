import csv

cereals_filename = 'cereal_grains.csv'
with open(cereals_filename, encoding='utf-8',newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)

countries = {}
input_filename = r"D:\denama\python\11_3\country_info.txt"
with open(input_filename,'r',encoding='utf-8',newline='') as country_data:
    dict_reader = csv.DictReader(country_data,delimiter='|')
    
    for row in dict_reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row


while True:
    chosen_country = input("Please enter the name of your country")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['Capital']}")
    elif chosen_country == 'exit':
        break