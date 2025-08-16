# Python - if/else, loops, functions

This directory contains Python programming exercises focusing on conditional statements, loops, and functions.

## Learning Objectives

At the end of this project, you should be able to explain:
- How to use if, if ... else statements
- How to use comments
- How to affect values to variables
- How to use while and for loops
- How to use break and continue statements
- How to use else clauses on loops
- What does the pass statement do, and when to use it
- How to use range
- What is a function and how do you use functions
- What does return a function that does not use any return statement
- Scope of variables
- What's a traceback
- What are the arithmetic operators and how to use them

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

### 0. Positive anything is better than negative nothing
**File:** `0-positive_or_negative.py`

This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

### 1. The last digit
**File:** `1-last_digit.py`

This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
**File:** `2-print_alphabet.py`

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

**Requirements:**
- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

### 3. When I was having that alphabet soup, I never thought that it would pay off
**File:** `3-print_alphabt.py`

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

**Requirements:**
- Print all the letters except q and e
- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

### 4. Hexadecimal printing
**File:** `4-print_hexa.py`

Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal.

**Requirements:**
- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

### 5. 00...99
**File:** `5-print_comb2.py`

Write a program that prints numbers from 0 to 99.

**Requirements:**
- Numbers must be separated by `,`, followed by a space
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

### 6. Inventing is a combination of brains and materials
**File:** `6-print_comb3.py`

Write a program that prints all possible different combinations of two digits.

**Requirements:**
- Numbers must be separated by `,`, followed by a space
- The two digits must be different
- 01 and 10 are considered the same combination of the two digits 0 and 1
- Print only the smallest combination of two digits
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 3 print functions with string format
- You can only use no more than 2 loops in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

### 7. islower
**File:** `7-islower.py`

Write a function that checks for lowercase character.

**Prototype:** `def islower(c):`
- Returns True if c is lowercase
- Returns False otherwise
- You are not allowed to import any module
- You are not allowed to use str.upper() and str.isupper()
- Tips: ord()

### 8. To uppercase
**File:** `8-uppercase.py`

Write a function that prints a string in uppercase followed by a new line.

**Prototype:** `def uppercase(str):`
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to import any module
- You are not allowed to use str.upper() and str.isupper()
- Tips: ord()

### 9. There are only 3 colors, 10 digits, and 7 notes
**File:** `9-print_last_digit.py`

Write a function that prints the last digit of a number.

**Prototype:** `def print_last_digit(number):`
- Returns the value of the last digit
- You are not allowed to import any module

### 10. a + b
**File:** `10-add.py`

Write a function that adds two integers and returns the result.

**Prototype:** `def add(a, b):`
- Returns the value of a + b
- You are not allowed to import any module

### 11. a ^ b
**File:** `11-pow.py`

Write a function that computes a to the power of b and return the value.

**Prototype:** `def pow(a, b):`
- Returns the value of a ^ b
- You are not allowed to import any module

### 12. Fizz Buzz
**File:** `12-fizzbuzz.py`

Write a function that prints the numbers from 1 to 100 separated by a space.

**Prototype:** `def fizzbuzz():`
- For multiples of three print Fizz instead of the number
- For multiples of five print Buzz
- For numbers which are multiples of both three and five print FizzBuzz
- Each element should be followed by a space
- You are not allowed to import any module

## Repository Structure

```
alche-higher_level_programming/
└── python-if_else_loops_functions/
    ├── README.md
    ├── 0-positive_or_negative.py
    ├── 1-last_digit.py
    ├── 2-print_alphabet.py
    ├── 3-print_alphabt.py
    ├── 4-print_hexa.py
    ├── 5-print_comb2.py
    ├── 6-print_comb3.py
    ├── 7-islower.py
    ├── 8-uppercase.py
    ├── 9-print_last_digit.py
    ├── 10-add.py
    ├── 11-pow.py
    └── 12-fizzbuzz.py
```

## Author

This project is part of the ALX Higher Level Programming curriculum.
