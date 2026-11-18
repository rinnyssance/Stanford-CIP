# CIPx – Cheer on Your Team

## Exercise

Write a Python program that loops through a list of words
`["way", "to", "go", "team"]`, converts each word to uppercase,
and prints each word with an exclamation mark on a separate line.

### Expected Output

WAY!  
TO!  
GO!  
TEAM!

## Mistakes We Made

### 1. Using `.upper()` on a List

We wrote `CHEER.upper()` instead of `word.upper()`.

This caused an `AttributeError` because `.upper()` works on
strings, not entire lists.

**Correction:** Use `word.upper()` to convert each individual
word to uppercase.

### 2. Using the Wrong Variable Name

We wrote `for word in words:` even though our list was
named `CHEER`.

**Correction:** Use `for word in CHEER:` so Python loops
through the correct list.

### 3. Misunderstanding `end=" "`

We originally used `end=" "` in our `print()` statement.

We thought removing it was what fixed our error, but it
only changes how the output is formatted.

**Correction:** Remove `end=" "` so each word prints
on a separate line.

## What We Learned

The main mistake was confusing the entire list (`CHEER`)
with an individual item (`word`).

We learned that a `for` loop lets us access each string
individually and apply methods like `.upper()` to it.
