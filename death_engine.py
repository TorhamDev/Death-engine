from tools import (
    whois,
    ping,
    check_site,
    dnsf,
    googledork,
    nmapScan,
    subdom,
    wappalyzer,
    info,
)
from webcrawler import crawler
import os
import platform
import datetime
import time
from optparse import OptionParser
from colorama import Fore
from banners import print_main_banner

from rich.console import Console
from rich import print
from rich.traceback import install
install(show_locals=True)


console = Console()
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
parser.add_option(
    '-I',
    '--info',
    dest="info",
    action="store_true",
    default=False,
    help="Get Death Engine Information"
)


def cls():
    if platform.uname()[0] == "Linux":
        os.system("clear")
    else:
        os.system("cls")


def main():

    start_scan_time = time.time()

    # start banner
    print_main_banner()

    (options, args) = parser.parse_args()

    if options.info:
        info.print_readme()

    # if target not define
    if not options.target:
        print(
            '[+] ' + "Enter Target Or Use " + "--help "+"to see help page"
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
            console.rule("[bold red]"+"death engine".title())
            target_ip = ping.ipfind(target)
            print("[bold gold3]Target [/bold gold3]: [white underline]" + target + "\n")
            print("[bold gold3]Target Ip [/bold gold3]: " + target_ip + "\n")

    if options.whois:
        console.rule("[bold yellow]"+"WHOIS lookup".title())

        try:
            whois.get_whois(target)
        except:
            print(Fore.RESET + 'An error occured')
            exit()

    if options.dns:
        console.rule("[bold yellow]"+"DNS lookup".title())

        try:
            dnsf.dnsl(target)
        except:
            print('An error occured')

    if options.dork:
        console.rule("[bold yellow]"+"Google dork".title())
        googledork.search(target=target)

    if options.crawl:
        console.rule("[bold yellow]"+"Crawl".title())
        target = 'https://' + target

        crawler.crawl(target)

    if options.nmap:
        console.rule("[bold yellow]"+"Nmap Scan".title())
        nmapScan.nmapScanner(target_ip)

    if options.subdoms:
        console.rule("[bold yellow]"+"Subdomain Scan".title())
        subdom.run_subdomains(target=target)

    if options.wappalyzer:
        console.rule("[bold yellow]"+"Wappalyzer Scan".title())
        wappalyzer.wappalyzer_scan(target)

   
    # scan time report
    console.rule("[bold yellow]"+"Scan time".title())
    time.sleep(70)
    end_scan_time = time.time()
    diff = int(end_scan_time - start_scan_time)
    minutes, seconds = divmod(diff, 60)
    hours, minutes = divmod(minutes, 60)


    print("[bold light_cyan1]start time[/bold light_cyan1]: " + str(start_scan_time))
    print("[bold light_cyan1]end time[/bold light_cyan1]: " + str(end_scan_time))

    print(f"\thours: {hours} & minutes: {minutes} & seconds: {seconds}")


cls()

main()
