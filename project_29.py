from time import perf_counter


def measure(operation):
    start = perf_counter()
    result = operation()
    return result, perf_counter() - start


def main():
    result, seconds = measure(lambda: sum(range(10000)))
    print("Result:", result)
    print(f"Elapsed: {seconds:.6f} seconds")


if __name__ == "__main__":
    main()
