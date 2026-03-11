current_choice = "-"
computer_parts = []
available_parts = ["computer","monitor","keyboard","mouse","mouse mat","hdmi cable","dvd drive"]
valid_choices = [str(i) for i in range(1,len(available_parts)+1)]

while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("please add options from the list below")
        for number,part in enumerate(available_parts):
            print("{0}: {1}".format(number,part))
        
    current_choice = input("Enter yoyur choice: ")
print(computer_parts)

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []
for i in data :
    if"shrub" in i.casefold():       
        shrubs.append(i)
    else:
        flowers.append(i)
print(flowers)
print(shrubs)