import random
from word_list import *
from hangman_art import *


chosen_word = random.choice(word_list)

num_of_letters= len(chosen_word)

display = ['_'] * num_of_letters
wrong_guesses = []

game_over = False

lives = 6

print(logo)

while game_over == False:
    guess = input('Guess a letter: ').lower()

    for position in range(num_of_letters):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        wrong_guesses.append(guess)
    
    print(stages[lives])
    print(f'Incorrect guesses: {wrong_guesses}')
    print(f' '.join(display))

    if lives == 0:
        game_over = True
        print("You lose!")
        print(f'The correct word was: {chosen_word}') 
    elif '_' not in display:
        game_over = True
        print("You win!")
    