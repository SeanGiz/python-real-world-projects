import hashlib
from pathlib import Path
from collections import defaultdict


def checksum(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def duplicates(directory):
    groups = defaultdict(list)
    for path in Path(directory).iterdir():
        if path.is_file():
            groups[checksum(path)].append(path.name)
    return [names for names in groups.values() if len(names) > 1]


def main():
    print(duplicates("."))


if __name__ == "__main__":
    main()
