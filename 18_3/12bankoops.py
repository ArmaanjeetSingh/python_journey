class Account:
    def __init__(self,name,balance):
        self.name = name
        self._balance = balance #private variable

    def get_balance(self):
        return self._balance

    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f'{amount} deposited sucessfully')
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f'{amount} withdrawn successfully')
        else:
            print("Insufficient Balance")

    def display(self):
        print(f"Account Holder : {self.name}")
        print(f"Balance : {self._balance}")


class SavingsAccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance)

    #Method Overriding
    def withdraw(self,amount):
        if amount > 10000:
            print("Cannot withdraw more than 10000 in savings account")
        else:
            super().withdraw(amount)

class CurrentAccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance)

    def withdraw(self,amount):
        if amount <= self.get_balance() + 5000:
            print("Overdraft facility is used" if amount > self.get_balance() else "")
            super().withdraw(amount)
        else:
            print("Overdraft limit exceeded.")

def process_withdraw(account,amount):
    account.withdraw(amount)

acc1 = SavingsAccount("Simran", 20000)
acc2 = CurrentAccount("Rahul", 5000)

print("\n--- Savings Account ---")
acc1.deposit(2000)
process_withdraw(acc1, 15000)  # Polymorphism
acc1.display()

print("\n--- Current Account ---")
acc2.deposit(1000)
process_withdraw(acc2, 9000)   # Polymorphism
acc2.display()