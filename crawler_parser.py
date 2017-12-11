from html.parser import HTMLParser

class CrawlerParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    self.links.append(value)

    def handle_data(self, data):
        self.data.append(data)

    def extract_data(self, html):
        self.data = []
        return self.data

    def extract_links(self, html):
        self.links = []
        self.feed(html)
        return self.links
