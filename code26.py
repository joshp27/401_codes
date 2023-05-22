#!/user/bin/python3
# Script: Ops 401 Class 26 Code Challenge
# Joshua Phipps
# 5/22/2023
# Purpose: Ops Challenge: Event Logging Tool Part 1 of 3


import logging
from scapy.all import *

# Configure logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

# Define the host IP and port range to scan
host = "scanme.nmap.org"
port_range = [22, 23, 80, 443, 3389]

# Define the TCP Port Range Scanner function
def tcp_port_scanner(host, port):
    try:
        # Send SYN packet and wait for response
        syn_packet = IP(dst=host) / TCP(dport=port, flags="S")
        response = sr1(syn_packet, timeout=1, verbose=0)

        # Check the response flags to determine if the port is open, closed, or filtered
        if response is None:
            logging.warning(f"Port {port} is filtered or host is down")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            # Send RST packet to close the open connection
            rst_packet = IP(dst=host) / TCP(dport=port, flags="AR")
            send(rst_packet, verbose=0)
            logging.info(f"Port {port} is open")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            logging.info(f"Port {port} is closed")
        else:
            logging.warning(f"Port {port} is filtered or host is down")
    except Exception as e:
        logging.error(f"An error occurred while scanning port {port}: {str(e)}")

# Iterate over the port range and call the TCP Port Range Scanner function for each port
for port in port_range:
    tcp_port_scanner(host, port)
