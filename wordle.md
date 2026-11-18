# Wordle — Stanford Code in Place X

## Project Overview

For this exercise, I developed a Python version of Wordle across five milestones.

The goal was to build a word-guessing game that compares letters, identifies correct and misplaced matches, formats the results, limits the number of attempts, and eventually selects a random secret word.

Each milestone introduced new programming concepts while building on the previous solution.

### Python Concepts Practiced

- `for` and `while` loops
- Lists and string indexing
- Conditional statements
- Functions and imports
- String formatting and `.join()`
- String normalization with `.lower()`
- The `break` statement
- The `for`–`else` structure
- Input validation
- Random word selection
- Debugging Python errors
- Automated testing

---

## Milestone 1 — Exact Matches

The first milestone involved comparing a five-letter guess against the secret word `"candy"`.

I used a `for` loop to compare each letter in the guess with the letter at the same index in the secret word.

- `G` represented a correct letter in the correct position.
- `B` represented a letter that did not match at that position.

### What I Learned

String indexing allows me to compare corresponding characters in two words.

I also practiced building a list of results and displaying those results as a string.

---

## Milestone 2 — Yellow Matches

The second milestone introduced `Y` for letters that appeared in the secret word but were in the wrong position.

I created a list called `remaining_letters` to track letters that had not already been matched.

The solution required two separate loops:

1. Identify green matches and remove those letters from `remaining_letters`.
2. Check unmatched letters for yellow matches and remove them as they were used.

This prevented duplicate letters from being counted more times than they appeared in the secret word.

For example, guessing `"daddy"` against `"candy"` should produce:

```text
B G B G G
```

The secret word contains only one `d`, and the exact match claims that letter.

### What I Learned

The order of operations matters.

Checking green matches before yellow matches prevents misplaced letters from consuming matches that belong to letters in the correct positions.

This was one of the more interesting programming challenges in the exercise.

---

## Milestone 3 — Formatting Results

The third milestone required replacing the original `G`, `Y`, and `B` markers with formatted letters.

- Green: `[a]`
- Yellow: `(a)`
- Black: `a`

This required a third loop and a list called `formatted_result`.

The program then joined the formatted letters into a single string.

```python
output = " ".join(formatted_result)
print("Result:", output)
```

### My Observation

I actually preferred the original `G`, `Y`, and `B` markers.

They were straightforward, readable, and easy to interpret.

Adding another loop just to display brackets and parentheses made the program longer without improving the underlying game logic.

It was useful formatting practice, but I questioned whether it was really a better design.

This milestone reminded me that meeting a formatting requirement and improving software design are not necessarily the same thing.

---

## Milestone 4 — Six Attempts

The fourth milestone introduced a maximum of six guesses.

```python
NUM_ATTEMPTS = 6

for attempt in range(NUM_ATTEMPTS):
```

I used `break` to end the game when the player guessed correctly.

The `for`–`else` structure handled the losing condition.

The `else` block executed only when the loop finished without encountering `break`.

Because Python starts counting at zero, I used `attempt + 1` to display the correct number of guesses.

```python
if guess == secret_word:
    print(
        f"Congratulations! You guessed the word "
        f"in {attempt + 1} tries!"
    )
    break
```

### What I Learned

A `for` loop can manage a limited number of attempts.

I also learned that Python's `for`–`else` structure is useful when a program needs to distinguish between a successful early exit and a loop that finishes normally.

My Milestone 4 implementation was working before I started modifying it for Milestone 5.

---

## Milestone 5 — Polish

The final milestone introduced three requirements:

1. Use `get_random_word()` to select a different secret word.
2. Convert guesses to lowercase using `.lower()`.
3. Reject guesses that are not exactly five characters long without consuming an attempt.

### Capitalization

I used `.lower()` to normalize the player's input.

```python
guess = input("Enter your guess: ").lower()
```

This allows guesses such as `PLANT`, `Plant`, and `plant` to be evaluated the same way.

### Input Validation

I added a `while` loop inside the existing `for` loop.

