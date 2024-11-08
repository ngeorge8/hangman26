# milestone_3.py

def is_valid_guess(guess):
    """Check if the input is a valid single alphabetical letter."""
    return len(guess) == 1 and guess.isalpha()

def ask_for_letter():
    """Continuously prompt the user for a letter and validate the input."""
    while True:
        guess = input("Enter a single letter: ")
        if is_valid_guess(guess):
            print("Good guess!")
            break  # Exit the loop if the guess is valid
        else:
            print("Oops! That is not a valid input. Please try again.")

if __name__ == "__main__":
    ask_for_letter()
