input_filename = 'country_info.txt'

with open(input_filename) as country_file:
    for row in country_file:
        # data = row.split('|')
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        print(country, capital, code, code3, dialing,timezone, currency, sep='\n\t')