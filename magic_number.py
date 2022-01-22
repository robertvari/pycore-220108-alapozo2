import random

MIN_NUMBER = 1
MAX_NUMBER = 10


def main():
    max_tries = 3

    # print intro
    intro(max_tries)

    # get random number
    magic_number = generate_random_number()

    # todo remove this!
    print(f"REMOVE THIS magic_number: {magic_number}")

    # ask player for his/her number
    player_number = get_player_number()

    # compare_numbers -> bool
    result = compare_numbers(magic_number, player_number)

    # while result == False do another round
    while not result:
        max_tries -= 1

        if max_tries == 0:
            print("You have no more tries :(")
            break

        player_number = get_player_number()
        result = compare_numbers(magic_number, player_number)

    # todo else call ask player for their number


def intro(max_tries):
    print("=" * 50, "MAGIC NUMBER", "=" * 50)
    print(f"There is a number between {MIN_NUMBER} and {MAX_NUMBER}. Can you guess it?")
    print(f"You have {max_tries} tries.")


def generate_random_number() -> str:
    return str(random.randint(MIN_NUMBER, MAX_NUMBER))


def get_player_number() -> str:
    result = input("What is your number?")
    # result = '5'

    # todo check if input is valid

    return result


def compare_numbers(magic_number, player_number):
    return magic_number == player_number


def end_game(magic_number, player_number):
    if magic_number == player_number:
        print(f"You win! My number was {magic_number}")
    else:
        print("Game over man....")


main()
