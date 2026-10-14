from collections import Counter

LINES = [
    "INFO Application started",
    "WARNING Disk nearly full",
    "ERROR Save failed",
    "ERROR Connection failed",
]


def count_levels(lines):
    levels = (line.split(maxsplit=1)[0] for line in lines if line)
    return Counter(levels)


def main():
    print(dict(count_levels(LINES)))


if __name__ == "__main__":
    main()
