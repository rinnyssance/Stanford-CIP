
# Project Notes — Planetary Weight Calculator

## Section
Stanford Code in Place — Section 3: Console Programming

---

# Project Overview

This project focused on building a console-based Python program that calculates a user's equivalent weight on different planets using gravitational conversion factors.

The project began with a Mars-only calculator and later expanded into a multi-planet planetary weight calculator as a stretch challenge.

---

# Milestone #1 — Mars Weight Calculator

## Goal

Create a Python program that:
1. Accepts user input for Earth weight
2. Converts the value to Mars weight
3. Rounds the output to 2 decimal places
4. Prints the formatted result

---

# Key Concepts Practiced

- Variables
- User input
- Floats vs integers
- Arithmetic operations
- String formatting
- Output formatting
- Python rounding
- Debugging
- Console programming

---

# Errors and Debugging Notes

## Error #1 — Using `int()` Instead of `float()`

### Problem

The program initially failed when decimal inputs were tested.

Example failing input:

```python
147.2
```

Error received:

```python
ValueError: invalid literal for int() with base 10: '147.2'
```

### Cause

The program used:

```python
weight = int(input())
```

Integers cannot process decimal values.

### Fix

Changed the code to:

```python
weight = float(input())
```

### Lesson Learned

- `int()` only accepts whole numbers
- `float()` accepts decimal numbers
- User input should match expected data types

---

## Error #2 — Output Formatting Mismatch

### Problem

The program logic was correct, but the automated grader still failed the submission.

### Cause

The output string did not exactly match the required formatting.

Incorrect:

```python
print("This is the weight on Mars", result)
```

Expected:

```python
print("The equivalent weight on Mars:", result)
```

### Lesson Learned

Automated grading systems are extremely strict about:
- capitalization
- punctuation
- spacing
- exact wording

Even correct calculations can fail if formatting does not match exactly.

---

## Error #3 — Extra Spaces in `__main__`

### Problem

The program structure caused issues because of incorrect formatting in the `__main__` statement.

Incorrect:

```python
if __name__ == " __main__ ":
```

Correct:

```python
if __name__ == "__main__":
```

### Lesson Learned

Python syntax must be exact.
Extra spaces inside strings change the value completely.

---

## Error #4 — Understanding Data Types During Input

### Observation

There was initial confusion about:
- strings
- numeric values
- converted integers
- converted floats

Especially when working with:
- user input
- substrings
- numeric operations

### Lesson Learned

Input from `input()` is always stored as a string until converted.

Examples:

```python
"123"     # string
123       # integer
123.0     # float
```

---

# Milestone #2 — Planetary Weight Calculator

## Stretch Goal

Expand the Mars calculator to support all major planets using unique gravity constants.

## Planned Features

- Mercury support
- Venus support
- Mars support
- Jupiter support
- Saturn support
- Uranus support
- Neptune support

---

# Planetary Gravity Constants

| Planet   | Gravity Relative to Earth |
|----------|---------------------------|
| Mercury  | 0.376 |
| Venus    | 0.889 |
| Mars     | 0.378 |
| Jupiter  | 2.360 |
| Saturn   | 1.081 |
| Uranus   | 0.815 |
| Neptune  | 1.140 |

---

# Planned Logic

Program flow:

1. Ask user for Earth weight
2. Ask user for planet name
3. Use conditional logic (`if` statements)
4. Apply correct gravity constant
5. Round output
6. Print formatted result

---

# Broader Takeaways

This project reinforced:
- precision in programming
- strict syntax requirements
- debugging through error messages
- the importance of data types
- how computers interpret instructions literally

It also helped strengthen computational thinking skills by breaking a larger problem into smaller logical steps.
````
