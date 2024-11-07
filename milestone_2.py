import random

# List of favorite fruits
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Select a random word from word_list
word = random.choice(word_list)

# Print the selected word (optional: for testing the random selection)
print(word)

# Prompt the user to enter a single letter
guess = input("Enter a single letter: ")

# Check if the input is valid
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
