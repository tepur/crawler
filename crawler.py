import sys

from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import HTTPError

from abc import ABC

from crawler_parser import CrawlerParser

class Crawler(ABC):
    def __init__(self):
        self.parser = CrawlerParser()
        self.base_url = ""
        self.visited_urls = set()

    def crawl(self, url):
        links = [url] #TODO: change to queue to optimize
        base_url = url
        self.visited_urls = set()

        self.init_crawler(base_url)

        while links and not self.is_ended():
            cur_url = links[0]
            links = links[1:]

            if cur_url not in self.visited_urls:
                try:
                    response = urlopen(cur_url)
                    self.visited_urls.update([cur_url])

                    if 'text/html' in response.getheader('Content-type'):
                        html = response.read().decode()
                        data = self.parser.extract_data(html)
                        new_links = [urljoin(base_url, link)
                                     for link in
                                     self.parser.extract_links(html)]

                        self.process_data(data, cur_url)
                        new_links = self.filter_links(new_links)

                        links.extend(new_links)

                        self.update()
                    else:
                        sys.stderr.write("wrong Content-type")
                except HTTPError:
                    sys.stderr.write("error on {}".format(cur_url))

        return self.value_to_return()

    def init_crawler(self, base_url):
        pass
    def process_data(self, data, url):
        pass
    def update(self):
        pass
    def filter_links(self, links):
        return links
    def is_ended(self):
        return False
    def value_to_return(self):
        return None
