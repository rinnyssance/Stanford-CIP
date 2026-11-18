
# Import Python's built-in random library
import random

# Set the maximum number of guesses
NUM_ATTEMPTS = 6

# Create a list of five-letter words
WORDS = ["place", "candy", "plant", "dance", "grape"]

# Return a randomly selected word
def get_random_word():
    return random.choice(WORDS)

def main():
    # Welcome the player
    print("Welcome to Wordle!")

    # CHANGE 1: Choose a random secret word
    secret_word = get_random_word()

    # Give the player up to 6 valid attempts
    for attempt in range(NUM_ATTEMPTS):

        # CHANGE 2: Convert the player's guess to lowercase
        # This allows PLANT, Plant, and plant to work the same
        guess = input("Enter your guess: ").lower()

        # CHANGE 3: Check that the guess is exactly 5 letters
        # Invalid guesses do not use an attempt
        while len(guess) != 5:
            print("Please enter a 5-letter word.")
            guess = input("Enter your guess: ").lower()

        # Create an empty list for G, Y, and B marks
        result = []

        # Track letters that have not been matched
        remaining_letters = list(secret_word)

        # FIRST LOOP: Find exact matches (GREEN)
        for i in range(5):

            # Check if letters match at the same position
            if guess[i] == secret_word[i]:

                # Mark the exact match as G
                result.append("G")

                # Remove the matched letter
                remaining_letters.remove(guess[i])

            else:
                # Mark unmatched letters as B for now
                result.append("B")

        # SECOND LOOP: Find yellow matches
        for i in range(5):

            # Only check letters marked B
            if result[i] == "B":

                # Check if the letter is still available
                if guess[i] in remaining_letters:

                    # Change B to Y for a misplaced letter
                    result[i] = "Y"

                    # Remove it to prevent duplicate matches
                    remaining_letters.remove(guess[i])

        # THIRD LOOP: Format the output
        formatted_result = []

        # Go through each letter in the guess
        for i in range(5):

            # Get the guessed letter
            letter = guess[i]

            # Green matches get square brackets
            if result[i] == "G":
                formatted_result.append("[" + letter + "]")

            # Yellow matches get parentheses
            elif result[i] == "Y":
                formatted_result.append("(" + letter + ")")

            # Black matches stay unchanged
            else:
                formatted_result.append(letter)

        # Join formatted letters with spaces
        output = " ".join(formatted_result)

        # Display the result
        print("Result:", output)

        # Check if the player guessed the secret word
        if guess == secret_word:

            # Add 1 because attempt starts counting at 0
            print(f"Congratulations! You guessed the word in {attempt + 1} tries!")

            # Stop the game immediately
            break

    # This runs only if the player never guessed correctly
    else:
        # The player used all 6 attempts
        print(f"Better luck next time! The correct word was '{secret_word}'.")

# Run the program
if __name__ == "__main__":
    main()
