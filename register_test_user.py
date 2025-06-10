import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Register a test user
username = 'testuser'
password = 'testpassword'

try:
    cursor.execute('INSERT INTO users (username, password, details) VALUES (?, ?, ?)',
                   (username, password, ''))
    conn.commit()
    print("Test user registered successfully.")
except sqlite3.IntegrityError:
    print("User already exists.")

# Close the connection
conn.close()
