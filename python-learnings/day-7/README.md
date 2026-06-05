# 🟤 Day 7: Interactive Scripting & Terminal Execution

Transitioning from writing code snippets to building functional terminal applications.

## 🛠️ Featured Project: Interactive Terminal Script

The `main.py` script demonstrates how to capture user input and provide dynamic feedback directly through the terminal interface.

### Key Concepts:
1.  **Capturing Input**: Using `input("Prompt text")` to wait for user data.
2.  **Type Conversion**: Handling the fact that `input()` returns a string (e.g., converting to `int` or `float` if needed).
3.  **Terminal Execution**: Understanding how to run scripts using the command line.

---

## 🧠 Project Knowledge Checks

<details>
<summary><b>Q1: What happens if you try to perform math on an input() result without conversion?</b></summary>

It will cause a `TypeError` because `input()` returns a string. You must use `int()` or `float()`.
![Input Logic](Screenshot%202026-06-05%20at%208.22.28 PM.png)
</details>

<details>
<summary><b>Q2: What is the standard command to run this script?</b></summary>

`python main.py` or `python3 main.py`.
![Terminal Execution](Screenshot%202026-06-05%20at%208.22.34 PM.png)
</details>

<details>
<summary><b>Q3: How can you make the terminal output more readable?</b></summary>

By using f-strings or adding newline characters (`\n`) for spacing.
![Scripting Result](Screenshot%202026-06-05%20at%208.22.45 PM.png)
</details>
