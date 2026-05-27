# Login System by Jeremy Okeke

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = {}

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        username = input("New username: ")
        password = input("New password: ")
        users[username] = hash_password(password)
        print("User registered!")

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == hash_password(password):
            print("Login successful!")
        else:
            print("Invalid username or password.")

    elif choice == "3":
        break