import sqlite3

db = sqlite3.connect("contacts1.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts1 (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts1(name, phone, email) VALUES('Tim', 654678, 'tim@email.com')")
db.execute("INSERT INTO contacts1 VALUES('Brian', 1234, 'brian@email.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts1")

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.commit()
db.close()
