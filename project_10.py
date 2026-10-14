from collections import defaultdict

EXPENSES = [
    ("food", 12.5), ("travel", 25.0),
    ("food", 9.5), ("books", 18.0),
]


def totals_by_category(expenses):
    totals = defaultdict(float)
    for category, amount in expenses:
        totals[category] += amount
    return dict(sorted(totals.items()))


def main():
    for category, total in totals_by_category(EXPENSES).items():
        print(f"{category}: {total:.2f}")


if __name__ == "__main__":
    main()
