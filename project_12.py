import re

NOTES = {
    "python.md": "Learn Python lists and loops",
    "travel.md": "Plan trips and travel budgets",
    "work.md": "Write a Python report",
}


def find_notes(notes, query):
    tokens = set(re.findall(r"\w+", query.lower()))
    return [name for name, text in notes.items()
            if tokens.issubset(set(re.findall(r"\w+", text.lower())))]


def main():
    print(find_notes(NOTES, "Python"))


if __name__ == "__main__":
    main()
