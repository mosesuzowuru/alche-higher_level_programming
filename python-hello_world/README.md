# Python - Hello, World

This directory contains introductory Python programming exercises focusing on basic syntax, string manipulation, and script execution.

## Learning Objectives

At the end of this project, you should be able to explain:
- How to use the Python interpreter
- How to print text and variables using print()
- How to use strings and string formatting
- What are f-strings and how to use them
- How to use string slicing and indexing
- The official Python coding style and how to check your code with pycodestyle

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the repo, containing a description of the repository
- Your code should use pycodestyle (version 2.8.*)
- All files must be executable
- The length of your files will be tested using `wc`

### Shell Scripts
- Allowed editors: vi, vim, emacs
- All scripts will be tested on Ubuntu 20.04 LTS
- All scripts should be exactly two lines long (`wc -l file` should print 2)
- All files should end with a new line
- The first line of all files should be exactly `#!/bin/bash`
- All files must be executable

## Tasks

### 0. Run Python file
**File:** `0-run`

Write a Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE`.

**Usage:**
```bash
export PYFILE=main.py
./0-run
```

### 1. Run inline
**File:** `1-run_inline`

Write a Shell script that runs Python code. The Python code will be saved in the environment variable `$PYCODE`.

**Usage:**
```bash
export PYCODE='print(f"Best School: {88+10}")'
./1-run_inline
```

### 2. Hello, print
**File:** `2-print.py`

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle` followed by a new line.

**Requirements:**
- Use the function `print`

### 3. Print integer
**File:** `3-print_number.py`

Complete this source code to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

**Requirements:**
- You are not allowed to cast the variable `number` into a string
- Your code must be 3 lines long
- You have to use f-strings

### 4. Print float
**File:** `4-print_float.py`

Complete the source code to print the float stored in the variable `number` with a precision of 2 digits.

**Requirements:**
- The output should be: `Float:` followed by the float with only 2 digits
- You are not allowed to cast `number` to string
- You have to use f-strings

### 5. Print string
**File:** `5-print_string.py`

Complete this source code to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

**Requirements:**
- You are not allowed to use any loops or conditional statements
- Your program should be maximum 5 lines long

### 6. Play with strings
**File:** `6-concat.py`

Complete this source code to print `Welcome to Holberton School!`

**Requirements:**
- You are not allowed to use any loops or conditional statements
- You have to use the variables `str1` and `str2` in your new line of code
- Your program should be exactly 5 lines long

### 7. Copy - Cut - Paste
**File:** `7-edges.py`

Complete this source code for string slicing operations.

**Requirements:**
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- `word_first_3` should contain the first 3 letters of the variable `word`
- `word_last_2` should contain the last 2 letters of the variable `word`
- `middle_word` should contain the value of the variable `word` without the first and last letters

### 8. Create a new sentence
**File:** `8-concat_edges.py`

Complete this source code to print `object-oriented programming with Python`, followed by a new line.

**Requirements:**
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

### 9. Easter Egg
**File:** `9-easter_egg.py`

Write a Python script that prints "The Zen of Python", by Tim Peters, followed by a new line.

**Requirements:**
- Your script should be maximum 98 characters long (check with `wc -m 9-easter_egg.py`)

## How to Run

### Shell Scripts
Make the scripts executable and run them:
```bash
chmod +x 0-run
chmod +x 1-run_inline
```

### Python Scripts
Make the scripts executable and run them:
```bash
chmod +x 2-print.py
./2-print.py
```

Or run with python3:
```bash
python3 2-print.py
```

## Testing

You can test your scripts using the provided examples in each task description. Make sure to:

1. Check that shell scripts are exactly 2 lines long:
   ```bash
   wc -l 0-run
   ```

2. Check that Python scripts meet the line requirements:
   ```bash
   wc -l 6-concat.py
   ```

3. Check character count for the easter egg:
   ```bash
   wc -m 9-easter_egg.py
   ```

## Repository Structure

```
alche-higher_level_programming/
└── python-hello_world/
    ├── README.md
    ├── 0-run
    ├── 1-run_inline
    ├── 2-print.py
    ├── 3-print_number.py
    ├── 4-print_float.py
    ├── 5-print_string.py
    ├── 6-concat.py
    ├── 7-edges.py
    ├── 8-concat_edges.py
    └── 9-easter_egg.py
```

## Author

This project is part of the ALX Higher Level Programming curriculum.
