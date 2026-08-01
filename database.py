import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

print("Database Connected")