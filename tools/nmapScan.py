import os
from platform import uname
from colorama import Fore


def nmapScanner(target):
    if uname()[0] == "Linux":
        print(Fore.GREEN+"[SUDO] "+Fore.RESET)
        os.system(f"sudo nmap -v -sS -sV -sC -A -O {target}")
        print(Fore.RED+"[Done]"+Fore.RESET)
    else:
        os.system(f"nmap -v -sS -sV -sC -A -O {target}")
