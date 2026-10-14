from urllib.parse import urlencode


def build_url(base, params):
    return base + "?" + urlencode(params)


def main():
    print(build_url("https://example.com/search",
                    {"q": "python projects", "page": 2}))


if __name__ == "__main__":
    main()