```python
guess = input("Enter your guess: ").lower()

while len(guess) != 5:
    print("Please enter a 5-letter word.")
    guess = input("Enter your guess: ").lower()
```

This allows players to correct invalid guesses without losing one of their six attempts.

The validation checks the length of the input, as required by the milestone. It does not check whether the guess is a real English word.

### Random Word Selection

This requirement caused the most difficulty.

The instructions required the program to call:

```python
secret_word = get_random_word()
```

However, the function was not defined in the code I was working with.

Several attempts to resolve the missing function introduced additional problems.

A standalone implementation was eventually created using Python's built-in `random` library.

```python
import random

WORDS = ["place", "candy", "plant", "dance", "grape"]

def get_random_word():
    return random.choice(WORDS)
```

This implementation selects a random word and works independently of an external Wordle module.

However, it was not confirmed to be compatible with Stanford's automated testing environment.

---

## Debugging Problems and Frustrations

### 1. ChatGPT Repeatedly Misunderstood the Wordle Library

I repeatedly tried to explain the issue involving the Wordle library and the random-word function.

Instead of verifying the environment, ChatGPT kept changing its explanation and suggesting different imports.

At one point, it confused the module name with the function name.

I had to correct the assistant several times before it acknowledged what I was saying.

This made a relatively simple programming exercise unnecessarily frustrating.

### 2. ChatGPT Suggested Imports That Did Not Exist

One suggestion was:

```python
from wordle_words import get_random_word
```

That produced:

```text
ModuleNotFoundError: No module named 'wordle_words'
```

Another suggestion was:

```python
import wordle
```

That also failed:

```text
ModuleNotFoundError: No module named 'wordle'
```

ChatGPT repeatedly presented unverified imports as solutions.

These suggestions introduced new errors rather than resolving the original problem.

### What I Learned

An AI assistant should not confidently recommend a library or function without verifying that it exists in the actual programming environment.

I also learned that an import error is different from an error in the program's logic.

---

### 3. The Undefined Function

Another error occurred when the code called:

```python
secret_word = get_random_word()
```

Python returned:

```text
NameError: name 'get_random_word' is not defined
```

This meant the function had not been defined or imported.

Instead of identifying the correct source of the function, ChatGPT repeatedly suggested different approaches.

Eventually, it recommended defining a custom function using Python's built-in `random` library.

That resolved the undefined-function problem in the standalone program but did not establish compatibility with Stanford's automated tests.

---

### 4. ChatGPT Kept Rewriting Working Code

My Milestone 4 implementation already handled:

- Green matches
- Yellow matches
- Duplicate letters
- Formatted output
- Six attempts
- Winning and losing conditions

I wanted to add only the three requirements from Milestone 5.

Instead, ChatGPT repeatedly rewrote portions of the program, introduced additional code, and changed things that did not need to be changed.

I had to repost my existing code several times.

### What I Learned

When modifying an existing program, preserving working code is often better than rewriting everything.

A good debugging process should isolate the problem and make the smallest necessary correction.

---

### 5. The Automated Tests Expected a Specific Word

The Stanford checker displayed `"place"` as the expected secret word.

For example:

```text
Enter your guess: PLANT
Result: [p] [l] [a] n t

Enter your guess: place
Result: [p] [l] [a] [c] [e]

Congratulations! You guessed the word in 2 tries!
```

This created a conflict with the custom random-word implementation.

If the program randomly selected `"candy"` or `"grape"`, the expected guesses would not produce the same results.

The checker could continue requesting guesses instead of ending after the expected correct answer.

This may explain why the automated checking process sometimes appeared to run indefinitely.

However, the exact mechanism Stanford uses to control its test word was not verified.

---

### 6. The Temporary Hardcoded Word

To diagnose the automated testing issue, ChatGPT eventually suggested:

```python
def get_random_word():
    return "place"
```

This made the secret word match the expected output shown in the checker.

However, it also introduced a new problem.

The final milestone explicitly requires random word selection.

Returning `"place"` every time does not satisfy that requirement.

### What I Learned

A temporary debugging workaround is not necessarily a correct final solution.

Hardcoding a value can help isolate a problem, but it should not be mistaken for completing a requirement that calls for random behavior.

