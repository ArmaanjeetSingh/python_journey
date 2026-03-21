class Payment:
    def pay(self, amount):
        pass


class PaymentProcessor:
    def process(self, amount, method):
        print(f"Paid {amount} via {method}")


class CreditCardPayment(Payment):
    def __init__(self):
        self.processor = PaymentProcessor()

    def pay(self, amount):
        self.processor.process(amount, "Credit Card")


class UPIPayment(Payment):
    def __init__(self):
        self.processor = PaymentProcessor()

    def pay(self, amount):
        self.processor.process(amount, "UPI")


class CashPayment(Payment):
    def __init__(self):
        self.processor = PaymentProcessor()

    def pay(self, amount):
        self.processor.process(amount, "Cash")
# payments = [
#     CreditCardPayment(),
#     UPIPayment(),
#     CashPayment()
# ]

# for payment in payments:
#     payment.pay(1000)
