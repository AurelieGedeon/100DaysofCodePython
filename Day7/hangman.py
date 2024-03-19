import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

print(chosen_word)

num_of_letters= len(chosen_word)

display = ['_'] * num_of_letters
game_over = False

lives = 6

while game_over == False:
    guess = input('Guess a letter: ').lower()

    for position in range(num_of_letters):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(lives)
    print(stages[lives])
    print(f' '.join(display))

    if lives == 0:
        game_over = True
        print("You lose!") 
    elif '_' not in display:
        game_over = True
        print("You win!")
    