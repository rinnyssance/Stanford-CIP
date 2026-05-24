# Haiku Generator Using AI

## Assignment

Write a program that creates a haiku using AI.

A haiku is a short poem with three lines:

- Line 1: 5 syllables
- Line 2: 7 syllables
- Line 3: 5 syllables

Haiku often describe nature, feelings, or quiet moments using simple imagery.

---

# Goal of the Program

The program should ask the user for:

1. Their name
2. A topic for the haiku

Then the program should use `call_gpt` to create a haiku based on the name and topic.

---

# Example Run

```text
Enter your name: Freya
Enter a topic: Rain in the forest
Creating your haiku...

Freya roams the woods,
Whispers dance with gentle rain,
Nature's song remains.
```

---

# What the Program Needs to Do

1. Ask the user to enter their name.
2. Ask the user to enter a topic.
3. Print `"Creating your haiku..."`
4. Create a prompt for the AI.
5. Use `call_gpt` to generate the haiku.
6. Print the haiku.

---

# Important Notes

The AI prompt should clearly tell GPT what to create.

The prompt should include:

- The user's name
- The topic
- Instructions that the poem should be a haiku
- Instructions that the poem should have 3 lines
- Instructions that the syllable pattern should be 5-7-5

---

# My Understanding

This exercise is about combining user input with AI.

Instead of writing the haiku myself, I collect information from the user and send that information into `call_gpt()`.

The most important part of this exercise is learning how to create a clear AI prompt.

---

# Pseudocode

```text
Ask the user for their name
Ask the user for a topic
Print "Creating your haiku..."

Create a prompt using the name and topic

Send the prompt to call_gpt()

Print the haiku
```

---

# Things to Remember

- `input()` collects information from the user.
- Variables store the user's answers.
- The prompt is the instruction sent to AI.
- `call_gpt()` generates the response.
- `print()` displays the result.

---

# Reflection

This exercise helps me practice:

- Using user input
- Working with variables
- Creating prompts for AI
- Displaying generated text

It also teaches me that AI works best when instructions are clear and specific.
