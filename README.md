# Hangman Project 

# Project Description
This project aims to create a game of hangman. Hangman is a game where the player has to guess a secret word by guessing a different letter at every go, with a limited life. The player wins if the word is guessed before the lives are exhausted, and a loss occurs if the word is not guessed within the life limit.

## Hangman class: Attributes
A Hangman class has been created with five attributes
- `num_lives`: Number of lives for user
- `word_list`: List of words the computer will randomly choose from
- `word`: Word chosen by computer from word_list 
- `word_guessed`: Includes the letters of the word guessed correctly by the user so far
- `num_letters` which is the number of unique leters in the word
- `list_of_guesses`:  Records all letter guesses made by user so far

## Hangman class: Methods
The Hangman class also has two methods. Both methods also update value of some attributes once run
- `ask_for_input`: This asks the user for input (their guess of the letter). It validates the input.
- `check_guess`: This checks whether the letter is part of the word


# Technologies Used
Python: The project is built with Python and utilizes core libraries, including random for selecting random words.
# Getting Started
  # Prerequisites
You must have python installed 
# Installation
Clone this repository:
bash
Copy code
git clone https://github.com/ngeorge8/hangman26.git
cd hangman26
No additional libraries are required as this project only uses standard Python modules.
# Running the Game
To start the game, run the milestone_5.py script:

bash
Copy code
python milestone_5.py

# Project Status
The game is fully functional. Future improvements could include:

-Adding a graphical interface (GUI) for easier interaction.
-Allowing custom word lists from a file or online source.
-Implementing difficulty levels with variable word lengths or lives.

