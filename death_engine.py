from tools import whois
import os, platform

def banner():
    print(''' Death engine
    [0] Whois
    [1] none
    ''')
    
def cls():
    if platform.uname()[0] == "Linux" :
        os.system("clear")
    else:
        os.system("cls")

cls()
banner()
ch = input()
if ch == '0':
    ip = input('Enter domain ot ip address : ')
    print(whois.get_whois(ip))
    banner()
elif ch == '1':
    cls()
    banner()
else:
    cls()
    banner()

