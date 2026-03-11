data = [
    ("orange", "A sweet orange citrus fruit"),
    ("apple", "A red or green fruit that is crisp and sweet"),
    ("banana", "A long yellow fruit that is soft and sweet"),
    ("grape", "A small juicy fruit used to make wine"),
    ("mango", "A tropical fruit that is sweet and juicy"),
    ("pineapple", "A tropical fruit with spiky skin and sweet inside"),
    ("strawberry", "A small red fruit with seeds on the outside"),
    ("watermelon", "A large green fruit with red juicy flesh"),
    ("peach", "A soft fruit with fuzzy skin and sweet taste"),
    ("pear", "A green fruit with a soft and sweet inside")
]

# print(ord("a"))
# print(ord("b"))
# print(ord("c"))

def simple_hash(s:str)->int:
    """A ridiculuously simple hashing function"""
    basic_hash = ord(s[0])
    return basic_hash % 10

def get(k:str)->str:
    """Return value for a key or None if key doesn't exist

    Args:
        k (str): _description_

    Returns:
        str: _description_
    """
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None

for key,value in data:
    h = simple_hash(key)
    print(key,h )

keys = [""]*10
values = keys.copy()
for key,value in data:
    h = simple_hash(key)
    print(key,h)
    keys[h] = key
    values[h] = value
print(keys)
print(values)

value = get("grape")
print(value)