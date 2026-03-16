import pytz
import datetime


class Account:
    """Simple account class with balance
    """
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.now()
        return pytz.utc.localize(utc_time)

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for "+self.name)

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.now()),amount))
            self.transaction_list.append((Account._current_time(),amount))

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(),-amount))
        else:
            print("The amount should be greater than zero or balance should be more than amount")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transaction(self):
        for date,amount in self.transaction_list:
            if amount > 0:
               tran_type = "deposited"
            else:
                tran_type = "withdraw"
                amount *= -1
            print("{} {} on {} (local time was {})".format(amount,tran_type,date,date.astimezone())) 

if __name__ == '__main__':
    tim = Account("Tim",0)
    tim.deposit(1000)
    tim.withdraw(5000)
    tim.withdraw(200)
    tim.show_balance()

    tim.show_transaction()