import sqlite3

connection = sqlite3.connect("users.db")  # connect to database. Crete if it doesn't exist

cursor = connection.cursor()

command = "CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT, age INTEGER)"

cursor.execute(command)
