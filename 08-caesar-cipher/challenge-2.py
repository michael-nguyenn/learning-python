# DECRYPTING MESSAGES

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    encrypted_word = ""

    for letter in plain_text:
        new_letter_index = alphabet.index(letter) + shift_amount

        # If we shift past z, we have to restart from a
        if new_letter_index > 25:
            new_letter_index -= 26

        encrypted_word += alphabet[new_letter_index]

    print(f"The encoded text is {encrypted_word}")


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# e.g.
# cipher_text = "mjqqt"
# shift = 5
# plain_text = "hello"
# print output: "The decoded text is hello"

def decrypt(encrypted_text, shift_amount):
    decrypted_word = ""

    for letter in encrypted_text:
        new_letter_index = alphabet.index(letter) - shift_amount

        if new_letter_index < 0:
            new_letter_index += 26

        decrypted_word += alphabet[new_letter_index]

    print(f"Your decrypted word is {decrypted_word}")


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the
#  'direction' variable. Then call the correct function based on that 'direction' variable.
#  You should be able to test the code to encrypt *AND* decrypt a message.

if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)
