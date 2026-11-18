# Code Machine — Stanford Code in Place X

## Project Overview

For this assignment, I built a Python program that uses a Caesar cipher to encrypt, decrypt, and crack secret messages.

The assignment consisted of four milestones, each introducing a new function that builds on the previous one.

## Milestones

### Milestone 1 — One Letter

I created a function called `shift_letter(letter, n)` that shifts a letter forward through the alphabet.

I used the modulo operator (`%`) to make sure letters wrap around when the shift goes beyond `z`.

### Milestone 2 — A Whole Message

I created an `encode(message, n)` function that shifts every lowercase letter in a message.

The function preserves spaces and punctuation.

### Milestone 3 — Decode

I created a `decode(message, n)` function that reverses the encryption by calling `encode()` with a negative shift.

```python
def decode(message, n):
    return encode(message, -n)
```

### Milestone 4 — Crack It

I created a `crack(message)` function that tries all 25 possible shifts.

```python
def crack(message):
    for shift in range(1, 26):
        decoded_message = decode(message, shift)
        print(f"Shift {shift}: {decoded_message}")
```

The program prints all 25 possible decoded messages so the user can identify the readable message.

---

## How I Used AI

I used ChatGPT as a programming assistant while completing the Code Machine assignment for Stanford Code in Place X.

I used it to review my existing Python code, understand Caesar ciphers, explain programming concepts, debug errors, and add explanatory comments.

ChatGPT helped me understand how the four functions work together:

- `shift_letter()` shifts individual letters.
- `encode()` calls `shift_letter()` to encrypt messages.
- `decode()` calls `encode()` to reverse encryption.
- `crack()` calls `decode()` to test every possible shift.

I also used ChatGPT to interpret Stanford's automated test results and compare the expected output against my program's actual output.

---

## ChatGPT's Mistakes

### 1. Missing the Decoding Requirement

ChatGPT initially provided code that only encoded messages.

However, Stanford's automated checker expected both encoded and decoded output.

The tests failed because the program never printed the required `Decoded:` line.

I had to share the failed test results before ChatGPT identified the missing functionality.

### 2. Making Assumptions About My Code

When I pasted my existing program, ChatGPT suggested that repeated copies of the code might be present in my actual Python file.

However, it had not verified that this was the case.

The assistant should have distinguished between repeated text in my message and a confirmed problem in my program.

### 3. Not Identifying the Current Milestone

ChatGPT initially responded without confirming which milestone I was completing.

As a result, it provided a solution that did not meet the requirements being checked by Stanford.

This created unnecessary additional debugging.

### 4. Providing Code Without Verifying the Tests

Although ChatGPT supplied a complete implementation for the final milestone, it had not independently verified the code against Stanford's automated checker.

This reinforced the importance of distinguishing between code that appears logically correct and code that has actually passed the required tests.

---

## Python Concepts Practiced

- Functions and function calls
- `for` loops
- String indexing
- String concatenation
- Conditional statements
- Modulo arithmetic (`%`)
- Negative numbers
- The `range()` function
- Reusing existing functions
- Debugging
- Automated testing

---

## What I Learned About Using AI

### AI Can Help Explain Programming Concepts

ChatGPT was useful for explaining how Caesar ciphers work and how modulo arithmetic handles alphabet wrapping.

### AI Can Misinterpret Assignment Requirements

The assistant initially overlooked the decoding requirement, which caused the suggested program to fail Stanford's tests.

### Error Messages and Test Results Matter

The automated checker helped identify the exact difference between the expected and observed output.

### Working Code Should Be Preserved

Rather than rewriting an entire program, it is often better to identify the missing functionality and make targeted changes.

### AI-Generated Code Still Requires Verification

Even when an AI-generated solution looks complete, I need to test it against the assignment requirements.

---

## Final Reflection

The Code Machine assignment helped me understand how functions can build on one another to solve increasingly complex programming problems.

I practiced manipulating strings, using loops, applying modulo arithmetic, and reusing functions rather than writing the same logic repeatedly.

I also used ChatGPT throughout the assignment to explain concepts, review code, and troubleshoot problems.

However, ChatGPT made mistakes that required me to correct its assumptions and provide additional information.

The most frustrating issue was receiving code that did not satisfy the current milestone's requirements.

**The most important thing from this assignment is that understanding my own code matters more than accepting an AI-generated answer.**

AI can be a useful learning and debugging tool, but its suggestions must be evaluated against the actual assignment instructions and test results.

This experience strengthened my understanding of Python and reinforced the importance of independent judgment when using AI-assisted programming.
