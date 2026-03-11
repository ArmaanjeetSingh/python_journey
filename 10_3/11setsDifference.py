travel_mode = {"1": "car", "2": "plane"}

items = {
    "clothes",
    "toothbrush",
    "charger",
    "laptop",
    "snacks",
    "water bottle",
    "knife",
    "lighter"
}

restricted_items = {
    "knife",
    "lighter",
    "gun",
    "explosives",
    "large liquids"
}
print("Please choose your mode of travel:")
for key,value in travel_mode.items():
    print(f"{key} : {value}")

mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode=="2":
    #travelling by plane, remove restricted items
    # for restricted_item in restricted_items:
    #     items.remove(restricted_item)
    items -= restricted_items

print("You need to pack: ")
for item in sorted(items):
    print(item)

favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

basket = {'garlic crusher',
          'stirling engine',
          'frying pan',
          'shirt',
          'bush hat',
          }

suggestions = sorted(favourites - basket)
print(suggestions)