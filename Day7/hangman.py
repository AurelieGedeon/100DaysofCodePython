import random
from word_list import *
from hangman_art import *
import os

def clear_console():
    # for Windows
    if os.name == 'nt':
        os.system('cls')
    # for Unix/Linux/MacOS
    else:
        os.system('clear')

def play_hangman():
    chosen_word = random.choice(word_list)

    num_of_letters = len(chosen_word)

    display = ['_'] * num_of_letters
    all_guesses = []
    wrong_guesses = []

    game_over = False

    lives = 6

    print(logo)

    while game_over == False:
        guess = input('Guess a letter: ').lower()
        clear_console()

        if guess in all_guesses:
            print("You already chose this letter; chose another one.")
            continue

        if guess in chosen_word:
            for position in range(num_of_letters):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
        else:
            if guess not in all_guesses:
                lives -= 1
                wrong_guesses.append(guess)

        all_guesses.append(guess)
        
        print(stages[lives])
        print(f' '.join(display))
        print(f'All Guesses: {all_guesses}')
        print(f'Incorrect guesses: {wrong_guesses}')

        if lives == 0:
            game_over = True
            print("You lose!")
            print(f'The correct word was: {chosen_word}') 
        elif '_' not in display:
            game_over = True
            print("You win!")

    play_again = input("Would you like again? (y/n): ").lower()

    if play_again == 'y':
        play_hangman()
    else:
        print("Thank you for playing!")

play_hangman()