from tools import whois, ping
import os, platform
from optparse import OptionParser





parser = OptionParser()


parser.add_option("-t", "--target", dest="target",
                metavar="url",help="define target")

parser.add_option("-w", "--whois", dest="whois",
                action="store_true", default=False,
                metavar="ip",help="get whois from target with IP ")



def banner():
    pass
    

def cls():
    if platform.uname()[0] == "Linux" :
        os.system("clear")
    else:
        os.system("cls")

def main():
    (options, args) = parser.parse_args()
    print(options)
    
    if not options.target:
        print("enter target or use -h for see help")
        exit

    if options.target:
        #target = str(options.target).replace("https://","").replace("http://","").replace("/","")
        #target_ip = ping.ping(target)
        print('hi')
        #print(target_ip)
    #print(whois.get_whois(target_ip))
    
    if options.whois:
        target_ip = str(options.whois).replace("https://","").replace("http://","").replace("/","")
        result = whois.get_whois(target_ip)
        
        for key, value in result.items():
            if key != 'nets':
                print(key , ' : ' , value)
            elif key == 'nets':
                nets = result.get('nets')[0]
                for key, value in nets.items():
                    print(key , ' : ' , value)
                    
                    
cls()

main()

