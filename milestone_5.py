import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
            # Check if all unique letters have been guessed
            if self.num_letters == 0:
                print("Congratulations. You won the game!")
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            # Check if player is out of lives
            if self.num_lives == 0:
                print("You lost!")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess) == 1 and guess.isalpha():
                if guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.list_of_guesses.append(guess)
                    self.check_guess(guess)
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    # Main game loop
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_for_input()

# List of words for the game
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Start the game
play_game(word_list)
