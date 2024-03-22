from cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alpha_length = len(alphabet)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
        else:
            letter_index = alphabet.index(letter)
            shifted_index = (letter_index + shift_amount) % alpha_length
            new_letter = alphabet[shifted_index]
            end_text += new_letter
    print(f"The {direction}d message is {end_text}")

caesar(text, shift, direction)



