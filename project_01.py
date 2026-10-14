def total_per_person(bill, tip_percent, people):
    if bill < 0 or tip_percent < 0 or people < 1:
        raise ValueError("Invalid bill, tip, or party size")
    total = bill * (1 + tip_percent / 100)
    return round(total / people, 2)


def main():
    print(total_per_person(80, 15, 4))


if __name__ == "__main__":
    main()
