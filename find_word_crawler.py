from crawler import Crawler

class FindWordCrawler(Crawler):
    def __init__(self, word_to_find):
        super().__init__()
        self.word_to_find = word_to_find
        self.word_found = False

    def process_data(self, data, url):
        print(self.visited_urls)
        for line in data:
            if self.word_to_find in line:
                self.word_found = True
                print("Word found on page: {}, line: {}".format(url, line.strip()))
                break
    def is_ended(self):
        return self.word_found