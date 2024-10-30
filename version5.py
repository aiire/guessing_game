import random 

MIN_GUESS = 1
MAX_GUESS = 100
magic_number = random.randint(MIN_GUESS, MAX_GUESS)

print("Welcome to the Guessing Game!")
print()

MAX_TRIES = 20
tries_left = MAX_TRIES
guesses = []

print(f"I'm thinking of a number between {MIN_GUESS} and {MAX_GUESS}, and I'm giving you {tries_left} attempts to guess it!")

win = False

while tries_left > 0:
    if len(guesses) > 0:
        print(f"You've already guessed: \n{guesses}")

    guess = int(input("Enter your guess: "))

    if guess in guesses:
        continue

    guesses.append(guess)

    if guess == magic_number:
        win = True
        break
    
    tries_left -= 1
    
    if tries_left == 1:
        print("Wrong again!")
        break
    else:
        print(f"Incorrect. You have {tries_left} {"tries" if tries_left != 1 else "try"} left.")
        print(f"Hint: Too {"high" if guess > magic_number else "low"}!")
        print()

if win:
    print("You win!")
    if tries_left < MAX_TRIES:
        print(f"It took you {MAX_TRIES - tries_left} out of {MAX_TRIES} attempts to guess right!")
else:
    print("Better luck next time...")
    print("You lose!")
    print(f"The number was {magic_number}!")
