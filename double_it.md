# Doubling Numbers with a While Loop — Reflection & Debugging Notes

## Assignment Overview

This assignment focused on using a `while` loop to repeatedly double a number until it becomes greater than 100.

The program:
- asks the user for a number
- stores it in a variable called `curr_value`
- keeps doubling the value
- prints each new doubled number
- stops once the number is no longer less than 100

Example:

If the user enters:

```text
2
```

The program prints:

```text
4
8
16
32
64
128
```

The loop stops after `128` because the next loop check asks:

```python
curr_value < 100
```

and `128` is not less than `100`.

---

# Concepts This Exercise Was Teaching

## 1. Variable Updating

This was one of the first exercises where a variable continuously changes over time.

The key line was:

```python
curr_value = curr_value * 2
```

This means:
- take the current value
- multiply it by 2
- store the new value back into `curr_value`

Example:

```text
curr_value = 2
curr_value = 4
curr_value = 8
curr_value = 16
```

The same variable keeps being replaced with a newer value.

---

## 2. While Loops

The loop condition was:

```python
while curr_value < 100:
```

This means:

> “Keep running this code while the number is still below 100.”

The loop:
- checks the condition
- runs the code inside
- checks again
- repeats until the condition becomes false

---

# Mistake #1 — Missing Colon

My original code:

```python
while curr_value < 100
```

Error:

```text
SyntaxError: expected ':'
```

What I learned:

Python requires a colon `:` after loop statements.

Correct structure:

```python
while condition:
```

The colon tells Python that a block of code is about to begin.

---

# Mistake #2 — Missing Indentation

After fixing the colon, I got another error:

```text
IndentationError: expected an indented block
```

This happened because the loop had no indented code underneath it.

Incorrect:

```python
while curr_value < 100:
```

Correct structure:

```python
while condition:
    do_something
```

I learned that Python uses indentation to define blocks of code.

Without indentation, Python does not know what should repeat inside the loop.

---

# My Final Program

```python
def main():
    curr_value = int(input("Enter a number: "))

    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()
```

---

# Important Logic I Learned

The order of operations matters.

The loop:
1. checks if the value is below 100
2. doubles the value
3. prints the new value
4. repeats

That is why the first printed number is `4` instead of `2`.

---

# Biggest Takeaway

This exercise helped me understand:
- loop structure
- indentation
- variable updates
- stopping conditions
- repeated execution

This felt like one of the first assignments where the program had ongoing behavior instead of just running line-by-line once.
