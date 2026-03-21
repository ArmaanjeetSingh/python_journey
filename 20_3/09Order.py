from productCart import Cart
from payment import PaymentProcessor
class Order:
    def __init__(self,order_id,cart):
        self._order_id = order_id
        self._cart = cart
        self._status = "CREATED"


    def show_order(self):
        print(f"\nOrder ID : {self._order_id}")
        print(f"Status: {self._status}")
        print("Items:")
        total = self._cart.calculate_total()
        print(f"Total : {total}")


    def make_payment(self,payment_obj):
        if self._status != "CREATED":
           print("Payment not allowed")
           amount = self._cart.calculate_total()
           payment_obj.pay(amount)

           self._status = "PAID"
           print(f"Order {self._order_id} paid successfully.")


    def ship_order(self):
        if self._status != "PAID":
            print("Order must be paid before shipping!")
            return
        self._status = "SHIPPED"
        print(f"Order {self._order_id} shipped.")


    def show_status(self):
        return self._status