input_filename = 'country_info.txt'

country_dict = {}

with open(input_filename) as file:
    for row in file:
        # data = row.strip('\n')
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