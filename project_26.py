from concurrent.futures import ThreadPoolExecutor


def square(value):
    return value * value


def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(square, [2, 3, 4, 5]))
    print(results)


if __name__ == "__main__":
    main()
