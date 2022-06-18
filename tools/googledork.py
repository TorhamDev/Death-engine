from bs4 import BeautifulSoup
import requests
import re
import time
from random import choice
from os import listdir, getcwd
from os.path import isfile, join
from colorama import Fore
from urllib.parse import unquote


def random_useragent():

    useragent_list = open("./tools/useragents/useragent.txt")
    useragent_list = useragent_list.readlines()
    useragents = []
    [useragents.append(i) for i in useragent_list]
    useragent = choice(useragents)
    useragent = str(useragent).replace("\n", "")

    return(useragent)


def select_dorks_file():
    count = 0
    pwd = getcwd()
    dorks_path = join(pwd, "tools/google_dork")
    print(Fore.CYAN +
          "[*] Dorks path, you can add your dork files here : ".title(), dorks_path + '\n')
    dork_list = [f for f in listdir(dorks_path) if isfile(join(dorks_path, f))]
    dork_selected = ''
    for i in dork_list:
        print(Fore.RED + f"\t[{count}]"+Fore.RESET+" : "+Fore.BLUE+f"{i}")
        count += 1

    print(Fore.GREEN+"\n[*] Select a dork list".title())
    dork_selected = int(
        input(Fore.GREEN+"Enter Dork List Number: "+Fore.RESET))

    return(dork_list[dork_selected])


def search(target):
    dorks = open(f"./tools/google_dork/{select_dorks_file()}", 'rb')
    dorks = dorks.readlines()

    search_output = []
    # starting
    for search in dorks:
        # create dork for search
        search = search.decode()
        # add target in dork
        search = f"{search} site:{target}".replace("\n", "")

        param = {"q": search}

        headers = {
            'User-Agent': f'{random_useragent()}'
        }

        r = requests.get("https://google.com/search?q=",
                         params=param, headers=headers)

        soup = BeautifulSoup(r.content, "lxml")
        soup.prettify()

        link = soup.findAll("a")

        for link in soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
            result = re.split(":(?=http)", link["href"].replace("/url?q=", ""))
            for i in result:
                if "google.com" in i:
                    i = None

                if i == None:
                    pass

                else:
                    search_output.append(unquote(unquote(i)))

        time.sleep(6)

    if len(search_output) == 0:
        print(Fore.RED + "[-] No link founded\n\tYou may have been blocked by Google or the dork list may have not get a hit.".title() + Fore.RESET)

    else:
        for o in search_output:
            print(Fore.RED+"LINK : "+Fore.RESET, o)
