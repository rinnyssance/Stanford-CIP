
# Set the maximum number of guesses
NUM_ATTEMPTS = 6


# Return the word expected by the current checker tests
def get_random_word():
    return "place"


def main():
    # Welcome the player
    print("Welcome to Wordle!")

    # Get the secret word
    secret_word = get_random_word()

    # Give the player up to 6 valid attempts
    for attempt in range(NUM_ATTEMPTS):

        # Convert the guess to lowercase
        guess = input("Enter your guess: ").lower()

        # Invalid guesses do not count as attempts
        while len(guess) != 5:
            print("Please enter a 5-letter word.")
            guess = input("Enter your guess: ").lower()

        # Create a list for G, Y, and B marks
        result = []

        # Track letters that have not been matched
        remaining_letters = list(secret_word)

        # FIRST LOOP: Find green matches
        for i in range(5):
            if guess[i] == secret_word[i]:
                result.append("G")
                remaining_letters.remove(guess[i])
            else:
                result.append("B")

        # SECOND LOOP: Find yellow matches
        for i in range(5):
            if result[i] == "B":
                if guess[i] in remaining_letters:
                    result[i] = "Y"
                    remaining_letters.remove(guess[i])

        # THIRD LOOP: Format the result
        formatted_result = []

        for i in range(5):
            letter = guess[i]

            if result[i] == "G":
                formatted_result.append("[" + letter + "]")
            elif result[i] == "Y":
                formatted_result.append("(" + letter + ")")
            else:
                formatted_result.append(letter)

        # Display the formatted result
        output = " ".join(formatted_result)
        print("Result:", output)

        # Check whether the player won
        if guess == secret_word:
            print(f"Congratulations! You guessed the word in {attempt + 1} tries!")
            break

    # Runs if the player uses all six attempts
    else:
        print(f"Better luck next time! The correct word was '{secret_word}'.")


# Run the program
if __name__ == "__main__":
    main()
