alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
alpha_length = len(alphabet)
alpha_index = alpha_length - 1

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        letter_index = alphabet.index(letter)
        shifted_index = letter_index + shift_amount
        if shifted_index > alpha_index:
            shifted_index = shifted_index - alpha_length
        elif shifted_index < 0:
            shifted_index = shifted_index + alpha_length
        new_letter = alphabet[shifted_index]
        end_text += new_letter
    print(f"The {direction}d message is {end_text}")

caesar(text, shift, direction)

# def encrypt(plain_text, shift_amount):
#     encrypted_message = ""
#     for letter in plain_text:
#         letter_index = alphabet.index(letter)
#         encrypted_index =  letter_index + shift_amount
#         if encrypted_index > alpha_index:
#             new_encrypted_index = encrypted_index - alpha_length
#             print(f"New encrypted index: {new_encrypted_index}")
#             encrypted_letter = alphabet[new_encrypted_index]
#             print(f"Encrypted letter: {encrypted_letter}")
#         else:
#             encrypted_letter = alphabet[encrypted_index]

#         encrypted_message += encrypted_letter
#     print(f"The encoded message is {encrypted_message}")

# def decrypt(cipher_text, shift_amount):
#     decrypted_message = ""
#     for letter in cipher_text:
#         letter_index = alphabet.index(letter)
#         decrypted_index = letter_index - shift_amount
#         if decrypted_index < 0:
#             new_decrypted_index = decrypted_index + alpha_length
#             print(f"New decrypted index: {new_decrypted_index}")
#             decrypted_letter = alphabet[new_decrypted_index]
#             print(f"decrypted letter: {decrypted_letter}")
#         else:
#             decrypted_letter = alphabet[decrypted_index]
#         decrypted_message += decrypted_letter
#     print(f"The decoded message is {decrypted_message}")

# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)


