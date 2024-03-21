alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encrypted_message = ""
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        encrypted_index =  letter_index + shift_amount
        encrypted_letter = alphabet[encrypted_index]
        encrypted_message += encrypted_letter
    print(encrypted_message)


encrypt(text, shift)