from .ping import ping
from ipwhois import IPWhois


def get_whois(ip):
    obj = IPWhois(ip)
    return(obj.lookup_whois())
