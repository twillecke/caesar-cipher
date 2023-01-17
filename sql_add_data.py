import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("INSERT INTO users VALUES ('Rishab', '123453454', 13)")
cursor.execute("INSERT INTO users VALUES ('Joshua', '683463456', 17)")
cursor.execute("INSERT INTO users VALUES ('John', '1340982', 20)")

connection.commit()