# REFACTORING CODE - COMBINING BOTH FUNCTIONS INTO ONE
# DECRYPTING MESSAGES

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

def caesar(encrypted_text, shift_amount, dire):
    word = ""

    if dire == "decode":
        shift_amount *= -1

    for letter in encrypted_text:

        letter_index = alphabet.index(letter)

        new_letter_index = letter_index + shift_amount

        if new_letter_index < 0:
            new_letter_index += 26

        if new_letter_index > 25:
            new_letter_index -= 26

        word += alphabet[new_letter_index]

    print(f"Your {dire}d word is {word}")


caesar(text, shift, direction)
