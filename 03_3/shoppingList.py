shoppingList = ["milk","pasta","eggs","spam","bread","rice"]
for item in shoppingList:
    if item != "spam":
       print("Buy "+item)
       
for item in shoppingList:
    if item == "spam":
        continue
    print("buy "+item)