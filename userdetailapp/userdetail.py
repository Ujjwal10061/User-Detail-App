import sqlite3

def get_user_details(username):
    # Connect to the database
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    # Safe SQL query using parameterization
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    # Fetch the results
    user = cursor.fetchone()
    connection.close()

    return user
