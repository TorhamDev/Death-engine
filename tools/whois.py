from .ping import ping_clear
from ipwhois import IPWhois

def get_whois(ip):
    ip = ping_clear(ip)
    obj = IPWhois(ip)
    return(obj.lookup_whois())
