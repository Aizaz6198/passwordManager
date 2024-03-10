from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"
PASSWORDS_FILE = 'passwords.txt'


def generate_key():
    return Fernet.generate_key()


def write_key(key):
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)


def load_key():
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def initialize():
    if not os.path.exists(KEY_FILE):
        key = generate_key()
        write_key(key)


def decrypt_password(encrypted_password):
    return fer.decrypt(encrypted_password.encode()).decode()


def encrypt_password(password):
    return fer.encrypt(password.encode()).decode()


def view_passwords():
    with open(PASSWORDS_FILE, 'r') as f:
        for line in f.readlines():
            username, encrypted_password = line.rstrip().split("|")
            password = decrypt_password(encrypted_password)
            print("Username:", username, "| Password:", password)


def add_password():
    username = input('Enter Account Name: ')
    password = input("Enter Password: ")

    with open(PASSWORDS_FILE, 'a') as f:
        f.write(username + "|" + encrypt_password(password) + "\n")


def main():
    initialize()
    key = load_key()
    global fer
    fer = Fernet(key)

    while True:
        mode = input(
            "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
        if mode == "q":
            break

        if mode == "view":
            view_passwords()
        elif mode == "add":
            add_password()
        else:
            print("Invalid mode.")
            continue


if __name__ == "__main__":
    main()
