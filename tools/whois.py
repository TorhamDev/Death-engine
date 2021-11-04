
from .ping import ipfind
from ipwhois import IPWhois

def get_whois(target_ip):
    ip = ipfind(target_ip)
    obj = IPWhois(ip)
    return obj.lookup_whois()

