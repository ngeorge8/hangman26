import random

# Define the Hangman class to encapsulate the logic for the game
class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Randomly select a word from the word list
        self.word = random.choice(word_list)
        # Create a list of underscores representing the unguessed letters of the word
        self.word_guessed = ["_" for _ in self.word]
        # Count the number of unique letters in the word
        self.num_letters = len(set(self.word))
        # Initialise the number of lives (chances) the player has
        self.num_lives = num_lives
        # Store the word list (not actively used in the game logic)
        self.word_list = word_list
        # Keep track of all letters guessed by the player
        self.list_of_guesses = []

    # Method to check whether the player's guess is correct or incorrect
    def check_guess(self, guess):
        # Convert the guessed letter to lowercase for consistency
        guess = guess.lower()
        
        # If the guessed letter is in the word
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            # Update the word_guessed list by replacing underscores with the correct letter
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            # Decrease the count of unique letters left to guess
            self.num_letters -= 1
            # Check if all unique letters have been guessed
            if self.num_letters == 0:
                print("Congratulations. You won the game!")
        else:
            # Decrease the number of lives if the guess is incorrect
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            # Check if the player has run out of lives
            if self.num_lives == 0:
                print("You lost!")

    # Method to handle user input for guessing letters
    def ask_for_input(self):
        while True:  # Loop until valid input is provided
            guess = input("Guess a letter: ")
            
            # Check if the input is a single alphabetical character
            if len(guess) == 1 and guess.isalpha():
                # Check if the player has already guessed this letter
                if guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    # Add the letter to the list of guessed letters
                    self.list_of_guesses.append(guess)
                    # Check if the guess is correct or incorrect
                    self.check_guess(guess)
                break  # Exit the loop after processing the guess
            else:
                # Prompt the player to enter a valid input if the input is invalid
                print("Invalid letter. Please, enter a single alphabetical character.")
            
            # Display the current state of the guessed word
            self.display_word()

    # Method to display the current guessed word
    def display_word(self):
        print("Current word: " + " ".join(self.word_guessed))

# Function to run the game
def play_game(word_list):
    # Initialise the number of lives the player starts with
    num_lives = 5
    # Create an instance of the Hangman class, passing the word list and number of lives
    game = Hangman(word_list, num_lives)

    # Main game loop: continue until the player runs out of lives or guesses the word
    while game.num_lives > 0 and game.num_letters > 0:
        # Display the current state of the guessed word (underscores and correctly guessed letters)
        game.display_word()
        # Ask the player to input a letter and process their guess
        game.ask_for_input()

# Define a list of words for the game
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Start the game by calling the play_game function
play_game(word_list)
