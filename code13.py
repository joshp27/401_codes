#!/user/bin/python3
# Script: Ops 401 Class 13 Code Challenge
# Joshua Phipps
# 5/3/2023
# Purpose: Network Security Tool with Scapy Part 3 of 3

# Import libraries
import random
from scapy.all import ICMP, IP, sr1, sr, TCP
import sys
from ipaddress import IPv4Network


# TCP scan function
def tcpscan(host):
    port_range = [22, 23, 80, 443, 3389]
    # Sends SYN with random source port for each destination port
    for dst_port in port_range:
        src_port = random.randint(1025,65534)
        resp = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='S'),timeout=1,verbose=0)

        # Port filtered response if no flag received
        if resp is None:
            print(f"{host}:{dst_port} is filtered (silently dropped).")

        elif (resp.haslayer(TCP)):
            # Port open notification for 0x12 flag
            if (resp.getlayer(TCP).flags == 0x12):
                # Send a RST to close the connection
                send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),timeout=1,verbose=0)
                print(f"{host}:{dst_port} is open.")

            # Port closed notification for 0x14 flag
            elif (resp.getlayer(TCP).flags == 0x14):
                print(f"{host}:{dst_port} is closed.")

        elif (resp.haslayer(ICMP)):
            # Port filtered response for no flag received
            if (
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
            ):
                print(f"{host}:{dst_port} is filtered (silently dropped). ")


# Main function
def main():
    # Prompt user for IP address to target
    host = input("Enter IP Address to scan: ")

    # Send ICMP ping request, wait for reply
    resp = sr1(IP(dst=host)/ICMP(),timeout=1,verbose=0)

    if resp is None:
        print(f"{host} is down or not responding. ")

    elif (
        int(resp.getlayer(ICMP).type) == 3 and
        int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
    ):
        print(f"{host} is blocking ICMP traffic.")
    else:
        # Call port scan function if host is responsive to ICMP echo requests
        tcpscan(host)

    # Prompt user to continue scanning or exit
    while True:
        user_choice = input("Do you want to scan another IP address? (y/n) ")

        if user_choice.lower() == "y":
            main()
        elif user_choice.lower() == "n":
            sys.exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


# Start the program
if __name__ == "__main__":
    main()
