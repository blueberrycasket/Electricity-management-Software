import sqlite3

DATABASE = 'users.db'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()
cursor.execute("ALTER TABLE appliances ADD COLUMN username TEXT")
cursor.execute("ALTER TABLE appliances ADD COLUMN power_rating REAL")  # Add this too for fullelctro.html
conn.commit()
conn.close()

print("Database updated with 'username' and 'power_rating' columns.")