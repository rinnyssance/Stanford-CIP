
# Store the 26 lowercase letters
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


# MILESTONE 1: Shift one letter
def shift_letter(letter, n):

    # Find the position of the letter
    position = ALPHABET.find(letter)

    # Calculate the new position and wrap around
    new_position = (position + n) % 26

    # Return the shifted letter
    return ALPHABET[new_position]


# MILESTONE 2: Encode a whole message
def encode(message, n):

    # Start with an empty string
    result = ""

    # Go through each character in the message
    for character in message:

        # Shift lowercase letters
        if character in ALPHABET:
            result += shift_letter(character, n)

        # Keep spaces and punctuation unchanged
        else:
            result += character

    # Return the encoded message
    return result


# MILESTONE 3: Decode a message
def decode(message, n):

    # Reverse the shift by using a negative number
    return encode(message, -n)


# MILESTONE 4: Crack a secret message
def crack(message):

    # Try every possible shift from 1 through 25
    for shift in range(1, 26):

        # Decode the message using the current shift
        decoded_message = decode(message, shift)

        # Print the shift number and decoded message
        print(f"Shift {shift}: {decoded_message}")


# Main function
def main():

    # Welcome the user
    print("Welcome to the Code Machine!")

    # Ask for the encrypted message
    message = input("Enter a message: ")

    # Try all 25 shifts
    crack(message)


# Run the program
if __name__ == "__main__":
    main()
