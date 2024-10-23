import random 

magic_number = random.randint(1, 10)

print("Welcome to the Guessing Game!")
print()

MAX_TRIES = 5
tries_left = MAX_TRIES

print(f"I'm thinking of a number between 1 and 10, and I'm giving you {tries_left} attempts to guess it!")

win = False

while tries_left > 0:
    guess = int(input("Enter your guess: "))

    if guess == magic_number:
        win = True
        break
    
    tries_left -= 1
    
    if tries_left == 1:
        print("Wrong again!")
        break
    else:
        print(f"Incorrect. You have {tries_left} {"tries" if tries_left != 1 else "try"} left.")
        print()

print()

if win:
    print("You win!")
    print(f"It took you {MAX_TRIES - tries_left} out of {MAX_TRIES} attempts to guess right!")
else:
    print("Better luck next time...")
    print("You lose!")
    print(f"The number was {magic_number}!")
