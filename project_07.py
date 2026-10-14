import re
from collections import Counter


def top_words(text, limit=5):
    words = re.findall(r"[a-z']+", text.lower())
    return Counter(words).most_common(limit)


def main():
    print(top_words("Python is fun. Python is practical!"))


if __name__ == "__main__":
    main()
