from tools import whois
import os, platform

banner()
ch = input()
if ch == '0':
    whois.get_whois()
elif ch == '1':
    cls()
    banner()
else:
    cls()
    banner()



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
