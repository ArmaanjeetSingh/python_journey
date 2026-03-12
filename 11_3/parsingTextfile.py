input_filename = 'country_info.txt'

countries = {}

with open(input_filename) as country_file:
    for row in country_file:
        # data = row.split('|')
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        country_dict = {
            'name':country,
            'capital':capital,
            'country_code':code,
            'cc3':code3,
            'dialing_code':dialing,
            'timezone':timezone,
            'currency':currency
        }
        print(country_dict)
        countries[country.casefold()] = country_dict
print(countries)