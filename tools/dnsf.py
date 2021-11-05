import dns
import dns.resolver

def dnsl(hostname):
    host = hostname
    dkeys = ['A','AAAA','CNAME','MX','NS']
    redic = {}
    for records in dkeys:
        result = dns.resolver.resolve(host,records,raise_on_no_answer=False)
        rrst = str(result.rrset)
        rrset = rrst.splitlines()
        redic[records] = rrset
    return redic
