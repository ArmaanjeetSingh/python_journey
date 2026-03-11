def removeprefix(string:str,prefix:str)->str:
    if string.startswith(prefix):
        return string[len(prefix)]
    else:
        return string[:] #return copy of `string`

def removesuffix(string:str,suffix:str)->str:
    if suffix and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]

filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first =  poem.readline().rstrip()

print(first)

twas_removed = removeprefix(first,"'Twas")
print(twas_removed)
toves_removed = removesuffix(first,'toves')
print(toves_removed)