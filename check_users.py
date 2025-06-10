import sqlite3

def get_users():
    DATABASE = 'users.db'
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    conn.close()
    return users

if __name__ == "__main__":
    users = get_users()
    for user in users:
        print(user)
