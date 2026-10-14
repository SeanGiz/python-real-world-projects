QUESTIONS = [
    ("Python list literal?", "[]"),
    ("Keyword to define a function?", "def"),
    ("Result of 2 ** 3?", "8"),
]


def grade(answers):
    return sum(answer.strip().lower() == correct.lower()
               for (_, correct), answer in zip(QUESTIONS, answers))


def main():
    answers = [input(question + " ") for question, _ in QUESTIONS]
    print(f"Score: {grade(answers)}/{len(QUESTIONS)}")


if __name__ == "__main__":
    main()
