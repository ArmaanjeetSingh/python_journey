class Payment:
    def __init__(self,amount):
        self._amount = amount

    def pay(self):
        if self._amount > 0:
            print(f"{self._amount} is being processed")
        else:
            print("Invalid amount")

class CreditCardPayment(Payment):
    def __init__(self,amount):
        super().__init__(amount = amount)
        self._mode = "credit card"

    def pay(self):
        if self._amount > 0:
           print(self._amount,"has been paid using ",self._mode)

class UPIPayment(Payment):
    def __init__(self,amount,id):
        super().__init__(amount)
        self._mode = "UPI"
        self._id = id

    def pay(self):
        if self._amount > 0:
           print(self._amount,"has been paid using ",self._mode,"ID : {}".format(self._id))

class CashPayment(Payment):
    def __init__(self,amount):
        super().__init__(amount)
        self._mode = "cash"

    def pay(self):
        if self._amount > 0:
           print(self._amount,"has been paid using ",self._mode)

# Create objects
p1 = CreditCardPayment(1000)
p2 = UPIPayment(500, "vinayak@upi")
p3 = CashPayment(200)

# Call methods
p1.pay()
p2.pay()
p3.pay()