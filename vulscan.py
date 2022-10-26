import portscanner

target_ip = input('[+] * Enter target to scan for vulnerable open ports: ')
port_number = int(input('[+] * Enter amount of ports you want to scan(500 - first 500 ports): '))
vul_file = input('[+] * Enter path to the file with vulnerable softwares: ')
print('\n')

portscanner.scan(target_ip)
