import random

magic_number = random.randint(1, 10)

print("Welcome to the Guessing Game!")
print()
print("I'm thinking of a number between 1 and 10.")

guess = int(input("Enter your guess: "))

if guess == magic_number:
    print("Correct! You win!")
else:
    print("Incorrect. You lose!")
    print(f"The number was {magic_number}.")
