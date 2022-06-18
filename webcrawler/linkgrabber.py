from html.parser import HTMLParser
from urllib import parse


class LinkGrabber(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for(attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
        if tag == 'script':
            for(attribute, value) in attrs:
                if attribute == 'src':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
        if tag == 'link':
            for(attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
