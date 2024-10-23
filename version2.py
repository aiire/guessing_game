import random 

magic_number = random.randint(1, 10)

print("Welcome to the Guessing Game!")
print()
print("I'm thinking of a number between 1 and 10.")

while True:
    guess = int(input("Enter your guess: "))

    if guess == magic_number:
        print("Correct! You win!")
        break
    else:
        print("Incorrect.")
        print()
