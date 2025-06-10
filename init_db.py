import sqlite3

def init_db():
    try:
        # Connect to the database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Drop the appliances table if it exists
        cursor.execute('DROP TABLE IF EXISTS appliances;')

        # Create users table with password hashing in mind
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,  -- Store hashed password
            details TEXT
        );
        ''')

        # Create appliances table with foreign key and power rating column
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS appliances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            institution_type TEXT,
            bill_date TEXT,
            historical_units REAL,
            previous_bill REAL,
            appliance_name TEXT,
            avg_hours_used REAL,
            power_rating REAL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
        ''')

        # Commit changes and close connection
        conn.commit()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    init_db()