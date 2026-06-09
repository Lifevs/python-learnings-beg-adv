# 🎓 Python Learning Journey

This log tracks a structured curriculum derived from daily practice sessions, coding projects, and comprehensive knowledge checks.

---

## 🟢 Day 1: Python Foundations & Type System
*Focus: Getting started, basic syntax, and how Python handles data.*

### 1. Variables & Syntax Basics
- **Variable Declaration**: Declared simply as `name = value`.
- **Naming Rules**: Must start with a letter or underscore; case-sensitive; avoid reserved keywords.
- **Best Practice**: Use descriptive names rather than single letters.

### 2. Output & Basic Types
- **The `print()` Function**: Separating values with commas automatically inserts a space.
- **Dynamic Typing**: Python automatically detects data types.
- **Type Inspection**: Use `type()` to identify the class and `isinstance()` for specific checks.

### 🧠 Day 1 Knowledge Check
<details>
<summary><b>Q1: How do you declare a variable in Python?</b></summary>

Variables are declared using the assignment operator `=`.
![Variable Quiz](Screenshot%202026-05-27%20at%2011.39.47%E2%80%AFAM.png)
</details>

<details>
<summary><b>Q2: What are the key naming rules for variables?</b></summary>

Must start with a letter/underscore, case-sensitive, no keywords.
![Naming Rules](Screenshot%202026-05-27%20at%2011.39.52%E2%80%AFAM.png)
</details>

---

## 🟡 Day 2: String Mastery & Manipulation
*Focus: Deep dive into text processing and formatting.*

### 1. String Properties
- **Immutability**: Strings cannot be modified in place.
- **Length**: Measured using the built-in `len()` function.
- **Multiline Text**: Defined using triple quotes (`"""` or `'''`).

### 2. Formatting & Methods
- **Concatenation**: Joining strings using the `+` operator.
- **Interpolation**: Embedding variables directly into strings.
- **Essential Methods**: `upper()`, `lower()`, `replace()`, and `str()` for conversion.

### 🧠 Day 2 Knowledge Check
<details>
<summary><b>Q1: How do you find the length of a string?</b></summary>

Use the `len()` function.
![Length Quiz](Screenshot%202026-05-28%20at%205.20.49%E2%80%AFPM.png)
</details>

<details>
<summary><b>Q2: Can you change a specific character in a string?</b></summary>

No, strings are **immutable**.
![Immutability](Screenshot%202026-05-28%20at%205.21.10%E2%80%AFPM.png)
</details>

---

## 🔴 Day 3: Numbers, Operators & Career Research
*Focus: Mathematical logic, efficiency, and real-world goals.*

### 1. Numeric Logic & Operators
- **Floor Division (`//`)**: Divides and rounds down to the nearest whole number.
- **Absolute Values**: Retrieved via the `abs()` function.
- **Augmented Assignment**: Shortcuts like `+=`, `-=`, and `**=`.
- **Note**: Python uses `x += 1` instead of `x++`.

### 2. Career Strategy
- **Research**: Analyzed **Full Stack AI Engineer** internship requirements.

### 🧠 Day 3 Knowledge Check
<details>
<summary><b>Q1: What is the difference between / and //?</b></summary>

`/` is float division, `//` is floor division (rounds down).
![Division Quiz](Screenshot%202026-05-28%20at%206.56.09%E2%80%AFPM.png)
</details>

---

## 🔵 Day 4: Logic, Control Flow & Booleans
*Focus: Mastering decision-making logic and building interactive applications.*

### 1. Booleans & Comparison Operators
- **Boolean Logic**: Represents one of two states: `True` or `False`.
- **Comparison Operators**: Used to compare two values (`==`, `!=`, `>`, `<`, `>=`, `<=`).

### 2. Control Flow (`if`, `elif`, `else`)
- **Indentation**: Python relies on consistent whitespace to define code blocks.

### 🧠 Day 4 Knowledge Check
<details>
<summary><b>Q1: What does 'Short-Circuiting' mean in logical operations?</b></summary>

In an `or` expression, if the first value is `True`, Python skips evaluating the second value.
![Efficiency Logic](day-4/Screenshot%202026-06-01%20at%206.53.43%E2%80%AFPM.png)
</details>

---

## 🟣 Day 5: Advanced Conditionals & Practical Planning
*Focus: Applying complex logical chains to real-world scenarios.*

### 1. Complex Conditional Logic
- **Decision Trees**: Structured multiple `if`, `elif`, and `else` blocks to evaluate layered conditions.

### 🧠 Day 5 Knowledge Check
<details>
<summary><b>Q1: How do you structure a decision tree for a travel planner?</b></summary>

Check distance, then weather, then availability of transport.
![FCC Weather Planner](day-5/Screenshot%202026-06-03%20at%203.12.37%E2%80%AFPM.png)
</details>

---

## ⚪ Day 6: Environment Setup & Installation
*Focus: Preparing the development foundation on Windows.*

### 1. Installation Essentials
- **Official Source**: Always download Python from [python.org](https://python.org).
- **PATH Variable**: Crucial to check **"Add Python to PATH"** during installation for command-line access.

### 🧠 Day 6 Knowledge Check
<details>
<summary><b>Q1: How can you get Python added to path automatically on Windows?</b></summary>

By checking the **"add to path"** checkbox during the installation process.
![Add to PATH](day-6/Screenshot%202026-06-04%20at%206.59.14%E2%80%AFPM.png)
</details>

---

## 🟤 Day 7: Interactive Scripting & Terminal Execution
*Focus: Transitioning from code snippets to functional terminal applications.*

### 1. Terminal Interaction
- **The `input()` Function**: Allows capturing user data directly from the terminal. Note: Always returns data as a **string**.
- **Script Execution**: Running files via `python main.py` or `python3 main.py`.

### 🧠 Day 7 Knowledge Check
<details>
<summary><b>Q1: What data type does the input() function return by default?</b></summary>

It always returns a **string**, even if the user enters a number.
![Input Logic](day-7/Screenshot%202026-06-05%20at%208.22.28%E2%80%AFPM.png)
</details>

---

## 🏁 Day 8: The Ultimate Python Basics Quiz
*Focus: Validating foundational knowledge and environment mastery.*

### 1. The Python Ecosystem
- **Official Source**: Downloading from `python.org`.
- **Development Tools**: Understanding IDEs like VS Code and PyCharm.
- **Terminal Proficiency**: Differentiating between the system terminal and the Python interactive shell.

### 2. Mastering the REPL
- **REPL**: Stands for **Read-Evaluate-Print Loop**.
- **The Prompt**: The `>>>` symbol indicates Python is ready for input.

### 🧠 Day 8 Knowledge Check
<details>
<summary><b>Q1: What command starts the Python interactive shell?</b></summary>

Simply typing `python` in the terminal and pressing enter.
![Shell Command](day-8/Screenshot%202026-06-07%20at%2010.46.01%E2%80%AFPM.png)
</details>

<details>
<summary><b>Q2: What does REPL stand for?</b></summary>

**Read-Evaluate-Print Loop**.
![REPL Review](day-8/Screenshot%202026-06-07%20at%2010.47.53%E2%80%AFPM.png)
</details>

---
*Documentation structured for optimal learning retention.*
