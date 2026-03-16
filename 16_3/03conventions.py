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
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(),balance)]
        print("Account created for "+self._name)

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            # self._transaction_list.append((pytz.utc.localize(datetime.datetime.now()),amount))
            self._transaction_list.append((Account._current_time(),amount))

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(),-amount))
        else:
            print("The amount should be greater than zero or balance should be more than amount")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transaction(self):
        for date,amount in self._transaction_list:
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

    steph = Account("Steph",800)
    steph.balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transaction()
    print(steph.__dict__)