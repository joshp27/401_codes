#!/user/bin/python3
# Script: Ops 401 Class 33 Code Challenge
# Joshua Phipps
# 5/32/2023
# Purpose: Signature-based Malware Detection Part 3 of 3

import os
import platform
import hashlib
import time
import requests

def search_files(file_name, directory):
    # Normalize directory path for different OS
    directory = os.path.normpath(directory)

    # Initialize counters
    files_searched = 0
    hits_found = 0

    # Iterate over all files and directories in the given directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if file name matches the search query
            if file == file_name:
                file_path = os.path.join(root, file)
                print(f"Hit found: {file_path}")

                # Generate the file's MD5 hash
                md5_hash = calculate_md5(file_path)

                # Get file information
                file_size = os.path.getsize(file_path)
                timestamp = time.ctime(os.path.getmtime(file_path))

                # Print file details
                print(f"Timestamp: {timestamp}")
                print(f"File name: {file}")
                print(f"File size: {file_size} bytes")
                print(f"MD5 hash: {md5_hash}")
                print()

                # Query VirusTotal API
                api_key = "Insert API key"
                positives = scan_with_virustotal(md5_hash, api_key)
                print(f"Positives detected: {positives}")
                print()

                hits_found += 1

            files_searched += 1

    # Print search summary
    print(f"\nSearch complete.")
    print(f"Files searched: {files_searched}")
    print(f"Hits found: {hits_found}")

def calculate_md5(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        for chunk in iter(lambda: file.read(4096), b''):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def scan_with_virustotal(md5_hash, api_key):
    url = f"https://www.virustotal.com/api/v3/files/{md5_hash}"
    headers = {"x-apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["attributes"]["last_analysis_stats"]["malicious"]
    else:
        return None

def main():
    # Prompt user for file name and directory
    file_name = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    # Check the operating system
    if platform.system() == "Windows":
        command = f'dir /s /b "{os.path.join(directory, file_name)}"'
    else:
        command = f'find "{directory}" -name "{file_name}"'

    print("\nSearching files...\n")

    # Call the appropriate search function based on the operating system
    search_files(file_name, directory)

if __name__ == "__main__":
    main()
