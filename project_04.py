def kilometers_to_miles(km):
    return km * 0.621371


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def main():
    print(f"10 km = {kilometers_to_miles(10):.2f} miles")
    print(f"20 C = {celsius_to_fahrenheit(20):.1f} F")


if __name__ == "__main__":
    main()
