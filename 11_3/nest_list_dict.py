customers = {
    101: {
        "name": "Rahul",
        "orders": [
            {"item": "Laptop", "price": 55000},
            {"item": "Mouse", "price": 800}
        ]
    },
    102: {
        "name": "Simran",
        "orders": [
            {"item": "Phone", "price": 25000}
        ]
    }
}


def show_customers()->None:
    for customer_id,info in customers.items():
        print(f"ID : {customer_id} Name : {info["name"]}")

def add_customer(customer_id:int,name:str)->None:
    if customer_id not in customers:
        customers.setdefault(customer_id,
                 {"name":name,
                  "orders":[]
                 })
        print("Customer added")
    else:
        print("Customer already exists")

def add_order(customer_id:int,item:str,price:int)->None:
    if customer:
        order = {
            "item": item,
            "price": price
        }
        customer["orders"].append(order)

        print("Order added")
    else:
        print("Customer not found")

def view_orders(customer_id:int)->None:
    customer = cusotmers.get(cusotmer_id)
    if not customer:
        print("Customer not found")
        return
    print("Customer:", customer["name"])

    for order in customer["orders"]:
        print(order["item"], "-", order["price"])


def calculate_total(customer_id):
    customer = customers.get(customer_id)

    if not customer:
        print("Customer not found")
        return

    total = 0

    for order in customer["orders"]:
        total += order["price"]

    print("Total Bill:", total)


def remove_order(cusotmer_id:int,item:str)->None:
    customer = customers.get(customer_id)
    if not customer_id:
        print("Customer not found")

    for order in customer["orders"]:
        if order["item"] == item:
            customer["orders"].remove(order)
            print("Order removed")
    print("Item not found")
while True:

    print("\n1 Show Customers")
    print("2 Add Customer")
    print("3 Add Order")
    print("4 View Orders")
    print("5 Calculate Bill")
    print("6 Remove Order")
    print("7 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_customers()

    elif choice == "2":
        cid = int(input("Customer ID: "))
        name = input("Name: ")
        add_customer(cid, name)

    elif choice == "3":
        cid = int(input("Customer ID: "))
        item = input("Item: ")
        price = int(input("Price: "))
        add_order(cid, item, price)

    elif choice == "4":
        cid = int(input("Customer ID: "))
        view_orders(cid)

    elif choice == "5":
        cid = int(input("Customer ID: "))
        calculate_total(cid)

    elif choice == "6":
        cid = int(input("Customer ID: "))
        item = input("Item to remove: ")
        remove_order(cid, item)

    elif choice == "7":
        break