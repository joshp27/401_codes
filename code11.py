#!/user/bin/python3
# Script: Ops 401 Class 11 Code Challenge
# Joshua Phipps
# 5/1/2023
# Purpose: Network Security Tool with Scapy Part 1 of 3


#!/user/bin/python3
from scapy.all import*

# Define the host IP and port range to scan
host = "scanme.nmap.org"
port_range = [22, 23, 80, 443, 3389]

# Define the TCP Port Range Scanner function
def tcp_port_scanner(host, port):
    # Send SYN packet and wait for response
    syn_packet = IP(dst=host) / TCP(dport=port, flags="S")
    response = sr1(syn_packet, timeout=1, verbose=0)
    
    # Check the response flags to determine if the port is open, closed or filtered
    if response is None:
        print(f"Port {port} is filtered or host is down")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        # Send RST packet to close the open connection
        rst_packet = IP(dst=host) / TCP(dport=port, flags="AR")
        send(rst_packet, verbose=0)
        print(f"Port {port} is open")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
        print(f"Port {port} is closed")
    else:
        print(f"Port {port} is filtered or host is down")

# Iterate over the port range and call the TCP Port Range Scanner function for each port
for port in port_range:
    tcp_port_scanner(host, port)

