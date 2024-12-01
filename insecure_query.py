import sqlite3

# Establish a database connection
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Simulate user input
user_input = "admin' OR '1'='1"

# Insecure SQL query (vulnerable to SQL injection)
query = f"SELECT * FROM users WHERE username = '{user_input}'"
print("Executing query:", query)
cursor.execute(query)

# Fetch and print results
results = cursor.fetchall()
print("Results:", results)

# Close the connection
conn.close()
