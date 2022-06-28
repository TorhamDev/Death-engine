from tools import (
    whois,
    ping,
    check_site,
    dnsf,
    googledork,
    nmapScan,
    subdom,
    wappalyzer,
)
from webcrawler import crawler
import os
import platform
from optparse import OptionParser
from colorama import Fore


parser = OptionParser()


parser.add_option(
    "-t",
    "--target",
    dest="target",
    metavar="url",
    help="define target"
)

parser.add_option(
    "-w",
    "--whois",
    dest="whois",
    action="store_true",
    default=False,
    metavar="ip",
    help="Target whois lookup"
)

parser.add_option(
    "-d",
    "--dns",
    dest="dns",
    action="store_true",
    default=False,
    metavar="ip",
    help="Dns lookup"
)

parser.add_option(
    "-D",
    "--Dork",
    dest="dork",
    action="store_true",
    default=False,
    help="Google dorking for target data"
)

parser.add_option(
    "-c",
    "--crawl",
    dest="crawl",
    action="store_true",
    default=False,
    help="Crawl and save website directories"
)

parser.add_option(
    "-n",
    "--nmap",
    dest="nmap",
    action="store_true",
    default=False,
    help="Comprehensive Scan"
)

parser.add_option(
    '-s',
    '--subdom',
    dest="subdoms",
    action="store_true",
    default=False,
    help="Scaning and find target subdomains"
)
parser.add_option(
    '-W',
    '--wappalyzer',
    dest="wappalyzer",
    action="store_true",
    default=False,
    help="Scaning and find target site tech with wappalyzer scaner"
)


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
    if platform.uname()[0] == "Linux":
        os.system("clear")
    else:
        os.system("cls")


def main():

    # start banner
    banner()

    (options, args) = parser.parse_args()

    # if target not define
    if not options.target:
        print(
            Fore.GREEN + '[+] ' + Fore.CYAN+"Enter Target Or Use " +
            Fore.RED+"--help "+Fore.CYAN+"to see help page" + Fore.RESET
        )
        exit()

    if options.target:

        target = str(options.target).replace(
            "https://", "").replace("http://", "").replace("/", "")

        # if target not up
        if not check_site.site_is_up(target):
            print(
                "\n\n HINT: sample targets => "+Fore.RED +
                "site.com / google.com / domain.com / sample.com"+Fore.RESET
            )

            exit()

        # if target up
        else:
            print("⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞⬞")
            target_ip = ping.ipfind(target)
            print(Fore.GREEN+"Target = " + Fore.RESET + target + "\n ")
            print(Fore.GREEN+"Target Ip = " + Fore.RESET + target_ip + "\n ")

    if options.whois:
        print(
            Fore.RED+'''
            =======|''' + Fore.GREEN+''' WHOIS lookup ''' + Fore.RED+'''|=======
        '''+Fore.RESET.title()
        )

        try:
            whois.get_whois(target)
        except:
            print(Fore.RESET + 'An error occured')
            exit()

    if options.dns:
        print(
            Fore.RED+'''
            =======|''' + Fore.GREEN+''' DNS lookup ''' + Fore.RED+'''|=======
        '''+Fore.RESET.title()
        )

        try:
            dnsf.dnsl(target)
        except:
            print('An error occured')

    if options.dork:
        print(
            Fore.RED+'''
            =======|''' + Fore.GREEN + ''' Google dork ''' + Fore.RED + '''|=======
        '''+Fore.RESET.title()
        )
        googledork.search(target=target)

    if options.crawl:
        print(
            Fore.RED+'''
            =======|''' + Fore.GREEN + ''' Crawl ''' + Fore.RED + '''|=======
        '''+Fore.RESET.title()+Fore.RESET
        )
        target = 'https://' + target

        crawler.crawl(target)

    if options.nmap:
        print(
            Fore.RED+'''
            =======|''' + Fore.GREEN + ''' Nmap Scan ''' + Fore.RED + '''|=======
        '''+Fore.RESET.title()+Fore.RESET
        )
        nmapScan.nmapScanner(target_ip)

    if options.subdoms:
        print(
            Fore.RED+'''
            =======|''' + Fore.GREEN + ''' Subdomain Scan ''' + Fore.RED + '''|=======
        '''+Fore.RESET.title()+Fore.RESET
        )
        subdom.run_subdomains(target=target)



    if options.wappalyzer:
        print(
            Fore.RED+'''
            =======|''' + Fore.GREEN + ''' Wappalyzer Scan ''' + Fore.RED + '''|=======
        '''+Fore.RESET.title()+Fore.RESET
        )
        wappalyzer.wappalyzer_scan(target)


cls()

main()
