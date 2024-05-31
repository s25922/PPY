import os
import base64
import json
from cryptography.fernet import Fernet, InvalidToken
import random
import string
import binascii

# Constants
ENCRYPTION_KEY = 'xUEKJp5PIzv7FYVtH8RDOze6U3V6x6F4iExBNbZCgQk='
FILENAME = 'passwords.json'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'

class Website:
    def __init__(self, name, link, login, password):
        self.name = name
        self.link = link
        self.login = login
        self.password = password

    def to_dict(self):
        return {
            'name': self.name,
            'link': self.link,
            'login': self.login,
            'password': self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['link'], data['login'], data['password'])

def encrypt_file(data, filename):
    fernet = Fernet(ENCRYPTION_KEY)
    encrypted_data = fernet.encrypt(json.dumps(data).encode())
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist. Creating a new one.")
        return []
    try:
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        fernet = Fernet(ENCRYPTION_KEY)
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return json.loads(decrypted_data)
    except InvalidToken:
        print("Error: Invalid token. The file may be corrupted or the encryption key is incorrect.")
    except binascii.Error:
        print("Error: Incorrect padding. The file may be corrupted.")
    except json.JSONDecodeError:
        print("Error: JSON decode error. The file content is not valid JSON.")
    return []


def save_websites_to_file(websites, filename):
    data = [website.to_dict() for website in websites]
    encrypt_file(data, filename)

def read_websites_from_file(filename):
    data = decrypt_file(filename)
    return [Website.from_dict(item) for item in data]

def check_password_strength(password):
    return (len(password) >= 8 and any(c.islower() for c in password) and
            any(c.isupper() for c in password) and any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password))

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def search_website_by_name(websites, name):
    for website in websites:
        if website.name == name:
            print(f"\nWebsite: {website.name}")
            print(f"Link: {website.link}")
            print(f"Login: {website.login}")
            print(f"Password: {website.password}")
            return
    print("Website not found!")


def main():
    print("Welcome to the !")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        print("Invalid credentials")
        return

    try:
        websites = read_websites_from_file(FILENAME)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        websites = []

    while True:
        print("\nMenu:")
        print("1. Add website")
        print("2. View passwords")
        print("3. Generate strong password")
        print("4. Delete website")
        print("5. Edit website")
        print("6. Search website by name")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter website name: ")

            # Check if the website name already exists
            if any(website.name == name for website in websites):
                print("A website with this name already exists. Please choose a different name.")
                continue

            link = input("Enter website link: ")
            login = input("Enter login for the website: ")
            use_generated_password = input(
                "Do you want to generate a strong password automatically? (yes/no): ").strip().lower()

            if use_generated_password == 'yes':
                password = generate_strong_password()
                print(f"Generated strong password: {password}")
            else:
                while True:
                    password = input("Enter website password: ")
                    if check_password_strength(password):
                        break
                    else:
                        print("Password is not strong enough! Please enter a stronger password.")

            website = Website(name, link, login, password)
            websites.append(website)
            print("Website added successfully!")

        elif choice == '2':
            for website in websites:
                print(f"\nWebsite: {website.name}")
                print(f"Link: {website.link}")
                print(f"Login: {website.login}")
                print(f"Password: {website.password}")

        elif choice == '3':
            password = generate_strong_password()
            print(f"Generated strong password: {password}")

        elif choice == '4':
            name = input("Enter the website name to delete: ")
            websites = [website for website in websites if website.name != name]
            print("Website deleted successfully!")

        elif choice == '5':
            name = input("Enter the website name to edit: ")
            for website in websites:
                if website.name == name:
                    new_name = input(
                        "Enter new website name (or press Enter to keep the current name): ") or website.name

                    # Check if the new website name already exists (and it's not the current website being edited)
                    if new_name != name and any(w.name == new_name for w in websites):
                        print("A website with this new name already exists. Please choose a different name.")
                        continue

                    new_link = input(
                        "Enter new website link (or press Enter to keep the current link): ") or website.link
                    new_login = input(
                        "Enter new login for the website (or press Enter to keep the current login): ") or website.login
                    use_generated_password = input(
                        "Do you want to generate a strong password automatically? (yes/no): ").strip().lower()

                    if use_generated_password == 'yes':
                        new_password = generate_strong_password()
                        print(f"Generated strong password: {new_password}")
                    else:
                        while True:
                            new_password = input(
                                "Enter new website password (or press Enter to keep the current password): ") or website.password
                            if check_password_strength(new_password):
                                break
                            else:
                                print("Password is not strong enough! Please enter a stronger password.")

                    website.name = new_name
                    website.link = new_link
                    website.login = new_login
                    website.password = new_password
                    print("Website edited successfully!")
                    break
            else:
                print("Website not found!")

        elif choice == '6':
            name = input("Enter the website name to search: ")
            search_website_by_name(websites, name)
            break

        elif choice == '7':
            save_websites_to_file(websites, FILENAME)
            print("Data saved. Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
