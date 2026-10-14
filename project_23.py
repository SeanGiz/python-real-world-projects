def retry(operation, attempts=3):
    if attempts < 1:
        raise ValueError("attempts must be positive")
    last_error = None
    for _ in range(attempts):
        try:
            return operation()
        except RuntimeError as exc:
            last_error = exc
    raise last_error


def main():
    state = {"tries": 0}
    def unstable():
        state["tries"] += 1
        if state["tries"] < 3:
            raise RuntimeError("Temporary issue")
        return "Success"
    print(retry(unstable))


if __name__ == "__main__":
    main()
