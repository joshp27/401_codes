
#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: This script scans a given URL for XSS vulnerabilities by detecting forms and submitting them with a crafted payload.
# Date:        6/8/2023
# Modified by: Joshua Phipps

### TODO: Install requests bs4 before executing this in Python3

# Import libraries
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### This function retrieves all the forms present on a given URL by parsing the HTML content using BeautifulSoup.
### It returns a list of all the form elements found.
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### This function retrieves the details of a specific form, including its action (URL where it submits the data),
### method (GET or POST), and the input fields it contains.
### It returns a dictionary with the form details.
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### This function submits a form with a specific value for a vulnerable field.
### It constructs the URL or data payload based on the form details and submits it using the appropriate method (GET or POST).
### It returns the response object received from the server.
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### This function scans a given URL for XSS vulnerabilities by detecting forms and submitting them with a crafted payload.
### It prints the number of forms detected and if a vulnerability is found, it prints the form details.
### It returns a boolean value indicating whether any XSS vulnerability was detected.
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = '<script>alert("XSS Vulnerability")</script>'
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### The main function prompts the user to enter a URL to test for XSS vulnerabilities.
### It calls the scan_xss function to perform the scanning and prints the result.
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### TODO: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### TODO: Test this script against one XSS-positive target and one XSS-negative target
### TODO: https://xss-game.appspot.com/level1/frame POSITIVE
## http://dvwa.local/login.php NEGATIVE
