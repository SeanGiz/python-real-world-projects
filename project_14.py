from pathlib import Path


def inventory(directory):
    directory = Path(directory)
    result = []
    for path in sorted(directory.iterdir()):
        if path.is_file():
            result.append((path.name, path.stat().st_size))
    return result


def main():
    for filename, size in inventory("."):
        print(f"{filename}: {size} bytes")


if __name__ == "__main__":
    main()
