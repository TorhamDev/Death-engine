from tools import whois
import os, platform

def banner():
    print('''Death engine
    [0] Whois
    [1] none
    ''')
    
def cls():
    if platform.uname()[0] == "Linux" :
        os.system("clear")
    else:
        os.system("cls")

def mainm():
    banner()
    ch = input()
    cls()
    if ch == '0':
        ip = input('Enter domain ot ip address : ')
        print(whois.get_whois(ip))
        mainm()
    
    elif ch == '1':
        cls()
        mainm()
    
    else:
        cls()
        mainm()
cls()
mainm()


