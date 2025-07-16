import os

FILENAME = "users.txt"

def load_users():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, "r") as file:
        lines = file.readlines()
        return dict(line.strip().split(":") for line in lines)

def save_users(users):
    with open(FILENAME, "w") as file:
        for user, pwd in users.items():
            file.write(f"{user}:{pwd}\n")

def signup(users):
    username = input("Choose a username: ")
    if username in users:
        print("Username already exists. Try another.")
        return
    password = input("Choose a password: ")
    users[username] = password
    save_users(users)
    print("Signup successful!")

def login(users):
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
    else:
        print("Invalid credentials.")

def main():
    users = load_users()
    while True:
        print("\n--- Login System ---")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            login(users)
        elif choice == "2":
            signup(users)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
