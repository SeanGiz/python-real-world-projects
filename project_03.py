import string


def check(password):
    rules = {
        "12+ characters": len(password) >= 12,
        "uppercase": any(c.isupper() for c in password),
        "lowercase": any(c.islower() for c in password),
        "digit": any(c.isdigit() for c in password),
        "symbol": any(c in string.punctuation for c in password),
    }
    return rules


def main():
    for rule, passed in check("LearnPython!2026").items():
        print(rule, "OK" if passed else "Missing")


if __name__ == "__main__":
    main()
