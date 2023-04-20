# Script: Ops 401 Class 3 Code Challenge
# Joshua Phipps
# 4/19/2023
# Purpose: Uptime Sensor Tool Part 2 of 2

import os
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

email = input("Please enter your email address: ")
password = input("Please enter your email password: ")

ip_address = "8.8.8.8"
status = "up"

while True:
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(current_time, "Pinging", ip_address, "...")
    response = os.system("ping -c 1 " + ip_address)
    if response == 0 and status == "down":
        status = "up"
        message = MIMEText("Host status changed from down to up at " + current_time)
        message['Subject'] = "Host Status Changed"
        message['From'] = email
        message['To'] = email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email, password)
            smtp.sendmail(email, email, message.as_string())
        print(current_time, ip_address, "is up!")
    elif response != 0 and status == "up":
        status = "down"
        message = MIMEText("Host status changed from up to down at " + current_time)
        message['Subject'] = "Host Status Changed"
        message['From'] = email
        message['To'] = email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email, password)
            smtp.sendmail(email, email, message.as_string())
        print(current_time, ip_address, "is down!")
    else:
        print(current_time, ip_address, "is", status)
    time.sleep(2)