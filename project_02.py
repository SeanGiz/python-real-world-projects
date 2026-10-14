import random


def play(secret=7, guesses=(4, 9, 7)):
    for attempt, guess in enumerate(guesses, 1):
        if guess == secret:
            return f"Won in {attempt} guesses"
        print("Higher" if guess < secret else "Lower")
    return "Out of guesses"


def main():
    secret = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Guess 1-10: "))
        except ValueError:
            print("Enter a whole number")
            continue
        if guess == secret:
            print("Correct!")
            break
        print("Higher" if guess < secret else "Lower")


if __name__ == "__main__":
    main()
