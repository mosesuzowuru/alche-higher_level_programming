# Python - Classes and Objects

This directory contains Python programming exercises focusing on object-oriented programming concepts like classes, objects, attributes, and methods.

## Learning Objectives

At the end of this project, you should be able to explain:
- What is OOP
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python

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
- All modules should have documentation
- All classes should have documentation
- All functions (inside and outside a class) should have documentation

## Tasks

### 0. My first square
**File:** `0-square.py`

Write an empty class Square that defines a square.

- You are not allowed to import any module

### 1. Square with size
**File:** `1-square.py`

Write a class Square that defines a square by: (based on 0-square.py)

- Private instance attribute: size
- Instantiation with size (no type/value verification)
- You are not allowed to import any module

### 2. Size validation
**File:** `2-square.py`

Write a class Square that defines a square by: (based on 1-square.py)

- Private instance attribute: size
- Instantiation with optional size: `def __init__(self, size=0):`
- size must be an integer, otherwise raise a TypeError exception with the message `size must be an integer`
- if size is less than 0, raise a ValueError exception with the message `size must be >= 0`
- You are not allowed to import any module

### 3. Area of a square
**File:** `3-square.py`

Write a class Square that defines a square by: (based on 2-square.py)

- Private instance attribute: size
- Instantiation with optional size: `def __init__(self, size=0):`
- size must be an integer, otherwise raise a TypeError exception with the message `size must be an integer`
- if size is less than 0, raise a ValueError exception with the message `size must be >= 0`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

### 4. Access and update private attribute
**File:** `4-square.py`

Write a class Square that defines a square by: (based on 3-square.py)

- Private instance attribute: size:
  - property `def size(self):` to retrieve it
  - property setter `def size(self, value):` to set it:
    - size must be an integer, otherwise raise a TypeError exception with the message `size must be an integer`
    - if size is less than 0, raise a ValueError exception with the message `size must be >= 0`
- Instantiation with optional size: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

### 5. Printing a square
**File:** `5-square.py`

Write a class Square that defines a square by: (based on 4-square.py)

- Private instance attribute: size:
  - property `def size(self):` to retrieve it
  - property setter `def size(self, value):` to set it:
    - size must be an integer, otherwise raise a TypeError exception with the message `size must be an integer`
    - if size is less than 0, raise a ValueError exception with the message `size must be >= 0`
- Instantiation with optional size: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character #:
  - if size is equal to 0, print an empty line
- You are not allowed to import any module

### 6. Coordinates of a square
**File:** `6-square.py`

Write a class Square that defines a square by: (based on 5-square.py)

- Private instance attribute: size:
  - property `def size(self):` to retrieve it
  - property setter `def size(self, value):` to set it:
    - size must be an integer, otherwise raise a TypeError exception with the message `size must be an integer`
    - if size is less than 0, raise a ValueError exception with the message `size must be >= 0`
- Private instance attribute: position:
  - property `def position(self):` to retrieve it
  - property setter `def position(self, value):` to set it:
    - position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional size and optional position: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character #:
  - if size is equal to 0, print an empty line
  - position should be use by using space - Don't fill lines by spaces when position[1] > 0
- You are not allowed to import any module

## How to Run

### Testing individual classes
```bash
./0-main.py
./1-main.py
./2-main.py
./4-main.py
./6-main.py
```

## Examples

### Task 0 - Empty class
```python
my_square = Square()
print(type(my_square))  # <class '0-square.Square'>
print(my_square.__dict__)  # {}
```

### Task 4 - Properties
```python
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))
# Area: 7921 for size: 89

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))
# Area: 9 for size: 3
```

### Task 6 - Position
```python
my_square = Square(3, (1, 1))
my_square.my_print()
# 
#  ###
#  ###
#  ###
```

## Repository Structure

```
alche-higher_level_programming/
└── python-classes/
    ├── README.md
    ├── 0-square.py
    ├── 1-square.py
    ├── 2-square.py
    ├── 3-square.py
    ├── 4-square.py
    ├── 5-square.py
    ├── 6-square.py
    └── [test files]
```

## Author

This project is part of the ALX Higher Level Programming curriculum.
