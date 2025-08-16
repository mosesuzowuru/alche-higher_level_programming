# Python - import & modules

This directory contains Python programming exercises focusing on importing modules, functions, and variables.

## Learning Objectives

At the end of this project, you should be able to explain:
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function dir()
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use pycodestyle (version 2.8.*)
- All files must be executable
- The length of your files will be tested using `wc`

## Tasks

### 0. Import a simple function from a simple file
**File:** `0-add.py`

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

**Requirements:**
- You have to use print function with string format to display integers
- You have to assign: the value 1 to a variable called a, the value 2 to a variable called b
- You can only use the word add_0 once in your code
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported

### 1. My first toolbox!
**File:** `1-calculation.py`

Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

**Requirements:**
- Do not use the function print more than 4 times
- You have to define: the value 10 to a variable a, the value 5 to a variable b
- Your program should call each of the imported functions
- The word calculator_1 should be used only once in your file
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported

### 2. How to make a script dynamic!
**File:** `2-args.py`

Write a program that prints the number of and the list of its arguments.

**Requirements:**
- The number of elements of argv can be retrieved by using: len(argv)
- Your code should not be executed when imported
- Handle different output formats based on number of arguments

### 3. Infinite addition
**File:** `3-infinite_add.py`

Write a program that prints the result of the addition of all arguments.

**Requirements:**
- You can cast arguments into integers by using int()
- Your code should not be executed when imported
- Should handle big numbers

### 4. Who are you?
**File:** `4-hidden_discovery.py`

Write a program that prints all the names defined by the compiled module `hidden_4.pyc`.

**Requirements:**
- You should print one name per line, in alpha order
- You should print only names that do not start with __
- Your code should not be executed when imported

### 5. Everything can be imported
**File:** `5-variable_load.py`

Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

**Requirements:**
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported

## How to Run

### Basic execution
```bash
./0-add.py
./1-calculation.py
```

### With command line arguments
```bash
./2-args.py Hello World
./3-infinite_add.py 79 10 -40 -300 89
```

### Discovery and variable loading
```bash
./4-hidden_discovery.py
./5-variable_load.py
```

## Repository Structure

```
alche-higher_level_programming/
└── python-import_modules/
    ├── README.md
    ├── add_0.py              # Helper file for task 0
    ├── calculator_1.py       # Helper file for task 1
    ├── variable_load_5.py    # Helper file for task 5
    ├── hidden_4.pyc          # Compiled module for task 4
    ├── 0-add.py
    ├── 1-calculation.py
    ├── 2-args.py
    ├── 3-infinite_add.py
    ├── 4-hidden_discovery.py
    └── 5-variable_load.py
```

## Testing

### Test Task 0
```bash
./0-add.py
# Expected output: 1 + 2 = 3
```

### Test Task 1
```bash
./1-calculation.py
# Expected output:
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2
```

### Test Task 2
```bash
./2-args.py
# Expected: 0 arguments.

./2-args.py Hello
# Expected: 1 argument:
#           1: Hello

./2-args.py Hello World Test
# Expected: 3 arguments:
#           1: Hello
#           2: World
#           3: Test
```

### Test Task 3
```bash
./3-infinite_add.py
# Expected: 0

./3-infinite_add.py 79 10
# Expected: 89
```

### Test Task 5
```bash
./5-variable_load.py
# Expected: 98
```

## Notes

- All scripts use `if __name__ == "__main__":` to prevent execution when imported
- Helper files (`add_0.py`, `calculator_1.py`, `variable_load_5.py`) are provided
- `hidden_4.pyc` needs to be downloaded separately for Task 4
- All imports follow the specific requirements (no * imports, no __import__)

## Author

This project is part of the ALX Higher Level Programming curriculum.
