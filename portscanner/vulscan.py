import portscanner

target_ip = input('[+] * Enter target to scan for vulnerable open ports: ')
port_number = int(input('[+] * Enter amount of ports you want to scan(500 - first 500 ports): '))
vul_file = input('[+] * Enter path to the file with vulnerable softwares: ')
print('\n')

target = portscanner.PortScan(target_ip, port_number)
target.scan()

with open(vul_file, 'r') as file:
    for banner, port in zip(target.banners, target.open_ports):
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNERL " {} " ON PORT: {}'.format(banner, port))
