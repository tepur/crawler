from urllib.parse import urlparse
from crawler import Crawler

class CountWordCrawler(Crawler):
    def __init__(self, word_to_count, visit_limit=100):
        super().__init__()
        self.word_to_count = word_to_count
        self.word_counter = 0
        self.pages_left = visit_limit
        self.base_url_netloc = "";

    def init_crawler(self, base_url):
        self.base_url_netloc = urlparse(base_url).netloc

    def process_data(self, data, url):
        for line in data:
            self.word_counter += line.strip().split(' ').count(self.word_to_count)

    def filter_links(self, links):
        filtered_links = []
        for link in links:
            parsed_link = urlparse(link)
            if parsed_link.netloc == self.base_url_netloc:
                filtered_links.append(link)

        return filtered_links
    def update(self):
        self.pages_left -= 1
    def is_ended(self):
        return self.pages_left <= 0
    def value_to_return(self):
        return self.word_counter

if __name__ == "__main__":
    crawler = CountWordCrawler("word")
    word_occurencies = crawler.crawl("your_address_goes_here")
    print("Word occurencies: {}".format(word_occurencies))
