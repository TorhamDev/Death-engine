from tools import whois, ping, check_site, dnsf, googledork
import os, platform
from optparse import OptionParser
from colorama import Fore




parser = OptionParser()


parser.add_option("-t", "--target", dest="target",
                metavar="url",help="define target")

parser.add_option("-w", "--whois", dest="whois",
                action="store_true", default=False,
                metavar="ip",help="Target whois lookup")

parser.add_option("-d", "--dns", dest="dns",
                action="store_true", default=False,
                metavar="ip",help="Dns lookup")

parser.add_option("-D", "--Dork", dest="dork",
                action="store_true", default=False,
                help="Google dorking for target data")


def banner():
    '''
    start banner
    
    '''

    banner = Fore.RED+'''
                      ,____
                      |---.\\
              ___     |    `
             / .-\  ./=)
            |  |"|_/\/|
            ;  |-;| /_|
           / \_| |/ \ |
          /      \/\( |
          |   /  |` ) |
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /\n'''+Fore.GREEN+'''
  ▓█████▄ ▓█████  ▄▄▄      ▄▄▄█████▓ ██░ ██             ▓█████  ███▄    █   ▄████  ██▓ ███▄    █ ▓█████ 
  ▒██▀ ██▌▓█   ▀ ▒████▄    ▓  ██▒ ▓▒▓██░ ██▒            ▓█   ▀  ██ ▀█   █  ██▒ ▀█▒▓██▒ ██ ▀█   █ ▓█   ▀ 
  ░██   █▌▒███   ▒██  ▀█▄  ▒ ▓██░ ▒░▒██▀▀██░            ▒███   ▓██  ▀█ ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒▒███   
  ░▓█▄   ▌▒▓█  ▄ ░██▄▄▄▄██ ░ ▓██▓ ░ ░▓█ ░██             ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█  ██▓░██░▓██▒  ▐▌██▒▒▓█  ▄ 
  ░▒████▓ ░▒████▒ ▓█   ▓██▒  ▒██▒ ░ ░▓█▒░██▓            ░▒████▒▒██░   ▓██░░▒▓███▀▒░██░▒██░   ▓██░░▒████▒
   ▒▒▓  ▒ ░░ ▒░ ░ ▒▒   ▓▒█░  ▒ ░░    ▒ ░░▒░▒            ░░ ▒░ ░░ ▒░   ▒ ▒  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░
   ░ ▒  ▒  ░ ░  ░  ▒   ▒▒ ░    ░     ▒ ░▒░ ░             ░ ░  ░░ ░░   ░ ▒░  ░   ░  ▒ ░░ ░░   ░ ▒░ ░ ░  ░
   ░ ░  ░    ░     ░   ▒     ░       ░  ░░ ░               ░      ░   ░ ░ ░ ░   ░  ▒ ░   ░   ░ ░    ░   
     ░       ░  ░      ░  ░          ░  ░  ░               ░  ░         ░       ░  ░           ░    ░  ░
   ░ 
   '''+Fore.LIGHTBLUE_EX+'''
    ▣ Created By '''+Fore.YELLOW+''': TorhamDev and psyk3r '''+Fore.LIGHTBLUE_EX+'''

    ▣ Version : '''+Fore.YELLOW+'''0.1
    '''

    
    print(banner+Fore.RESET)
    



def cls():
    if platform.uname()[0] == "Linux" :
        os.system("clear")
    else:
        os.system("cls")


def main():

    # start banner
    banner()

    (options, args) = parser.parse_args()
    
    # if target not define
    if not options.target:
        print(Fore.GREEN +'[+] ' + Fore.CYAN+"Enter Target Or Use "+Fore.RED+"--help "+Fore.CYAN+"to see help page"+ Fore.RESET)
        exit()

    if options.target:
        
        target = str(options.target).replace("https://","").replace("http://","").replace("/","")

        # if target not up
        if not check_site.site_is_up(target):
            print("target not available")
            exit()

        # if target up
        else:
            print("⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞")
            target_ip = ping.ipfind(target)
            print(Fore.GREEN+"Target = "+ Fore.RESET + target + "\n ")
            print(Fore.GREEN+"Target Ip = "+ Fore.RESET + target_ip + "\n ")

    
    if options.whois:
        print(Fore.GREEN+'''
            =======|''' + Fore.RED+''' Get Whois ''' +Fore.GREEN+'''|=======
        '''+Fore.RESET.title())
        
        
        result = whois.get_whois(target)
        for key, value in result.items():
            if key != 'nets':
                print(Fore.GREEN +'[+] ' + Fore.CYAN + key , ' : ' , Fore.RESET , value)
            elif key == 'nets':
                nets_0 = result.get('nets')[0]
                
                for key, value in nets_0.items():
                    print(Fore.GREEN +'[+] ' + Fore.CYAN + key , ' : ' , Fore.RESET , value)
                
                if 2 <= len(result.get('nets')):
                    nets_1 = result.get('nets')[1]                    
                    for key, value in nets_1.items():
                        print(Fore.GREEN +'[+] ' + Fore.CYAN + key , ' : ' , Fore.RESET , value)
                
                else:
                    continue
        
        
    if options.dns:
        print(Fore.GREEN+'''
            =======|''' + Fore.RED+''' Dns lookup ''' +Fore.GREEN+'''|=======
        '''+Fore.RESET.title())
        result = dnsf.dnsl(target)
        for key, value in result.items():
            key = str(key)
            print(Fore.GREEN + '[+] ' + Fore.CYAN + key + ' :' + Fore.RESET)
            for rec in value:
                print(str(rec))

    
    if options.dork:
        print(Fore.RED+'''
            =======|''' + Fore.GREEN +''' Google dork ''' + Fore.RED +'''|=======
        '''+Fore.RESET.title())
        googledork.search(target=target)

                  
cls()

main()

