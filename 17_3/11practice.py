class Dish:
    def __init__(self,name,price):
        self._name = name
        self._price = price

class Restaurant:
    def __init__(self,name):
        self._name = name
        self._menu = []

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value >= 0:
            self._price = value
        else:
            print("Invalid price")

class Order:
    def __init__(self,customer,restaurant):
        self.customer = customer
        self.restaurant = restaurant
        self.items = []

    def add_item(self, dish):
        self.items.append(dish)

    def total_price(self):
        return sum(d.price for d in self.items)
