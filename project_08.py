import csv
from io import StringIO

DATA = "name,score\nMaya,91\nNoah,73\nAva,85\n"


def summarize(csv_text):
    rows = list(csv.DictReader(StringIO(csv_text)))
    scores = [int(row["score"]) for row in rows]
    average = sum(scores) / len(scores) if scores else 0
    return round(average, 2), len(scores)


def main():
    print(summarize(DATA))


if __name__ == "__main__":
    main()
