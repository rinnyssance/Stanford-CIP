# Sunrise Fill-in-the-Blanks

## Problem Overview

Create a Python program that asks the user for:

1. A color
2. An adjective
3. A goal they would like to achieve

The program should then build a short story using the user's answers.

---

# Story Template

```text
At dawn the sky turned [color], and the air felt [adjective]. I decided today I will finally [goal].
```

---

# Important Formatting Rules

The autograder is extremely strict.

Your input prompts must match **exactly**:

```python
"A color: "
"An adjective: "
"A goal you would like to achieve: "
```

Even:
- missing spaces
- extra punctuation
- different capitalization

can cause the program to fail the tests.

---

# Final Working Solution

```python
def main():
    # Ask the user for input
    color = input("A color: ")
    adjective = input("An adjective: ")
    goal = input("A goal you would like to achieve: ")

    # Print the completed story
    print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")


if __name__ == "__main__":
    main()
```

---

# Example Run #1

```text
A color: blue
An adjective: smelly
A goal you would like to achieve: eat fewer bugs
At dawn the sky turned blue, and the air felt smelly. I decided today I will finally eat fewer bugs.
```

---

# Example Run #2

```text
A color: pink
An adjective: friendly
A goal you would like to achieve: learn to code
At dawn the sky turned pink, and the air felt friendly. I decided today I will finally learn to code.
```

---

# Concepts Practiced

## 1. Using `input()`

The `input()` function allows the user to type information into the program.

Example:

```python
color = input("A color: ")
```

The user's answer gets stored in the variable `color`.

---

## 2. Variables

Variables store information that can be reused later.

Example:

```python
goal = input("A goal you would like to achieve: ")
```

Now the variable `goal` contains the user's answer.

---

## 3. f-Strings

An f-string allows variables to be inserted directly into text.

Example:

```python
print(f"My favorite color is {color}")
```

The `f` means:
- "formatted string"

The `{}` brackets tell Python where to place variable values.

---

# Errors I Ran Into

## 1. Extra Spaces in the Output

### Problem

Using commas inside `print()` caused unexpected spaces.

Example:

```python
print("Hello", color)
```

This can break strict autograders.

---

### Fix

Use an f-string instead:

```python
print(f"Hello {color}")
```

This gives precise control over punctuation and spacing.

---

## 2. Missing Punctuation

### Problem

The expected sentence included:
- a comma after the color
- a period after the adjective

Without exact punctuation, the autograder failed.

---

### Fix

Use the exact sentence format:

```python
print(f"At dawn the sky turned {color}, and the air felt {adjective}. I decided today I will finally {goal}.")
```

---

## 3. IndentationError

### Error Message

```text
IndentationError: unindent does not match any outer indentation level
```

### Cause

One line inside `main()` was not aligned correctly.

Python requires consistent indentation.

---

### Correct Example

```python
def main():
    print("Hello")
```

---

### Incorrect Example

```python
def main():
print("Hello")
```

---

# Key Takeaways

- Python is very strict about indentation.
- Autograders require exact formatting.
- f-strings make sentence-building much easier.
- Variables allow programs to become interactive and dynamic.
