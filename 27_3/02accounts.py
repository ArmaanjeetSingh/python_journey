import random
class Account:
    def __init__(self,name = " ",balance = 0):
        self.account = {
            "name":name,
            "balance":balance,
            "transactions":[]
        }

    def show_account(self):
        return f"Name : {self.account['name']}, Balance : {self.account['balance']}"

class Bank:
    def __init__(self):
        self.accounts = {}
        self.acc_no = 1000

    def validate_account(self,acc_no):
        return self.accounts.get(acc_no)


    def create_account(self,name,balance):
        self.acc_no += 1
        acc_no = str(self.acc_no)
        self.accounts[acc_no] = Account(name,balance)
        print("Account created for {} with {}".format(name,acc_no))
        return acc_no


    def deposit(self,acc_no,amount):
        deposit_acc = self.accounts.get(acc_no)
        if deposit_acc is not None and amount > 0:
            self.accounts[acc_no].account['balance'] += amount
            self.accounts[acc_no].account['transactions'].append('Deposited {}'.format(amount))

        else :
            print("Insert valid credentials")


    def withdraw(self,acc_no,amount):
        withdraw_acc = self.accounts.get(acc_no)
        if withdraw_acc is not None:
            if 0 < amount <= self.accounts[acc_no].account['balance'] :
                self.accounts[acc_no].account['balance'] -= amount
                self.accounts[acc_no].account['transactions'].append('Withdraw {}'.format(amount))
                return 1

            else:
                print("Insufficient balance")
                return 0
        else:
            print("Invalid credentials")
            return 0


    def transfer(self,acc_no1,acc_no2,amount):
        deposit_acc = self.accounts.get(acc_no2)
        withdraw_acc = self.accounts.get(acc_no1)
        if deposit_acc and withdraw_acc:
            success = self.withdraw(acc_no1,amount)
            if success :
               self.deposit(acc_no2,amount)
               print("Tansfer {} to {}".format(amount,acc_no2))



    def show_transactions(self,acc_no):
        deposit_acc = self.accounts.get(acc_no)
        if deposit_acc is not None:
           for transac in self.accounts[acc_no].account['transactions']:
               print(transac)


    def show_account(self,acc_no):
        acc = self.validate_account(acc_no)
        # print(acc)
        if acc :
            print(acc.show_account())
        else:
            print("Invalid account")


if __name__ == '__main__':
    bank = Bank()

    a1 = bank.create_account("Vinayak", 1000)
    a2 = bank.create_account("Rahul", 500)

    bank.deposit(a1, 200)
    bank.withdraw(a1, 100)

    bank.transfer(a1, a2, 300)

    bank.show_transactions(a1)
    bank.show_account(a1)
