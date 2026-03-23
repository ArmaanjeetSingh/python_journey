
class Account(object):
    def __init__(self,name:str,opening_balance=0):
        self.name = name
        self._balance = opening_balance
        print("Account created for {}".format(self.name))
        self.show_balance()

    def withdraw(self,amount:int)->float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("{:.2f} withdraw".format(amount/100))
            return amount /100

        else:
            print("The amount must be greater than zero and")
            return 0.0

    def deposit(self,amount:int)->float:
        if amount > 0:
            self._balance += amount
            print("{:.2f} withdrawn".format(amount/100))
        return self._balance /100

    def show_balance(self):
        print("Balance on account {} is {}".format(self.name,self._balance/100))

if __name__ == "__main__":
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()
        