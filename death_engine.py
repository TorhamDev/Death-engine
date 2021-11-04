from tools import whois, ping, check_site
import os, platform
from optparse import OptionParser
from colorama import Fore




parser = OptionParser()


parser.add_option("-t", "--target", dest="target",
                metavar="url",help="define target")

parser.add_option("-w", "--whois", dest="whois",
                action="store_true", default=False,
                metavar="ip",help="get whois from target with IP ")



def banner():
    print(Fore.GREEN+"DEATH ENGINE"+Fore.RESET)
    

def cls():
    if platform.uname()[0] == "Linux" :
        os.system("clear")
    else:
        os.system("cls")


def main():

    # start banner
    banner()

    (options, args) = parser.parse_args()
    print(options)
    
    # if target not define
    if not options.target:
        print("enter target or use -h for see help")
        exit()

    if options.target:
        
        target = str(options.target).replace("https://","").replace("http://","").replace("/","")

        # if target not up
        if not check_site.site_is_up(target):
            print("target not available")
            exit()

        # if target up
        else:
            target_ip = ping.ipfind(target)
            print(Fore.GREEN+"Target Ip = "+ Fore.RESET + target_ip + "\n ")

    
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

