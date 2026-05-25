import random

def play_game():
    print("\n Number Guessing Game")

    # difficulty choose
    level = input("Choose difficulty (easy/hard): ").lower()

    if level == "easy":
        attempts = 10
    else:
        attempts = 5

    secret_number = random.randint(1, 100)

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print(" Too low")

        elif guess > secret_number:
            print(" Too high")

        else:
            print(" Correct! You win!")
            return

        attempts -= 1

    print(f" You lost! Number was {secret_number}")


# replay loop
while True:
    play_game()

    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print("Game Over")
        break