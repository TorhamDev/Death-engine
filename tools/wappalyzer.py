from Wappalyzer import Wappalyzer, WebPage
from rich.console import Console
from json import dumps
from requests.exceptions import SSLError

console = Console()


def wappalyzer_scan(target):
    try:
        webpage = WebPage.new_from_url(f'https://{target}')
    except SSLError:
        webpage = WebPage.new_from_url(f'http://{target}')

    wappalyzer = Wappalyzer.latest()

    data = wappalyzer.analyze_with_versions_and_categories(webpage)

    console.print_json(dumps(data))
