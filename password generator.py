import random
import string

# Dictionary to store passwords with their associated apps/websites
passwords = {}

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def save_password(app_name, password):
    passwords[app_name] = password

def retrieve_password(app_name):
    return passwords.get(app_name, "Password not found.")

def main():
    while True:
        print("\n1. Generate Password")
        print("2. Retrieve Password")
        print("3. Quit")

        choice = input(str("Enter your choice: "))

        if choice == '1':
            length = int(input("Enter the length of the password: "))
            app_name = input("Enter the name of the application/website: ")
            password = generate_password(length)
            save_password(app_name, password)
            print("Generated Password:", password)
        elif choice == '2':
            app_name = input("Enter the name of the application/website: ")
            password = retrieve_password(app_name)
            print(f"Password for {app_name}: {password}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
