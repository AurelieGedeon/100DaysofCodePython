import random

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

num_of_letters = len(chosen_word)
display = ['_'] * num_of_letters
print(display)

print(chosen_word)
game_over = False

while game_over == False:
    guess = input('Guess a letter: ').lower()

    for position in range(num_of_letters):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if '_' not in display:
        game_over = True
        print("You won!")
print(display)