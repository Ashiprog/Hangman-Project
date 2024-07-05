from hangman_words_list import word_list
from hangman_stages import stages, logo
import random
chosen_word = random.choice(word_list)
print(chosen_word) # Just displaying the word for testing purpose. Original game will not display this.
no_of_lives = 6
game_over = False
display = []
for char in chosen_word:
    display += '_'
guess_list = []
print(logo)

while not game_over:

    guess = input("Guess a letter ").lower()
    if guess in guess_list:
        print("You have already guessed this  letter. Try again with a different letter")
        print(f"{' '.join(display)}")
    elif guess in chosen_word:
        print(f"letter {guess} is present in the word.Guess is correct")
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter
        print(f"{' '.join(display)}")
        if '_' not in display:
            print("Congrats. You have guessed the word correctly. You win")
            game_over = True
    else:
        no_of_lives -= 1
        print(stages[no_of_lives])
        print(f"Wrong guess. Letter {guess} is not present in the word. You lose a life")
        print(f"{' '.join(display)}")
        if no_of_lives == 0:
            print("Oh no!! You have lost the game")
            game_over = True
    guess_list.append(guess)
