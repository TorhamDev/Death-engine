from Wappalyzer import Wappalyzer, WebPage
from colorama import Fore

def wappalyzer_scan(target):
    webpage = WebPage.new_from_url(f'https://{target}')
    wappalyzer = Wappalyzer.latest()

    data = wappalyzer.analyze_with_versions_and_categories(webpage)

    for key, value in data.items():
        print(Fore.YELLOW+f"{key}:"+Fore.RESET)
        print(Fore.MAGENTA+f"\t Versions:\n")
        for version in value["versions"]:
            print(Fore.RED+f"\t\t{version}, ")
        
        print(Fore.MAGENTA+f"\tCategories:\n")
        for categorie in value['categories']:
            print(Fore.RED+f"\t\t{categorie}, ")
