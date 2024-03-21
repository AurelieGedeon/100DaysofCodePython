alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alpha_index = len(alphabet) - 1

def encrypt(plain_text, shift_amount):
    encrypted_message = ""
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        encrypted_index =  letter_index + shift_amount
        if encrypted_index > alpha_index:
            new_encrypted_index = encrypted_index - (alpha_index + 1)
            print(f"New encrypted index: {new_encrypted_index}")
            encrypted_letter = alphabet[new_encrypted_index]
            print(f"Encrypted letter: {encrypted_letter}")
        else:
            encrypted_letter = alphabet[encrypted_index]

        encrypted_message += encrypted_letter
    print(f"The encoded message is {encrypted_message}")

def decrypt(plain_text, shift_amount):
    decrypted_message = ""
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        decrypted_index = letter_index - shift_amount
        if decrypted_index < 0:
            new_decrypted_index = decrypted_index + (alpha_index + 1)
            print(f"New decrypted index: {new_decrypted_index}")
            decrypted_letter = alphabet[new_decrypted_index]
            print(f"decrypted letter: {decrypted_letter}")
        else:
            decrypted_letter = alphabet[decrypted_index]
        decrypted_message += decrypted_letter
    print(f"The decoded message is {decrypted_message}")

if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)


