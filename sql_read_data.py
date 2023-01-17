import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")  # Select everything (*) from table "users"
results = cursor.fetchall()
print(results)
