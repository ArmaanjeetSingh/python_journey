import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo
import pickle

db = sqlite3.connect("account2.db",detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL, amount INTEGER NOT NULL,zone INTEGER NOT NULL, PRIMARY KEY (time,account))")
# db.execute("ALTER TABLE transactions RENAME TO history")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS SELECT strftime('%Y-%m-%d, %H:%M:%S',history.time,'localtime') AS localtime, history.account,history.amount,history.zone FROM history ORDER BY history.time")


class Account(object):
    def __init__(self,name:str,opening_balance=0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)",(name,))
        row = cursor.fetchone()
        
        if row:
            self.name, self._balance = row
            print("Retrieved record for {}".format(self.name))
 
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?,?)",(name,opening_balance))
            cursor.connection.commit()
            print("Account created for {}".format(self.name))

    @staticmethod
    def get_current_time():
        utc_time = datetime.now(ZoneInfo("UTC"))
        local_time = utc_time.astimezone()
        zone = local_time.tzinfo
        return utc_time,zone

    
    
    def save_update(self,amount):
        new_balance = self._balance + amount
        deposit_time,zone = Account.get_current_time() #<------ unpacking return tuple
        pickled_zone = pickle.dumps(zone)

        db.execute("UPDATE accounts SET balance = ? WHERE name = ?",(new_balance,self.name))
        db.execute("INSERT INTO history VALUES(?,?,?,?)",(deposit_time,self.name,amount,pickled_zone))
        db.commit()
        self._balance = new_balance
        
        
    def withdraw(self,amount:int)->float:
        if 0 < amount <= self._balance:
            # new_balance = self._balance - amount
            # withdraw_time = Account.get_current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE name = ?",(new_balance,self.name))
            # db.execute("INSERT history VALUES(?,?,?)",(withdraw_time,self.name,-amount))
            # db.commit()
            self.save_update(-amount)
            print("{:.2f} withdraw".format(amount/100))
            return amount /100

        else:
            print("The amount must be greater than zero and")
            return 0.0


    def deposit(self,amount:int)->float:
        if amount > 0:
            # new_balance = self._balance + amount
            # deposit_time = Account.get_current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE name = ?",(new_balance,self.name))
            # db.execute("INSERT INTO history VALUES(?,?,?)",(deposit_time,self.name,amount))
            # db.commit()
            # self._balance = new_balance
            self.save_update(amount)
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

    terry = Account("Terry")

    brian = Account("Brian",1000)
    eric = Account("Eric",9000)

    db.close()
        