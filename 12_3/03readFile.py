with open(r"D:\denama\python\11_3\Jabberwocky.txt") as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if "jubjub" in line.casefold():
            break

print("*"*80)

with open(r"D:\denama\python\11_3\Jabberwocky.txt") as jabber:
    while True:
        print(line.rstrip())
        if "jubjub" in line.casefold():
            break


input_filename = r"D:\denama\python\11_3\country_info.txt"

with open(input_filename) as country_file:
    for row in country_file:
        data = row.split('|')
        country,capital,code,code3,dialing,timezone,currency = data
        