Hangman Game Project
Table of Contents
Project Description
Features
Technologies Used
Getting Started
Usage
File Structure
Project Status
License
Project Description
This is a command-line Hangman game implemented in Python. The objective is to guess a hidden word, letter by letter, within a limited number of attempts. If you guess all unique letters in the word before exhausting your lives, you win the game. If you use all available guesses without completing the word, you lose.

Purpose
This project was developed as a practice exercise in Python programming, focusing on:

Working with classes and object-oriented programming.
Using control flow mechanisms like loops and conditional statements.
Managing user input and basic input validation.
Practicing modular design and code readability with functions and classes.
Features
Random Word Selection: The game selects a word randomly from a predefined list.
Guess Validation: Ensures that only single alphabetical characters are accepted as guesses.
Tracking Guesses and Lives: Keeps track of the player’s guesses and remaining lives.
Game Ending Conditions: Automatically ends the game when either the word is completely guessed or lives run out.
Clear Feedback: Displays messages guiding the user through the game and providing feedback on each guess.
Technologies Used
Python 3: The project is built with Python and utilizes core libraries, including random for selecting random words.
Getting Started
Prerequisites
Python 3.x installed on your machine. You can download Python here.
Installation
Clone this repository:
bash
Copy code
git clone https://github.com/your-username/hangman-project.git
cd hangman-project
No additional libraries are required as this project only uses standard Python modules.
Running the Game
To start the game, run the milestone_5.py script:

bash
Copy code
python milestone_5.py
Usage
Once you start the game:

The program will randomly select a word from a predefined list.
You’ll be prompted to guess a letter.
Input Requirements:
Only single alphabetical characters are allowed.
Repeated guesses will prompt a reminder that the letter was already tried.
You’ll receive feedback after each guess, and the game will notify you of the current state of the word, remaining lives, and when the game is won or lost.
Example Gameplay
Starting Prompt:
css
Copy code
Guess a letter: 
Valid Guess:
arduino
Copy code
Good guess! 'a' is in the word.
Invalid Guess:
vbnet
Copy code
Sorry, 'x' is not in the word. You have 4 lives left.
File Structure
bash
Copy code
hangman-project/
│
├── milestone_1.py          # Initial project setup with list creation
├── milestone_2.py          # Adds word selection and input handling
├── milestone_3.py          # Adds continuous guess validation loop
├── milestone_4.py          # Introduces Hangman class structure
├── milestone_5.py          # Complete game with play loop and win/lose conditions
└── README.md               # Project documentation
Project Status
The game is fully functional. Future improvements could include:

Adding a graphical interface (GUI) for easier interaction.
Allowing custom word lists from a file or online source.
Implementing difficulty levels with variable word lengths or lives.
License
This project is licensed under the MIT License. See the LICENSE file for details.
