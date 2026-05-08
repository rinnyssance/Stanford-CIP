# Hello Name Exercise Notes

## Assignment

Write a customizable version of the classic `"Hello World"` program.

Instead of printing:

```python
Hello World
```

the program should:

1. Ask the user for their name
2. Store the user's response in a variable
3. Print a personalized greeting

---

# Example

## User Input

```text
What is your name?
```

If the user types:

```text
Karel
```

The output should be:

```text
What is your name? Karel
Hello Karel
```

---

# Important Python Concepts

## `input()`

The `input()` function asks the user for information.

Example:

```python
name = input("What is your name? ")
```

### What this does:
- Displays a question
- Waits for the user to type something
- Stores the result in a variable

---

## `print()`

The `print()` function displays output to the console.

Example:

```python
print("Hello")
```

You can also print multiple things:

```python
print("Hello", name)
```

---

# Final Correct Solution

```python
def main():

    # Ask for the user's name
    name = input("What is your name? ")

    # Print the greeting
    print("Hello", name)

if __name__ == '__main__':
    main()
```

---

# Step-by-Step Breakdown

## Step 1: Ask for input

```python
name = input("What is your name? ")
```

### Explanation
- `input()` runs the input function
- The text inside the parentheses is the prompt
- Whatever the user types gets stored inside `name`

---

## Step 2: Print the greeting

```python
print("Hello", name)
```

### Explanation
- `"Hello"` is text
- `name` is the variable
- Python prints both together

Example:

```text
Hello Erin
```

---

# Errors I Made

## Error #1 — Variable Not Defined

### My Code

```python
input("What is your name? ")

print("Hello", name)
```

### Error Message

```text
NameError: name 'name' is not defined
```

### Why It Happened

I asked for input, but I never stored the result in a variable.

This line:

```python
input("What is your name? ")
```

runs the function, but throws away the answer.

So later, Python has no idea what `name` is.

---

## Fix

Store the result:

```python
name = input("What is your name? ")
```

---

# Error #2 — Storing the Function Instead of Running It

## My Code

```python
name = input
```

### Output

```text
Hello <built-in function input>
```

### Why It Happened

I stored the actual function itself instead of calling it.

This:

```python
input
```

means:

> the function

while this:

```python
input()
```

means:

> run the function

---

# Correct Version

```python
name = input("What is your name? ")
```

---

# Important Concept

## Parentheses Matter

### Without parentheses:

```python
input
```

Python sees the function itself.

### With parentheses:

```python
input()
```

Python runs the function.

---

# Key Things Learned

- How to use `input()`
- How to store data in variables
- How to use `print()`
- Why parentheses are important
- The difference between:
  - a function
  - calling a function
- How variables are reused later in a program

---

# Mental Model

Think of variables like labeled boxes.

```python
name = input("What is your name? ")
```

means:

1. Ask the user a question
2. Take the answer
3. Put the answer into a box called `name`

Later:

```python
print("Hello", name)
```

means:

> Open the `name` box and print what's inside.

---

# Example Run

```text
What is your name? Erin
Hello Erin
```
