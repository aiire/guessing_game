import random

MIN_GUESS = 1
MAX_GUESS = 100

MAX_TRIES = 10

player_wins = 0
computer_wins = 0
match_round = 1

line_seperator_thing = "-" * 50
print(line_seperator_thing)
print("GUESS THE NUMBER")
print(line_seperator_thing)

YES = "y"
NO = "n"

def yes_no(prompt):
    while True:
        answer = input(f'{prompt} ({YES}/{NO}): ').lower().strip()
        if answer in [YES, NO]:
            return answer == YES


while True:
    magic_number = random.randint(MIN_GUESS, MAX_GUESS)
    tries_left = MAX_TRIES
    guesses = []
    player_won = False

    print(line_seperator_thing)
    print(f"ROUND {match_round}")
    print(line_seperator_thing)
    
    print(f"\nI'm thinking of a number between {MIN_GUESS} to {MAX_GUESS}.\nYou can try up to {MAX_TRIES} times to guess correctly.")

    while tries_left > 0:
        if len(guesses) > 0:
            print("You've already guessed the following numbers: ")
            print(guesses)
        
        while True:
            try:
                guess = int(input("\nEnter your guess: "))
                break
            except:
                print("That's not a number...")
        
        if guess < MIN_GUESS or guess > MAX_GUESS:
            print(f"Number is out of range: [{MIN_GUESS}, {MAX_GUESS}]")
            continue
        
        if guess in guesses:
            continue
        
        if guess == magic_number:
            player_won = True
            break

        guesses.append(guess)
        tries_left -= 1

        if tries_left > 0:
            print(f"Wrong. You have {tries_left} {"tries" if tries_left > 1 else "try"} left.")
            print(f"Hint: Too {"high" if guess > magic_number else "low"}!")

    print()

    if player_won:
        player_wins += 1
        print("Correct! You win!")
        if tries_left < MAX_TRIES:
            print(f"It took you {MAX_TRIES - tries_left} out of {MAX_TRIES} attempts to get it right!")
    else:
        computer_wins += 1
        print("Out of tries! You lose...")
        print(f"The number was {magic_number}!")
    
    print()
    print(f"SCORE: {player_wins}-{computer_wins}")
    print()

    if not yes_no("Do you want to play again?"):
        if yes_no("Are you sure?") and yes_no("Are you sure you're sure?"):
            print()
            if not player_won and player_wins == 0 and match_round >= 3: 
                print("GG, lmk when you're ready to win")
            elif player_won and computer_wins == 0 and match_round >= 3:
                print("o7") # rare case
            else:
                print("gg")
            break
    
    match_round += 1
