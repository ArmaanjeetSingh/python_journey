import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "updatemail@gmail.com"
phone = input("Enter phone number ")

# update_sql = 'UPDATE contacts SET email = "updatemail@gmail.com" WHERE contacts.phone = 12345678;'
update_sql = 'UPDATE contacts SET email = {} WHERE contacts.phone = {};'.format(new_email,phone)
update_cursor = db.cursor()
update_cursor.execute(update_sql)
update_cursor.connection.commit()
#connection specific commit 

print()
print("Are connections the same : {}".format(update_cursor.connection == db))
print()


for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('*'*20)

# db.commit()
db.close()