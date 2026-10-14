import json
from urllib.request import urlopen


def read_json(url):
    with urlopen(url, timeout=10) as response:
        if response.status != 200:
            raise RuntimeError("Unexpected HTTP status")
        return json.load(response)


def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        data = read_json(url)
        print(data.get("title", "No title"))
    except (OSError, ValueError) as exc:
        print("Request failed:", exc)


if __name__ == "__main__":
    main()
