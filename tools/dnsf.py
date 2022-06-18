import dns
import dns.resolver
from colorama import Fore


def dnsl(hostname):
    host = hostname
    dkeys = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'SOA']
    redic = {}
    for records in dkeys:
        result = dns.resolver.resolve(host, records, raise_on_no_answer=False)
        rrst = str(result.rrset)
        rrset = rrst.splitlines()
        print(Fore.GREEN + '[+]' + Fore.CYAN + records + Fore.RESET + '\n')
        for rec in rrset:
            print(rec)
        print('\n')
    return ''
