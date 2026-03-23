import sqlite3

db = sqlite3.connect("account.db",detect_types = sqlite3.PARSE_DECLTYPES)

for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%S',history.time,'localtime') AS localtime, history.account,history.amount FROM history ORDER BY history.time"):
    print(row)

db.close()