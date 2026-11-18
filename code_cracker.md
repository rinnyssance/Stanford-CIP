Here is the Markdown version for your **Code Machine assignment**, including how you used AI and the mistakes it made.

\# Code Machine — Stanford Code in Place X\
\
\## How I Used AI\
\
I used ChatGPT as a programming assistant while completing the Code Machine assignment for Stanford Code in Place X.\
\
The assignment involved building a Caesar cipher program across four milestones:\
\
1\. \*\*One Letter:\*\* Shift a single letter through the alphabet.\
2\. \*\*A Whole Message:\*\* Encode an entire message.\
3\. \*\*Decode:\*\* Reverse the encryption to recover the original message.\
4\. \*\*Crack It:\*\* Try all 25 possible shifts to identify a secret message.\
\
I used ChatGPT to review my Python code, understand the assignment requirements, debug errors, and add explanatory comments.\
\
\## Python Concepts Practiced\
\
\- Functions and function calls\
\- \`for\` loops\
\- String indexing\
\- String concatenation\
\- Conditional statements\
\- Modulo arithmetic (\`%\`)\
\- Negative numbers\
\- The \`range()\` function\
\- Debugging and automated testing\
\
\## How ChatGPT Helped\
\
ChatGPT explained how Caesar ciphers work and how modulo arithmetic allows letters to wrap around the alphabet.\
\
For example, shifting \`z\` forward by three positions produces \`c\`.\
\
It also helped me understand how the functions build on one another:\
\
\- \`encode()\` calls \`shift_letter()\`.\
\- \`decode()\` calls \`encode()\`.\
\- \`crack()\` calls \`decode()\`.\
\
I used ChatGPT to add comments explaining each part of the program and to implement the final milestone, which required testing all 25 possible shifts.\
\
\## ChatGPT's Mistakes\
\
\### 1. Missing the Decoding Requirement\
\
ChatGPT initially provided a version of my program that only encoded messages.\
\
However, Stanford's automated checker expected the program to display both the encoded and decoded messages.\
\
The tests failed because the program never printed the required \`Decoded:\` line.\
\
I had to share the failed test results before ChatGPT identified the missing functionality.\
\
\### 2. Making Assumptions About My Code\
\
When I pasted my existing program, ChatGPT assumed that repeated copies of the code might be present in my actual Python file.\
\
That was not established.\
\
The assistant should have distinguished between a possible formatting issue in my message and a confirmed problem in my program.\
\
\### 3. Not Identifying the Current Milestone\
\
ChatGPT initially responded to my code without establishing which milestone Stanford was currently testing.\
\
As a result, it supplied a solution that did not meet the requirements shown by the automated checker.\
\
This created unnecessary additional debugging.\
\
\## How I Verified the AI's Suggestions\
\
I compared ChatGPT's suggestions against the assignment instructions and Stanford's automated test results.\
\
When the checker reported that the decoded output was missing, I shared the expected and observed outputs with ChatGPT.\
\
I also checked whether the suggested code followed the required function structure rather than introducing unnecessary changes.\
\
The final \`crack()\` implementation was written to print all 25 possible decoded messages, although I had not yet confirmed its final autograder result.\
\
\## What I Learned\
\
The assignment helped me understand how functions can work together to solve increasingly complex problems.\
\
I also learned that reversing a Caesar cipher does not require an entirely new encryption algorithm. The existing \`encode()\` function can be reused with a negative shift.\
\
The debugging process reinforced the importance of checking expected output, preserving working code, and making targeted changes.\
\
\## Final Reflection\
\
ChatGPT was useful for explaining Python concepts, reviewing code, and helping me understand how to build a Caesar cipher.\
\
However, it also made mistakes that required me to review its suggestions and provide additional information.\
\
\*\*The most important thing from this assignment is that AI-generated code still needs to be understood and tested.\*\*\
\
I used ChatGPT as a learning and debugging tool rather than treating its answers as automatically correct. The experience helped me strengthen my understanding of Python while practicing independent judgment when working with AI.\
