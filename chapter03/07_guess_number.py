import random

def get_user_guess():
    while True:
        try:
            return int(input("Please give an int: "))
        except ValueError:
            print("Invalid input. Please insert a valid integer")

def check_guess(secret, guess):
    if guess == secret:
        print("Bingo! Secret number:", secret)
        return True
    elif abs(secret - guess) <=5:
        print("Hot!")
    else:
        print("Cold")
    return False

def main():
    secret_number = random.randint(1, 10)
    MAX_TRIES = 5
    tries = 0

    while tries < MAX_TRIES:
        guess_number = get_user_guess()

        if check_guess(secret = secret_number, guess=guess_number):
            break
        tries += 1

        if tries == MAX_TRIES:
            print("You reaches the max number of tries.")

if __name__ == "__main__":
    main()