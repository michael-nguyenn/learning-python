# ENCRYPTING WORDS

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by
#  the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"


def encrypt(plain_text, shift_amount):
    encrypted_word = ""

    for letter in plain_text:
        new_letter_index = alphabet.index(letter) + shift_amount

        # If we shift past z, we have to restart from a
        if new_letter_index > 25:
            new_letter_index -= 26

        encrypted_word += alphabet[new_letter_index]

    print(f"The encoded text is {encrypted_word}")


# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs.
#  You should be able to test the code and encrypt a message.

encrypt(text, shift)
