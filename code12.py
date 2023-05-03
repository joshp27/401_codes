#!/user/bin/python3
# Script: Ops 401 Class 11 Code Challenge
# Joshua Phipps
# 5/2/2023
# Purpose: Network Security Tool with Scapy Part 2 of 3




from scapy.all import*
import ipaddress

# Prompt user for mode choice
mode_choice = input("Enter '1' for TCP Port Range Scanner mode or '2' for ICMP Ping Sweep mode: ")

if mode_choice == "1":
    # TCP Port Range Scanner code
    host = input("Enter the host IP address to scan: ")
    port_range = input("Enter the port range to scan (e.g. '1-1000') or a specific set of ports (e.g. '80,443,8080'): ")
    ports = port_range.split(",")
    open_ports = []
    closed_ports = []

    try:
        ip_addr = ipaddress.ip_address(host)
    except ValueError:
        print("Invalid IP address entered.")
        exit()

    for port in ports:
        try:
            port = int(port)
        except ValueError:
            print("Invalid port range or set of ports entered.")
            continue

        # Send SYN packet
        packet = IP(dst=str(ip_addr))/TCP(sport=12345, dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)

        if response is None:
            print("Port " + str(port) + " is filtered and silently dropped.")
        elif response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:
                # Send RST packet to graciously close the open connection
                packet = IP(dst=str(ip_addr))/TCP(sport=12345, dport=port, flags="R")
                sr1(packet, timeout=1, verbose=0)
                print("Port " + str(port) + " is open.")
                open_ports.append(port)
            elif response.getlayer(TCP).flags == 0x14:
                print("Port " + str(port) + " is closed.")
                closed_ports.append(port)
            else:
                print("Port " + str(port) + " has an unknown response.")
        else:
            print("Port " + str(port) + " has an unknown response.")

    # Print summary
    print("Open ports: " + str(open_ports))
    print("Closed ports: " + str(closed_ports))

elif mode_choice == "2":
    # ICMP Ping Sweep mode code
    network_input = input("Enter the network address including CIDR block, for example '10.10.0.0/24': ")
    target_network = ipaddress.IPv4Network(network_input, strict=False)

    # Ping all addresses on the given network except for network address and broadcast address
    online_hosts = 0
    for host in target_network.hosts():
        if host != target_network.network_address and host != target_network.broadcast_address:
            response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
            if response is None:
                print(f"Host {str(host)} is down or unresponsive")
            elif response.type == 3 and response.code in [1, 2, 3, 9, 10, 13]:
                print(f"Host {str(host)} is actively blocking ICMP traffic")
            else:
                print(f"Host {str(host)} is responding")
                online_hosts += 1

    # Inform the user how many hosts are online
    print(f"Scan complete. {online_hosts} host(s) online.")

else:
    print("Invalid mode choice.")

