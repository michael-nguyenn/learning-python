from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Importing and displaying logo
print(logo)

# Restarting the game cypher if user wishes
should_continue = True

while should_continue:

    # Gathering user inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(encrypted_text, shift_amount, dire):
        word = ""

        # If the user inputs a number greater than the amount of characters in the alphabet
        shift_amount = shift_amount % 26

        # If user chooses decode, reverse the order of shifts
        if dire == "decode":
            shift_amount *= -1

        for char in encrypted_text:
            if char not in alphabet:
                word += char
                continue

            letter_index = alphabet.index(char)

            new_letter_index = letter_index + shift_amount

            if new_letter_index < 0:
                new_letter_index += 26

            if new_letter_index > 25:
                new_letter_index -= 26

            word += alphabet[new_letter_index]

        print(f"Your {dire}d word is {word}")


    caesar(text, shift, direction)

    restart_game = input("\nWould you like to restart the cipher program? Type 'yes', or 'no'\n")

    if restart_game == "no":
        should_continue = False
