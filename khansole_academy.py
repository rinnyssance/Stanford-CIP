
import random  # Import the random number library

# Welcome the user
print("Khansole Academy")

# Keep track of consecutive correct answers
correct_in_a_row = 0

# Keep asking questions until the user gets 3 correct
while correct_in_a_row < 3:

    # Generate two random numbers between 10 and 99
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)

    # Calculate the correct answer
    correct_answer = num1 + num2

    # Display the addition problem
    print(f"What is {num1} + {num2}?")

    # Ask the user for their answer
    user_answer = int(input("Your answer: "))

    # Check whether the answer is correct
    if user_answer == correct_answer:

        # Add 1 to the consecutive correct answer count
        correct_in_a_row += 1

        # Tell the user they got it right
        print("Correct!")
        print(f"You've gotten {correct_in_a_row} correct in a row.")

    else:
        # Reset the count to 0 if the answer is wrong
        correct_in_a_row = 0

        # Show the user the correct answer
        print("Incorrect.")
        print(f"The expected answer is {correct_answer}")

    # Add a blank line between questions
    print()

# This runs once the user gets 3 correct in a row
print("Congratulations! You mastered addition.")
