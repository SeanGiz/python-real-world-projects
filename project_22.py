from html.parser import HTMLParser

class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            address = dict(attrs).get("href")
            if address:
                self.links.append(address)


def main():
    parser = LinkCollector()
    parser.feed('<a href="/about">About</a><a href="/help">Help</a>')
    print(parser.links)


if __name__ == "__main__":
    main()
