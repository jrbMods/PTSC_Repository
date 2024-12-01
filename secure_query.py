import sqlite3

# Establish a database connection
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Simulate user input
user_input = "admin' OR '1'='1"

# Secure SQL query using parameterized queries
query = "SELECT * FROM users WHERE username = ?"
print("Executing query:", query)
cursor.execute(query, (user_input,))

# Fetch and print results
results = cursor.fetchall()
print("Results:", results)

# Close the connection
conn.close()
