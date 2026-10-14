RECORDS = [
    {"name": " maya ", "score": 85},
    {"name": "NOAH", "score": 59},
    {"name": "Ava", "score": 93},
]


def pipeline(records):
    cleaned = ((row["name"].strip().title(), row["score"])
               for row in records)
    return sorted((name, score) for name, score in cleaned
                  if score >= 60)


def main():
    print(pipeline(RECORDS))


if __name__ == "__main__":
    main()
