import requests
from .googledork import random_useragent
from colorama import Fore

def search(domain):
    two = [200,201,202,203,204,205,206,207,208,209,210]
    four = [400, 401, 402, 403, 405, 406, 407, 408, 409, 410]

    try:
        dlist = open('./conf/dirlist.txt').read().splitlines()
    except Exception as e:
        print('dirlist.txt file not found in conf folder!')
        print(e)
        quit()
        domain = 'http://' + domain + '/'
    for dir in dlist:
        headers = {
            'User-Agent': f'{random_useragent()}'
        }
        response = requests.get(domain + '/' + dir, headers=headers).status_code
        if response in two:
            print(Fore.GREEN + '[+] ' + domain + '/' + dir + Fore.RESET)
        elif response in four:
            print(Fore.RED + '[*] ' + domain + '/' + dir + Fore.RESET + " Blocked by Webserver/WAF")
        elif response == 404:
            pass
        else:
            pass
