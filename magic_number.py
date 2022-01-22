import random

MIN_NUMBER = 1
MAX_NUMBER = 10
MAX_TRIES = 3


def main():
    # print intro
    intro()

    # get random number
    magic_number = generate_random_number()

    # todo ask player for their number

    # todo compare number

    # todo if numbers are == player wins
    # todo else call ask player for their number


def intro():
    print("=" * 50, "MAGIC NUMBER", "=" * 50)
    print(f"There is a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess it?")
    print(f"You have {MAX_TRIES} tries.")


def generate_random_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


main()
