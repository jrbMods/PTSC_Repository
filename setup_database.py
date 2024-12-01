import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a sample table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Insert sample data
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', '1234')")
cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'abcd')")
conn.commit()

print("Database and table created with sample data.")
conn.close()
