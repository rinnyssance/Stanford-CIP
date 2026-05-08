# Multiply Two Numbers

## Problem
Write a Python program that:

1. Prints `"This program multiplies two numbers."`
2. Prompts the user for the first number
3. Converts the input into an integer
4. Prompts the user for the second number
5. Converts the input into an integer
6. Multiplies the two numbers
7. Prints the result

---

## Correct Solution

```python
def main():
    print("This program multiplies two numbers.")

    num1 = input("Enter first number: ")
    num1 = int(num1)

    num2 = input("Enter second number: ")
    num2 = int(num2)

    total = num1 * num2

    print(total)


if __name__ == '__main__':
    main()
```

---

## Example Run

```text
This program multiplies two numbers.
Enter first number: 20
Enter second number: 3
60
```

---

## My Original Error

### What I wrote:

```python
print("The total is " + str(total) + ".")
```

### Why it failed:
The assignment expected ONLY the number to be printed.

The autograder compares output very strictly, so extra words or punctuation can cause tests to fail.

---

## Correct Output Line

```python
print(total)
```

---

## Important Lesson

Early programming errors are often caused by:

- Extra spaces
- Wrong capitalization
- Incorrect punctuation
- Extra words in output
- Formatting mismatches
- Forgetting type conversion

In this exercise, the logic was correct.
The issue was simply not following the exact output format required by the assignment.

---

## Concepts Practiced

- `input()`
- Variables
- Integer conversion with `int()`
- Multiplication
- Printing output
- Following program specifications exactly
