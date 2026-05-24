import random
secret_number = random.randint(1,100)
print("Welcome to number guessing game:")
while True:
    guess = int(input("Enter your guess:"))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct")
        break