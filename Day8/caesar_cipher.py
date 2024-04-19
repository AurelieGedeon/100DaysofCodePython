from cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_length = len(alphabet)
cipher_over = False

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            letter_index = alphabet.index(char)
            shifted_index = (letter_index + shift_amount) % alpha_length
            new_letter = alphabet[shifted_index]
            end_text += new_letter
    print(f"The {direction}d message is {end_text}")

while cipher_over == False:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    end_cipher = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()

    if end_cipher == "no":
        cipher_over = True
    elif end_cipher == "yes":
        print("Goodbye!")
        cipher_over = False







