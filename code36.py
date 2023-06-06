#!/user/bin/python3
# Script: Ops 401 Class 36 Code Challenge
# Joshua Phipps
# 6/6/2023
# Purpose: Web Application Fingerprinting


import socket
import time

def netcat(addr, port):
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((addr, port))
    print("Netcat...")

    command = "nc " + addr + " " + str(port)
    print(command)
    socket1.sendall(command.encode())
    time.sleep(0.5)
    socket1.shutdown(socket.SHUT_WR)

    output = ""

    while True:
        data = socket1.recv(1024)
        if not data:
            break
        output += data.decode()

    print(output)
    socket1.close()

def telnet(addr, port):
    # Placeholder for telnet functionality
    return ""

def nmap(addr, port):
    # Placeholder for Nmap functionality
    return ""

def main():
    addr = input("Enter the target address: ")
    port = int(input("Enter the target port: "))

    netcat(addr, port)
    telnet(addr, port)
    nmap(addr, port)

if __name__ == "__main__":
    main()
