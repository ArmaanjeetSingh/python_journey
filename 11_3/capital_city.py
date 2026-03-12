countries = {}

# user_choice = input("Enter your country: ")

with open("country_info.txt", "r") as country_file:
    for row in country_file:

        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data

        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }

        countries[country.casefold()] = country_dict


# for name, country in countries.items():
#     if name.casefold() == user_choice.casefold():
#         print(country["capital"])

while True:
    chosen_country  = input("Please enter the name of country ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f'The capital of {chosen_country} is {country_data['capital']}')
    else:
        break