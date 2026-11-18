# Wordle — Stanford Code in Place X

## Project Overview

For this exercise, I built a Python version of Wordle across five milestones. The goal was to create a word-guessing game that compares letters, identifies correct and misplaced matches, formats results, limits attempts, and selects a random secret word.

### Python Concepts Practiced

- `for` and `while` loops
- Lists and string indexing
- Conditional statements
- Functions and imports
- String formatting
- `.lower()`
- `break`
- `for`–`else`
- Input validation
- Debugging Python errors

---

## Milestone 1 — Exact Matches

The first milestone involved comparing a five-letter guess against the secret word `"candy"`.

I used a `for` loop to compare each letter at the same index.

- `G` represented a correct letter in the correct position.
- `B` represented a letter that did not match at that position.

**What I learned:** String indexing allows me to compare corresponding characters in two words.

## Milestone 2 — Yellow Matches

The second milestone introduced `Y` for letters that appeared in the secret word but were in the wrong position.

I created a list called `remaining_letters` to track letters that had not already been matched.

The solution used two loops:

1. Identify green matches and remove those letters from `remaining_letters`.
2. Check unmatched letters for yellow matches and remove them as they were used.

This prevented duplicate letters from being counted more times than they appeared in the secret word.

**What I learned:** The order of operations matters. Checking green matches before yellow matches helps handle repeated letters correctly.

## Milestone 3 — Formatting Results

The third milestone required replacing the simple `G`, `Y`, and `B` output with formatted letters.

- Green: `[a]`
- Yellow: `(a)`
- Black: `a`

This required another loop and a `formatted_result` list.

**My observation:** I actually preferred the original `G`, `Y`, and `B` markers. They were straightforward and easy to understand.

Adding another loop just to display brackets and parentheses made the program longer without improving the underlying game logic.

It was useful formatting practice, but I questioned whether it was really a better design.

## Milestone 4 — Six Attempts

The fourth milestone introduced a maximum of six guesses.

```python
NUM_ATTEMPTS = 6

for attempt in range(NUM_ATTEMPTS):
```

I used `break` to end the game when the player guessed correctly.

The `for`–`else` structure handled the losing condition. The `else` block executed only when the loop finished without encountering `break`.

Because Python starts counting at zero, I used `attempt + 1` to display the correct number of attempts.

**What I learned:** A `for` loop can manage a limited number of attempts, and its `else` clause can handle what happens when no successful guess occurs.

## Milestone 5 — Polish

The final milestone introduced three requirements:

1. Select a different secret word using `get_random_word()`.
2. Convert guesses to lowercase using `.lower()`.
3. Reject guesses that are not exactly five characters long without using an attempt.

The input validation required a `while` loop inside the existing `for` loop.

```python
guess = input("Enter your guess: ").lower()

while len(guess) != 5:
    print("Please enter a 5-letter word.")
    guess = input("Enter your guess: ").lower()
```

This allowed the player to correct an invalid guess without losing one of the six attempts.

Unfortunately, the random-word requirement became the most frustrating part of the exercise.

---

## Debugging Problems and Frustrations

### 1. ChatGPT Repeatedly Misunderstood the Wordle Library

I repeatedly tried to explain that the exercise involved Wordle and that the import needed to come from the appropriate library.

Instead of verifying the environment, ChatGPT kept changing its explanation and suggesting different function names and imports.

At one point, it confused the name of the library with the name of the function.

This wasted time and made a relatively simple exercise unnecessarily complicated.

### 2. ChatGPT Invented Imports That Did Not Work

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

The assistant repeatedly presented unverified imports as solutions.

**My observation:** An AI assistant should not confidently recommend a library or function without knowing whether it exists in the actual programming environment.

### 3. The Undefined `get_random_word()` Function

Another error occurred when the code called:

```python
secret_word = get_random_word()
```

Python returned:

```text
NameError: name 'get_random_word' is not defined
```

Instead of identifying the correct source of the function, ChatGPT kept cycling through possible solutions.

Eventually, it suggested defining a custom function using Python's built-in `random` library.

That made the game runnable as a standalone program, but it did not establish that the solution would satisfy Stanford's automated tests.

### 4. ChatGPT Kept Rewriting Code That Already Worked

My Milestone 4 implementation was functional.

I wanted to add only the three requirements from Milestone 5.

Instead, ChatGPT repeatedly supplied alternative implementations, introduced additional code, and changed things that did not need to be changed.

I had to keep reposting my existing code to establish what I was actually working with.

**My observation:** When modifying an existing program, preserving working code is often better than rewriting everything.

### 5. The Automated Tests Expected a Specific Word

The Stanford tests showed `"place"` as the expected secret word.

For example:

```text
Enter your guess: PLANT
Result: [p] [l] [a] n t

Enter your guess: place
Result: [p] [l] [a] [c] [e]

Congratulations! You guessed the word in 2 tries!
```

This raised an important question about how the testing environment controlled the random-word function.

ChatGPT suggested creating a custom list of words and selecting one randomly, but this could conflict with the test's expected output.

The correct integration with Stanford's intended helper remained unverified during our debugging session.

### 6. The EOFError

During testing, I also encountered:

```text
EOFError: EOF when reading a line
```

This happened when the program requested another guess but no additional input was available.

This was different from the import and undefined-function errors.

It demonstrated why it is important to distinguish between problems in program logic, problems with dependencies, and problems with the execution environment.

### 7. I Had to Repeat Myself Too Many Times

The most frustrating part was not the Python itself.

It was repeatedly correcting ChatGPT about the same issue, asking for complete code, receiving another incorrect solution, and then having to explain the problem again.

I explicitly asked for the entire corrected program multiple times.

Instead of resolving the uncertainty about the library, ChatGPT continued guessing.

The debugging process became longer and more aggravating than the original assignment.

---

## What I Learned About Using AI for Programming

### AI-Generated Code Is Not Automatically Correct

A solution can look complete, contain detailed comments, and still fail immediately.

### Error Messages Are More Useful Than Confident Explanations

The `NameError` and `ModuleNotFoundError` clearly identified problems that the assistant's repeated assumptions did not resolve.

### Working Code Should Be Preserved

My existing solution already handled matching, formatting, and attempt counting.

The final milestone should have required only targeted modifications.

### Dependencies Need to Be Verified

An import statement is only useful if the module and function actually exist in the execution environment.

### Readability Matters

More code, more loops, and more abstraction do not necessarily produce a better beginner program.

### AI Assistance Still Requires Human Judgment

I had to identify inconsistencies, question proposed solutions, and repeatedly redirect the assistant toward the actual requirements.

---

## Final Reflection

Wordle was a useful exercise in loops, lists, conditional logic, string manipulation, and input validation.

The most interesting programming concepts were handling duplicate letters, using `for`–`else`, and preventing invalid guesses from consuming an attempt.

The most frustrating experience was debugging with ChatGPT.

I spent more time correcting the assistant's assumptions about the Wordle library than understanding the actual Python logic.

The assistant repeatedly introduced errors, misunderstood corrections, and failed to preserve the working solution I had already provided.

**The most important thing from this exercise is that understanding my own code matters more than accepting an AI-generated answer.**

I can use AI to explain concepts, suggest approaches, and help debug problems, but I still need to verify its claims and recognize when its suggestions are making a problem worse.

The standalone game logic was completed, although compatibility with Stanford's expected random-word helper was not conclusively verified during our debugging session.
