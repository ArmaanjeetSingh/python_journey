from medals_data import medals_table

def sort_keys(d:dict)->str:
    return d['rank']


medals_table.sort(key=lambda medals_table: medals_table['rank'])
print(medals_table)

x = 99 
result = 'in range' if x < 100 else "out of range"
print(result)