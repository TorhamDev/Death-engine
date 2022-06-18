from colorama import Fore
from .ping import ipfind
from ipwhois import IPWhois


def get_whois(target_ip):
    ip = ipfind(target_ip)
    obj = IPWhois(ip)
    result = obj.lookup_whois()
    for key, value in result.items():
        if key != 'nets':
            print(
                Fore.GREEN + '[+] ' + Fore.CYAN +
                key,
                ' : ',
                Fore.RESET,
                value
            )
        elif key == 'nets':
            nets_0 = result.get('nets')[0]

            for key, value in nets_0.items():
                print(
                    Fore.GREEN + '[+] ' + Fore.CYAN +
                    key,
                    ' : ',
                    Fore.RESET,
                    value
                )

            if 2 <= len(result.get('nets')):
                nets_1 = result.get('nets')[1]
                for key, value in nets_1.items():
                    print(
                        Fore.GREEN + '[+] ' + Fore.CYAN +
                        key,
                        ' : ',
                        Fore.RESET,
                        value
                    )
