# Hangman-Project
Implementing a classic Hangman game in Python. Players guess letters to uncover a hidden word within a limited number of attempts. A fun project to practice strings, loops, and conditional statements in Python programming.

Initialization:
The game begins by importing a list of words (word_list) and predefined stages of the hangman figure (stages) from separate modules (hangman_words_list and hangman_stages).
A random word is chosen from word_list, which the player needs to guess.

Game Setup:
The chosen word is displayed for testing purposes (print(chosen_word)), but this line is typically omitted in the actual game.
The player starts with 6 lives (no_of_lives = 6) and the game state (game_over) is initialized to False.

Display Initialization:
An initial display (display) is created as a list of underscores (_) representing each letter in the chosen word. This list will be updated as correct letters are guessed.

Game Loop:
The main game loop (while not game_over) continues until the game is over (either by guessing the word correctly or running out of lives).
Inside the loop, the player is prompted to guess a letter (guess = input("Guess a letter ").lower()).

Guess Handling:
If the guessed letter (guess) has already been guessed (guess in guess_list), a message informs the player to try again with a different letter.
If the guessed letter is in the chosen word (guess in chosen_word):
The letter is revealed in the display list at its corresponding positions in the word.
If all letters in display are filled (no more underscores), the player wins and the game ends (game_over = True).
If the guessed letter is not in the chosen word:
The number of lives (no_of_lives) decreases by 1.
The corresponding hangman stage (stages[no_of_lives]) is displayed.
If no_of_lives reaches 0, the player loses and the game ends (game_over = True).

Game Outcome:
After each guess, the updated display and current game state are printed to provide feedback to the player.
Once the game loop ends, a message is displayed indicating whether the player won by guessing the word correctly or lost by running out of lives.

Additional Features:
A guess_list keeps track of all guessed letters to prevent duplicate guesses.
The logo is printed at the beginning of the game for aesthetic purposes.
