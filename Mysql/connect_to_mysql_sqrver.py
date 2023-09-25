import bcrypt
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='your_host',
    port=3306,  # Replace with the desired port number
    user='your_username',
    password='your_password',
    database='your_database'
)
cursor = conn.cursor()

# Create a table to store user credentials
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )''')
conn.commit()


def register_user(username, password):
    # Hash and salt the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Store the username and hashed password in the database
    cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)',
                   (username, hashed_password.decode('utf-8')))
    conn.commit()
    print("User registered successfully!")


def verify_user(username, password):
    # Retrieve the hashed password from the database based on the provided username
    cursor.execute('SELECT password FROM users WHERE username = %s', (username,))
    result = cursor.fetchone()

    if result:
        stored_password = result[0]
        # Verify the provided password against the stored hashed password
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            print("Authentication successful!")
        else:
            print("Incorrect password.")
    else:
        print("User not found.")


# Example usage:
register_user("alice", "password123")  # Register a user
verify_user("alice", "password123")  # Verify the user's credentials

# Close the database connection
conn.close()
