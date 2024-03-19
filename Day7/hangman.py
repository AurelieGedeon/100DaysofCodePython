import random

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

print(chosen_word)

guess = input('Guess a letter: ').lower()

chosen_word_letters = [*chosen_word]
print(chosen_word_letters)

if guess in chosen_word_letters:
    print("huzzah!")