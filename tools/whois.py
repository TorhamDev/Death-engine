from ipwhois import IPWhois

def get_whois():
    ip = input("Enter ip : ")
    obj = IPWhois(ip)

    print(obj.lookup_whois())
