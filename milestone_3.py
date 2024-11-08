import random

# Define a list of possible words for the game
words_to_guess = ["apple", "banana", "cherry", "date", "elderberry"]

# Randomly choose a word from words_to_guess
chosen_word = random.choice(words_to_guess)

def validate_and_check_guess(player_guess):
    """Convert guess to lowercase, then check if it is in the chosen word."""
    player_guess = player_guess.lower()
    if player_guess in chosen_word:
        print(f"Good guess! '{player_guess}' is in the word.")
    else:
        print(f"Sorry, '{player_guess}' is not in the word. Try again.")

def get_player_input():
    """Prompt the player to guess a letter and validate their input."""
    while True:
        player_guess = input("Enter a single letter: ")
        if len(player_guess) == 1 and player_guess.isalpha():
            validate_and_check_guess(player_guess)
            break  # Exit loop on valid input
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Start the game by calling get_player_input
get_player_input()
