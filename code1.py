# # Script: Ops 401 Class 2 Code Challenge
# # Joshua Phipps
# # 4/18/2023
# # Purpose: Uptime Sensor Tool Part 1 of 2
# Resource 1: https://www.w3schools.com/python/python_datetime.asp 
# Resource 2: https://github.com/codefellows/seattle-ops-401d6/blob/main/class-02/challenges/DEMO.md
#!/bin/bash

import os
import time
from datetime import datetime

ip_address = "8.8.8.8"




# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
# while True:
#     response = os.system("ping -c 1 " + ip_address)
#     if response == 0:
#         print(ip_address, "is up!")
#     else:
#         print(ip_address, "is down!")
#     time.sleep(2)

# Evaluate the response as either success or failure.


# while True:
#     now = datetime.now()
#     current_time = now.strftime("%Y-%m-%d %H:%M:%S")
#     response = os.system("ping -c 1 " + ip_address)
#     if response == 0:
#         print(current_time, ip_address, "is up!")
#     else:
#         print(current_time, ip_address, "is down!")
#     time.sleep(2)


# Assign success or failure to a status variable.

# while True:
#     now = datetime.now()
#     current_time = now.strftime("%Y-%m-%d %H:%M:%S")
#     response = os.system("ping -c 1 " + ip_address)
#     if response == 0:
#         ping_status = "Success"
#         print(current_time, ip_address, "is up!")
#     else:
#         ping_status = "Failure"
#         print(current_time, ip_address, "is down!")
#     print("Ping Status:", ping_status)
#     time.sleep(2)


# For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.

while True:
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(current_time, "Pinging", ip_address, "...")
    response = os.system("ping -c 1 " + ip_address)
    if response == 0:
        ping_status = "Success"
        print(current_time, ip_address, "is up!")
    else:
        ping_status = "Failure"
        print(current_time, ip_address, "is down!")
    print(current_time, "Ping Status:", ping_status)
    time.sleep(2)
