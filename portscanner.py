import ipaddress
import socket
from IPy import IP


def check_ip(ip):
    try:
        return IP(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print('[+] Port {} is open'.format(port))
    except:
        print('[-] Port {} is closed'.format(port))


ipaddress = input('[+] Enter target to scan: ')
converted_ip = check_ip(ipaddress)

for port in range(75, 85):
    scan_port(converted_ip, port)
