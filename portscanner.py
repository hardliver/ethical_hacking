import ipaddress
import socket
from IPy import IP

ipaddress = input('[+] Enter target to scan: ')
port = 80

try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print('[+] Port 80 is opened')
except:
    print('[-] Port 80 is closed')
