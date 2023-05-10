#!/user/bin/python3
# Script: Ops 401 Class 18 Code Challenge
# Joshua Phipps
# 5/10/2023
# Purpose: Automated Brute Force Wordlist Attack Tool Part 3 of 3



import time
from zipfile import ZipFile

# Mode 1: Iterator
def iterator():
    # Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
    filepath = input("Enter your dictionary filepath:\n")

    # Open file
    with open(filepath) as file:
        for word in file:
            password = word.strip()
            try:
                with ZipFile(zip_file) as zf:
                    zf.extractall(pwd=bytes(password, 'utf-8'))
                print(f"Password found: {password}")
                return
            except Exception as e:
                # Incorrect password, continue iterating
                continue

    # If the loop completes without finding the password
    print("Password not found in the dictionary.")


# Mode 2: Check Password
def check_password():
    # Accepts a user input word list file path.
    dictionary_path = input("Enter dictionary filepath:\n")
    # Search the word list for the user input string.
    password_found = False
    with open(dictionary_path) as file:
        for word in file:
            password = word.strip()
            try:
                with ZipFile(zip_file) as zf:
                    zf.extractall(pwd=bytes(password, 'utf-8'))
                print(f"Password found: {password}")
                password_found = True
                break
            except Exception as e:
                # Incorrect password, continue iterating
                continue

    if not password_found:
        print("Password not found in the dictionary.")


# Prompt the user to select a mode
mode = input("Select a mode:\n1. Iterator\n2. Check Password\n")

# Run the selected mode
if mode == "1":
    zip_file = input("Enter the path to the password-protected ZIP file:\n")
    iterator()
elif mode == "2":
    zip_file = input("Enter the path to the password-protected ZIP file:\n")
    check_password()
else:
    print("Invalid mode selected")

