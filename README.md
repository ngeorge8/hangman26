# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


Hangman-AiCore Project
Table of Contents
Description
Installation
Usage
File Structure
License
This is a command-line implementation of the classic Hangman game in Python. The program generates a random word from a list of words, and the user must guess the letters in the word one at a time. The user has a limited number of guesses, and each incorrect guess results in the drawing of a new part of a hangman figure. If the user guesses all the letters in the word before running out of guesses, they win the game. Otherwise, the hangman figure is fully drawn, and the user loses the game. Hangman Game

Getting Started
Clone this repository to your local machine.

Install Python 3 on your machine, if it is not already installed.
Open your terminal or command prompt and navigate to the directory containing the repository.
Run the command python milestone_3.py to start the game.
How to Play
The computer will generate a random word.
The player will have to guess the letters in the word one at a time.
The player has 6 attempts to guess the word correctly, otherwise the game is over.
The player will be shown a series of dashes representing the letters in the word. The dashes will be replaced with the correctly guessed letters as they are guessed.
If the player guesses a letter that is not in the word, they will lose an attempt.
If the player guesses a letter that is in the word, they will be informed and the corresponding dashes will be replaced with the letter.
If the player correctly guesses the entire word before running out of attempts, they win the game.
Description
The Hangman Game Project is a Python-based implementation of the classic word-guessing game. The aim of the project is to provide an interactive and entertaining game where players try to guess letters to uncover a hidden word within a limited number of attempts. Through this project, we practice object-oriented programming, user input validation, and game logic implementation.

Installation
To play the Hangman game, follow these steps:

Clone this repository to your local machine using:

https://github.com/montahac/Hangman-AiCore.git
Navigate to the project directory:

cd hangman-game
Run the game by executing the Python script:

python milestone_5.py
Usage
The game will display underscores representing the letters in the word to guess.
Enter a single alphabetical character to guess a letter.
The game will provide feedback about the correctness of the guess and the remaining lives.
Continue guessing until you either guess the word or run out of lives.
File Structure
The project files are structured as follows:

hangman-game/
├── milestone_4.py
├── milestone_5.py
└── README.md
milestone_4.py: Contains the Hangman class definition and game logic implementation up to Milestone 4.
milestone_5.py: Contains the complete Hangman game implementation up to Milestone 5, including the play_game function.
README.md: This README file provides information about the project.
