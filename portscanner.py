import ipaddress
import socket
from IPy import IP


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print('[+] Port {} is open'.format(port))
    except:
        print('[-] Port {} is closed'.format(port))


ipaddress = input('[+] Enter target to scan: ')

for port in range(75, 85):
    scan_port(ipaddress, port)