---

### 7. The EOFError

During testing, I also encountered:

```text
EOFError: EOF when reading a line
```

This happened when the program requested another guess but no additional input was available.

It was different from the import and undefined-function errors.

The error showed that the program was still waiting for input rather than necessarily failing in its letter-matching logic.

### What I Learned

It is important to distinguish between:

- Syntax and runtime errors
- Missing dependencies
- Problems with input
- Problems with program logic
- Problems with automated testing

Different errors require different solutions.

---

### 8. The Automated Checker Kept Running

At one point, the Stanford checker appeared to continue checking without finishing.

One possible explanation was that the program selected a random word that did not match the test's expected answer.

The test could then exhaust its supplied input while the program continued requesting guesses.

This was not conclusively verified.

The experience demonstrated that random behavior can make automated testing more complicated when the tests expect reproducible results.

---

### 9. I Had to Repeat Myself Too Many Times

The most frustrating part of this exercise was not learning Python.

It was repeatedly correcting ChatGPT about the same issue.

I asked for complete corrected code multiple times.

Instead, I received more incorrect suggestions, unverified imports, and explanations that did not resolve the actual problem.

I repeatedly explained what was wrong, shared the same code, and provided error messages from Stanford's checker.

ChatGPT continued making assumptions rather than identifying the missing information.

The debugging process became significantly longer and more frustrating than the original assignment.

---

## What I Learned About Using AI for Programming

### AI-Generated Code Is Not Automatically Correct

A solution can look complete, contain detailed comments, and still fail immediately.

### Error Messages Matter More Than Confident Explanations

The `NameError` and `ModuleNotFoundError` messages provided concrete information about what was failing.

The assistant's explanations were not always consistent with those errors.

### Working Code Should Be Preserved

My original Milestone 4 implementation was functional.

The final milestone should have involved targeted modifications rather than repeated rewrites.

### Dependencies Need to Be Verified

An import statement is only useful if the module and function actually exist in the environment.

### Randomness Complicates Automated Testing

A randomly selected word may produce different results each time a program runs.

Automated tests often need a predictable way to control or reproduce those results.

### Readability Matters

More code, more loops, and more abstraction do not necessarily produce a better beginner program.

### AI Assistance Requires Human Judgment

I had to identify inconsistencies, question proposed solutions, interpret errors, and repeatedly redirect the assistant toward the actual requirements.

---

## Project Status

| Milestone | Status |
|-----------|--------|
| 1. Exact Matches | Implemented |
| 2. Yellow Matches | Implemented |
| 3. Format the Output | Implemented |
| 4. Six Attempts | Implemented |
| 5. Capitalization | Implemented |
| 5. Input Validation | Implemented |
| 5. Random Word Selection | Implemented in standalone version |
| 5. Stanford Autograder | Not yet verified as passing |

The core game logic is implemented.

The remaining issue is confirming that random word selection works with Stanford's expected testing mechanism.

The temporary hardcoded `"place"` version is a diagnostic workaround, not a completed random-word solution.

---

## Final Reflection

Wordle was a useful exercise in loops, lists, conditional logic, string manipulation, input validation, and debugging.

The most interesting programming concepts were handling duplicate letters, using `for`–`else`, and preventing invalid guesses from consuming an attempt.

The most frustrating experience was debugging with ChatGPT.

I spent more time correcting the assistant's assumptions about the Wordle library than understanding the actual Python logic.

The assistant repeatedly introduced errors, misunderstood corrections, and failed to preserve working code.

I also learned that an AI assistant can continue offering plausible explanations even when it does not have enough information to identify the correct solution.

**The most important thing from this exercise is that understanding my own code matters more than accepting an AI-generated answer.**

I can use AI to explain concepts, suggest approaches, and help debug problems, but I still need to verify its claims and recognize when its suggestions are making a problem worse.

The experience reinforced the importance of reading error messages, preserving working code, testing changes individually, and maintaining independent judgment when using AI-assisted programming.

Although the standalone Wordle implementation was completed, the final Stanford autograder result remained unresolved at the time of writing.
