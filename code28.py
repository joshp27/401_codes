#!/user/bin/python3
# Script: Ops 401 Class 28 Code Challenge
# Joshua Phipps
# 5/24/2023
# Purpose: Ops Challenge: Event Logging Tool Part 3 of 3

import logging
from logging.handlers import RotatingFileHandler
import sys
from scapy.all import *
# Configure logging with log rotation
log_file = 'log.txt'
max_log_size = 500  # 1 MB
backup_count = 2  # Number of backup log files to keep
# Create a rotating file handler for log rotation
log_file_handler = RotatingFileHandler(log_file, maxBytes=max_log_size, backupCount=backup_count)
log_file_handler.setLevel(logging.DEBUG)
log_file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
# Create a stream handler for console output
log_stream_handler = logging.StreamHandler(sys.stdout)
log_stream_handler.setLevel(logging.INFO)
log_stream_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
# Create a logger and add the log handlers
logger = logging.getLogger()
logger.addHandler(log_file_handler)
logger.addHandler(log_stream_handler)
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
            logger.warning(f"Port {port} is filtered or host is down")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            # Send RST packet to close the open connection
            rst_packet = IP(dst=host) / TCP(dport=port, flags="AR")
            send(rst_packet, verbose=0)
            logger.info(f"Port {port} is open")
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
            logger.info(f"Port {port} is closed")
        else:
            logger.warning(f"Port {port} is filtered or host is down")
    except Exception as e:
        logger.error(f"An error occurred while scanning port {port}: {str(e)}")
# Iterate over the port range and call the TCP Port Range Scanner function for each port
for port in port_range:
    tcp_port_scanner(host, port)