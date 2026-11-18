# Khansole Academy – CIPx Exercise

## Exercise
The goal of this exercise is to create a Python program that generates random addition problems using two-digit numbers between 10 and 99.

The program asks the user for an answer, checks whether it is correct, and provides feedback.

In Step 2, the program must continue generating addition problems until the user gets **three correct answers in a row**.

## Where We Got Confused
- We initially struggled with generating random numbers using `random.randint(10, 99)`.
- We weren't sure how to make the program repeat questions until the user answered three correctly in a row.
- We were confused about the difference between repeating a program three times and getting three consecutive correct answers.

## How We Solved It
- We used `random.randint(10, 99)` to generate two random numbers.
- We used a `while` loop to keep generating new addition problems.
- We created a counter called `correct_in_a_row` to track correct answers.
- Each correct answer increases the counter by 1.
- An incorrect answer resets the counter to 0.
- Once the counter reaches 3, the loop ends and the program congratulates the user.
