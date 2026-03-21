import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")

db.execute("INSERT INTO contacts (name,phone,email) VALUES ('Tim',65456789,'tim@email.com')")

db.execute("INSERT INTO contacts VALUES ('Brian',12345678, 'brianemail@gmail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name,phone,email,sep='\n')
    print("*"*20)
db.commit()
db.close()