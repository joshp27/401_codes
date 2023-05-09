#!/user/bin/python3
# Script: Ops 401 Class 16 Code Challenge
# Joshua Phipps
# 5/8/2023
# Purpose: Automated Brute Force Wordlist Attack Tool Part 1 of 3



import getpass
import os
import time


# Mode 1
def iterator():
    # Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
    filepath = input("Enter your dictionary filepath:\n")

    # Open file
    with open(filepath) as file:
        for word in file:
            print(word.strip())
            # Add a delay between words.
            time.sleep(1)

# # Mode 2: Defensive; Password Recognized
def check_password():
    # Accepts a user input string.
    user_password = input("Enter password to check:\n")
    # Accepts a user input word list file path.
    dictionary_path = input("Enter dictionary filepath:\n")
    # Search the word list for the user input string.
    password_found = False
    with open(dictionary_path) as file:
        for word in file:
            if word.strip() == user_password:
                print("You in DANGA, yo password is weak!")
                password_found = True
                break



# Prompt the user to select a mode
mode = input("Select a mode:\n1. Iterator\n2. Check Password\n")

# Run the selected mode
if mode == "1":
    iterator()
elif mode == "2":
    check_password()
else:
    print("Invalid mode selected")
