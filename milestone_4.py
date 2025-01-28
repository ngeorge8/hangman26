import random

# Define the Hangman class to encapsulate the game logic
class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Randomly select a word from the provided word list
        self.word = random.choice(word_list)
        # Create a list of underscores representing unguessed letters in the word
        self.word_guessed = ["_" for _ in self.word]
        # Calculate the number of unique letters in the word to track progress
        self.num_letters = len(set(self.word))
        # Set the initial number of lives (chances) the player has
        self.num_lives = num_lives
        # Store the word list for potential future use (though unused here)
        self.word_list = word_list
        # Maintain a list of letters already guessed by the player
        self.list_of_guesses = []

    # Define a method to check the validity of the player's guess
    def check_guess(self, guess):
        # Convert the guess to lowercase to ensure consistency
        guess = guess.lower()
        
        # Check if the guessed letter is in the word
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            # Replace underscores with the guessed letter in the correct positions
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            # Decrement the count of unique letters left to guess
            self.num_letters -= 1
        else:
            # Decrement the number of lives if the guess is incorrect
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    # Define a method to handle user input for guessing letters
    def ask_for_input(self):
    while True:  
        guess = input("Guess a letter: ")
        # Check input logic
        self.display_word()  # This is called after the guess is processed to show the current word state

            
            # Check if the input is valid (a single alphabetical character)
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            # Check if the letter has already been guessed
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Add the guess to the list of guessed letters
                self.list_of_guesses.append(guess)
                # Check if the guess is correct or incorrect
                self.check_guess(guess)
                break  # Exit the loop after a valid guess

# Sample usage of the Hangman class
word_list = ["apple", "banana", "cherry", "date", "elderberry"]  # List of words for the game
game = Hangman(word_list)  # Create an instance of the Hangman class
game.ask_for_input()  # Start the game by asking the player for input

