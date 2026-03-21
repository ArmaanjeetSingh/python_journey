class Product :
    def __init__(self,name,price):
        self._name = name 
        self._price = price

    def get_price(self,quantity=1):
        return self._price *quantity

    def get_name(self):
        return self._name


class RegularProduct(Product):
    def __init__(self,name,price):
        super().__init__(name,price)

    def get_price(self,quantity=1):
        super().get_price(quantity)


class DiscountedProduct(Product):
    def __init__(self,name,price,discount):
        super().__init__(name,price)
        self._discount = discount

    def get_price(self):
        discounted_price = self._price * (1 - self._discount)
        return discounted_price * quantity


class BulkProduct(Product):
    def __init__(self,name,price,discount,threshold):
        super().__init__(name,price)
        self._discount = discount
        self._threshold = threshold

    def get_price(self):
        if quantity > self._threshold:
            discounted_price = self._price * (1 - self._discount)
            return discounted_price * quantity
        return self._price * quantity


class Cart:
    def __init__(self):
        self._cart = {}


    def add_product(self,product,quantity):
        if product in self._cart :
           self._cart[product] += quantity
        else:
            self._cart[product] = quantity

    def remove_product(self,product):
        if product in self._cart:
            del self._cart[product]
    
    def calculate_total(self):
        total = 0
        for product, quantity in self._cart.items():
            price = product.get_price(quantity)
            print(f"{product.get_name()} x {quantity} = {price}")
            total += price
        return total
        
if __name__ == "__main__":
    p1 = RegularProduct("Cap", 500)
    p2 = DiscountedProduct("Shoes", 2000, 0.1)
    p3 = BulkProduct("Notebook", 100, 0.2, threshold=5)

    cart = Cart()
    cart.add_product(p1, 2)
    cart.add_product(p2, 1)
    cart.add_product(p3, 6)

    print("\nCart Total:", cart.calculate_total())

    