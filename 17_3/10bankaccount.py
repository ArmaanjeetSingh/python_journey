import datetime
class BankAccount :
    def __init__(self,account_holder,balance):
        self._account_holder = account_holder
        self._balance = balance
        self._transactions = []

    def current_time(self):
        return datetime.datetime.now()

    def deposit(self,amount):
        if amount > 0 :
            self._balance += amount
            self._transactions.append({
                "type": "deposit",
                "amount": amount,
                "time": self.current_time()
            })
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
            self._transactions.append({
                "type": "withdraw",
                "amount": amount,
                "time": self.current_time()
            })
            return True
        else:
            print("Insufficient balance")
            return False

    def get_balance(self):
        return self._balance

    def get_transactions(self):
        for txn in self._transactions:
            print(f"{txn['time']} : {txn['type']} {txn['amount']}")


class SavingsAccount(BankAccount):
    def __init__(self,account_holder,balance,interest_rate):
        super().__init__(account_holder,balance)
        self._interest_rate = interest_rate

    def deposit(self,amount):
        super().deposit(amount)
        interest = self._balance * self._interest_rate / 100
        self._balance += interest

        self._transactions.append({
            "type": "interest",
            "amount": interest,
            "time": self.current_time()
        })


class CurrentAccount(BankAccount):
    def __init__(self,account_holder,balance,overdraft = 5000):
        super().__init__(account_holder,balance)
        self._overdraft = overdraft

    def withdraw(self,amount):
        if self._balance - amount >= - self._overdraft:
            self._balance -= amount
            self._transactions.append({
                "type":"withdraw",
                "amount": amount,
                "time": self.current_time()
            })

acc1 = SavingsAccount("Vinayak", 1000, 5)
acc1.deposit(500)
acc1.withdraw(200)

acc2 = CurrentAccount("Arjun", 1000)
acc2.withdraw(6000)

print("Balance:", acc1.get_balance())
acc1.get_transactions()


