#!/user/bin/python3
# Script: Ops 401 Class 3 Code Challenge
# Joshua Phipps
# 4/24/2023
# Purpose: Uptime Sensor Tool Part 2 of 2


from cryptography.fernet import Fernet
import os

# Function to handle writing key
def write_key():
    # Generate a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key
def load_key():
    # Load the key from the current file name key.key
    return open("key.key", "rb").read()

# Function to encrypt a file path
def encrypt_filepath(filepath):
    # Load the key
    key = load_key()
    f = Fernet(key)

    # Encode the filepath as bytes
    message = filepath.encode()

    # Encrypt the filepath
    encrypted_filepath = f.encrypt(message)

    return encrypted_filepath

# Function to decrypt a file path
def decrypt_filepath(encrypted_filepath):
    # Load the key
    key = load_key()
    f = Fernet(key)

    # Decrypt the filepath
    decrypted_filepath = f.decrypt(encrypted_filepath)

    # Decode the filepath from bytes to string
    filepath = decrypted_filepath.decode()

    return filepath

# Function to encrypt a file
def encrypt_file(filepath):
    # Encrypt the filepath
    encrypted_filepath = encrypt_filepath(filepath)

    # Load the key
    key = load_key()
    f = Fernet(key)

    # Read the file content
    with open(filepath, "rb") as file:
        file_data = file.read()

    # Encrypt the file content
    encrypted_data = f.encrypt(file_data)

    # Replace the file with the encrypted content
    with open(encrypted_filepath, "wb") as file:
        file.write(encrypted_data)

    file.close()

    print(f"File {filepath} encrypted successfully!")

# Function to decrypt a file
def decrypt_file(encrypted_filepath):
    # Decrypt the filepath
    filepath = decrypt_filepath(encrypted_filepath)

    # Load the key
    key = load_key()
    f = Fernet(key)

    # Read the file content
    with open(encrypted_filepath, "rb") as file:
        file_data = file.read()

    # Decrypt the file content
    decrypted_data = f.decrypt(file_data)

    # Replace the file with the decrypted content
    with open(filepath, "wb") as file:
        file.write(decrypted_data)

    file.close()

    print(f"File {filepath} decrypted successfully!")

# Function to encrypt a string
def encrypt_string(cleartext):
    # Load the key
    key = load_key()
    f = Fernet(key)

    # Encode the string as bytes
    message = cleartext.encode()

    # Encrypt the message
    encrypted_message = f.encrypt(message)

    # Print the encrypted message
    print("Encrypted message: ", encrypted_message.decode())

# Function to decrypt a string
def decrypt_string(ciphertext):
    # Load the key
    key = load_key()
    f = Fernet(key)

    # Decode the string from base64
    message = ciphertext.encode()

    # Decrypt the message
    decrypted_message = f.decrypt(message)

    # Print the decrypted message
    print("Decrypted message: ", decrypted_message.decode())

# Main program
write_key()  # Call write_key function to generate key file
while True:
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    mode = input("Enter the mode (1-4): ")

    if mode == "1":
        filepath = input("Enter the file path to encrypt: ")
        if os.path.isfile(filepath):
            encrypt_file(filepath)
        else:
            print("File does not exist!")
    elif mode == "2":
        filepath = input("Enter the file path to decrypt: ")
        if os.path.isfile(filepath):
            decrypt_file(filepath)
        else:
            print("File does not exist!")
    elif mode == "3":
        cleartext = input("Enter the string to encrypt: ")
        encrypt_string(cleartext)
    elif mode == "4":
        ciphertext = input("Enter the string to decrypt: ")
        decrypt_string(ciphertext)
    else:
        print("Invalid mode! Please enter a valid mode")
