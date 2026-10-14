from datetime import date, timedelta


def schedule(start_date, every_days, count):
    if every_days <= 0 or count < 0:
        raise ValueError("Invalid scheduling arguments")
    return [start_date + timedelta(days=i * every_days)
            for i in range(count)]


def main():
    for day in schedule(date(2026, 10, 1), 7, 3):
        print(day.isoformat())


if __name__ == "__main__":
    main()
