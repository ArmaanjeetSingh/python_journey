class Payment:
    def pay(self,amount):
        pass

class PaymentProcessor:
    def process(self,amount,method):
        print(f"Processing {amount} via {method}")

class CreditCardPayment(Payment):
    def __init__(self):
        self.processor = PaymentProcessor()

    def pay(self,amount):
        self.processor.process(amount,"Credit Card")

class UPIPayment(Payment):
    def __init__(self):
        self.processor = PaymentProcessor()

    def pay(self,amount):
        self.processor.process(amount,"UPI Payment")

class CashPayment(Payment):
    def __init__(self):
        self.processor = PaymentProcessor()

    def pay(self,amount):
        self.processor.process(amount,"Cash Payment")

payments = [
    CreditCardPayment(),
    UPIPayment(),
    CashPayment()
]

for payment in payments:
    payment.pay(1000)
