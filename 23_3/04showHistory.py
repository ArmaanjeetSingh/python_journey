import sqlite3

db = sqlite3.connect("account.db")
cursor = db.execute("SELECT * FROM history")
for row in cursor:
    print(row)