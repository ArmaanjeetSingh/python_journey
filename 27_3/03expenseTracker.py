import random
import datetime
import functools
class Expense:
    def __init__(self,amount,category,date):
        self.expense = {
            "amount":amount,
            "category":category,
            "date":date
        }



class User:
    def __init__(self,name):
        self.user = {
            "name":name,
            "expenses":[]
        }



class ExpenseTracker:
    def __init__(self):
        self.users = {}
        self.user_id = 1000 

    @staticmethod
    def get_current_date():
        return datetime.datetime.now().strftime("%Y-%m-%d")


    def add_user(self,name):
        self.user_id += 1
        username = f"{name}@{self.user_id}"
        self.users[username] = User(name)
        print(f'{username} created for {name}')
        return username

    def validate_username(self,username):
        return self.users.get(username)

    def add_expense(self,username,amount,category):
        user1 = self.validate_username(username)
        if user1 and amount > 0:
            date = ExpenseTracker.get_current_date()
            user1.user['expenses'].append(Expense(amount,category,date))
            print(f'{user1.user['name']} has been updated with new expense {amount} under {category}')
        else:
            print('check your username')


    def total_spent(self,username):
        user1 = self.validate_username(username)
        if user1:
            total = sum(exp.expense['amount'] for exp in user1.user['expenses'])
            print(f'Total amount : {total} spent by {user1.user['name']}')
        else:
            print("Invalid user")


    def category_spending(self,username):
        user1 = self.validate_username(username)
        if user1:
            result = {}
            for exp in user1.user['expenses']:
                cat = exp.expense['category']
                amt = exp.expense['amount']

                result[cat] = result.get(cat, 0) + amt

            for k,v in result.items():
                print(f'{k} : {v}')


    def highest_expense(self,username):
        user = self.validate_username(username)

        if user and user.user['expenses']:
            max_exp = max(user.user['expenses'],key=lambda x:x.expense['amount'])
            print(max_exp.expense)

        else:
            print('No expenses found')




if __name__ == '__main__':
    tracker = ExpenseTracker()
    u1 = tracker.add_user('Rahul')
    tracker.add_expense(u1,500,'food')
    tracker.add_expense(u1, 1200, "travel")
    tracker.add_expense(u1, 800, "food")
    tracker.total_spent(u1)
    tracker.category_spending(u1)