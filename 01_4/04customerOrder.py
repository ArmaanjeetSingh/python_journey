from payment import CreditCardPayment as CreditCard, UPIPayment as UPI, CashPayment as Cash
class Item:
    def __init__(self,data,quantity):
        self.name,self.price = data #tuple
        self.quantity = quantity

    def total_price(self):
        return self.price *self.quantity

class Order:
    def __init__(self):
        self.items = [] #Order HAS-A list of Item object

    def add_item(self,item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.total_price()
        return total

    def show_items(self):
        for item in self.items:
            print(f"{item.name} x {item.quantity} = {item.total_price()}")

data = [
    (("Laptop", 50000), 1),#((name,price),quantity)
    (("Mouse", 500), 2),
    (("Keyboard", 1500), 1)
]

if __name__ == '__main__':
    order = Order()

    for item_data, qty in data:
        item = Item(item_data, qty)
        order.add_item(item)
    
    order.show_items()
    total = order.calculate_total()
    print("Total : ",total)

    payments = [CreditCard(), UPI(), Cash()]

    for p in payments:
        p.pay(total)