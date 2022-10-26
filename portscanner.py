import socket
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('\n[-_0 Scanning Target] {}'.format(target))
    for port in range(1, 100):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print('[+] Port {} is open'.format(port))
    except:
        pass


targets = input('[+] Enter target\'s to scan: (split multiple targets with ,): ')
if ',' in targets:
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '))
else:
    scan(targets)
