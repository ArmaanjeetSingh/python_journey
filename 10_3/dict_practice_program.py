inventory = {
    "rice": {"price": 60, "stock": 50},
    "wheat": {"price": 40, "stock": 70},
    "milk": {"price": 30, "stock": 25},
    "eggs": {"price": 6, "stock": 200}
}

def show_inventory()->None:
    """shows all items with price and stock
    """    
    for item,details in inventory.items():
        price = details["price"]
        stock = details["stock"]
        print(f"{item} - Price: {price}, Stock: {stock}")

def buy_item(buy_item:str,buy_qty:int)->int:

    for item,details in inventory.items():
        if buy_item.casefold() == item.casefold() :

            price = details["price"]
            stock = details["stock"]
            if stock >= buy_qty:
                total_bill = price * buy_qty
                inventory[item]["stock"] -= buy_qty

                print("Total bill:", total_bill)
                print("Remaining stock ",inventory[item]["stock"])

            else:
                print("Stock less than demand")


def add_item(item:str,price:int,qty:int):
    inventory.update({item:{"price":price,"stock":qty}})
    print("Item {} is updated for price {} and stock {}".format(item,price,qty))

def remove_item(item:str):
    result = inventory.pop(item,None)
    if result :
        price = result["price"]
        stock = result["stock"]
        print(f"{item} with price {price} and stock {stock} is deleted")
    else:
        print("not found")

def check_item(item:str):
    result = inventory.get(item,None)
    if result :
        print(f"Price: {result['price']} - Stock: {result['stock']}")
    else:
        print("Item not found")

show_inventory()

buy_item("rice", 5)

add_item("sugar", 50, 30)

check_item("milk")

remove_item("eggs")