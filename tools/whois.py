from ipwhois import IPWhois

def get_whois():
    obj = IPWhois("site_ip")

    print(obj.lookup_whois())