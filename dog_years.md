# Dog Years Calculator 🐶

## Assignment
Write a program which asks a user to input an age in human years and converts it to the equivalent age in dog years.

Dogs age differently than humans. On average:

```python
1 human year = 7.18 dog years
```

Your program should:
1. Ask the user for an age in calendar years
2. Convert the age into dog years
3. Print the result

---

# Final Working Code

```python
# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18

def main():
    age = float(input("Enter an age in calendar years: "))
    total = DOG_YEARS_MULTIPLIER * age

    print(f"That's {total} in dog years!")

if __name__ == '__main__':
    main()
```

---

# Example Run

```text
Enter an age in calendar years: 10
That's 71.8 in dog years!
```

---

# What I Learned

## 1. `input()` collects user input
```python
age = input("Enter an age in calendar years: ")
```

`input()` always returns a string.

---

## 2. Convert strings into numbers
Because we need math, we convert the input into a float:

```python
float(input(...))
```

This allows multiplication with decimals like `7.18`.

---

## 3. Variables store information

```python
total = DOG_YEARS_MULTIPLIER * age
```

- `DOG_YEARS_MULTIPLIER` stores the conversion rate
- `age` stores the user's input
- `total` stores the calculated dog years

---

## 4. f-strings insert variables into text

```python
print(f"That's {total} in dog years!")
```

The `f` before the string allows variables inside `{}` to display their values.

---

# Errors I Made Along the Way

## Mistake #1 — Using `print()` instead of `input()`

Incorrect:

```python
age = print("Enter an age in calendar years:")
```

Problem:
- `print()` only displays text
- It does NOT collect input
- `print()` returns `None`

This caused the error:

```text
TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'
```

---

## Mistake #2 — Forgetting f-string formatting

Incorrect:

```python
print("That's {total} in dog years!")
```

Problem:
- Without the `f`, Python prints `{total}` literally instead of the variable value.

Correct:

```python
print(f"That's {total} in dog years!")
```

---

# Key Concepts Practiced

- User input
- Variables
- Floats
- Multiplication
- String formatting
- Program structure with `main()`

---

# Final Thoughts

This exercise introduced a simple programming workflow:

```text
Input → Process → Output
```

The user enters data, the program performs a calculation, and the result is displayed back to the user.
