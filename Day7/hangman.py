import random

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

num_of_letters = len(chosen_word)
display = ['_'] * num_of_letters
print(display)

print(chosen_word)

guess = input('Guess a letter: ').lower()

for letter in chosen_word:
    if letter == guess:
        print("huzzah!")
    else:
        print('wrong!!!')