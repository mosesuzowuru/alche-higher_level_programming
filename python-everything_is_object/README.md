# Python - Everything is object

This directory contains exercises about Python's object model, exploring concepts like mutability, immutability, identity, equality, and how Python handles different types of objects.

## Learning Objectives

At the end of this project, you should be able to explain:
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use pycodestyle (version 2.7.*)
- All files must be executable
- The length of your files will be tested using wc

### .txt Answer Files
- Only one line
- No Shebang
- All files should end with a new line

## Tasks

### 0. Who am I?
**File:** `0-answer.txt`

What function would you use to print the type of an object?
Write the name of the function in the file, without ().

### 1. Where are you?
**File:** `1-answer.txt`

How do you get the variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without ().

### 2-5. Right count questions
**Files:** `2-answer.txt`, `3-answer.txt`, `4-answer.txt`, `5-answer.txt`

These tasks test understanding of when variables point to the same object, considering Python's integer caching and object creation.

### 6-9. String equality and identity
**Files:** `6-answer.txt`, `7-answer.txt`, `8-answer.txt`, `9-answer.txt`

These tasks explore the difference between `==` (equality) and `is` (identity) with strings, including string interning.

### 10-13. List equality and identity
**Files:** `10-answer.txt`, `11-answer.txt`, `12-answer.txt`, `13-answer.txt`

These tasks explore how lists behave with equality and identity operations.

### 14-18. Mutability and function calls
**Files:** `14-answer.txt`, `15-answer.txt`, `16-answer.txt`, `17-answer.txt`, `18-answer.txt`

These tasks demonstrate the difference between mutable and immutable objects, and how they behave when passed to functions or modified.

### 19. Copy a list object
**File:** `19-copy_list.py`

Write a function `def copy_list(l):` that returns a copy of a list.
- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module

### 20-26. Tuple identification
**Files:** `20-answer.txt`, `21-answer.txt`, `22-answer.txt`, `23-answer.txt`, `24-answer.txt`, `25-answer.txt`, `26-answer.txt`

These tasks test understanding of tuple syntax and when tuples are the same object vs different objects.

### 27-28. List operations and identity
**Files:** `27-answer.txt`, `28-answer.txt`

These tasks explore the difference between `+` (creates new object) and `+=` (in-place modification) operations on lists.

## Key Concepts

### Mutable vs Immutable Objects

**Mutable objects** (can be changed after creation):
- list
- dict
- set
- bytearray

**Immutable objects** (cannot be changed after creation):
- int, float, complex
- str
- tuple
- frozenset
- bytes

### Identity vs Equality

- `==` checks if two objects have the same value (equality)
- `is` checks if two variables refer to the same object (identity)
- `id()` returns the unique identifier of an object (memory address in CPython)

### Python Integer Caching

Python caches small integers (typically -5 to 256) for performance. This means:
```python
a = 100
b = 100
print(a is b)  # True - same cached object

a = 1000
b = 1000
print(a is b)  # False - different objects (may vary)
```

### String Interning

Python automatically interns some strings (like identifiers and small strings):
```python
a = "hello"
b = "hello"
print(a is b)  # True - same interned string object
```

### Function Arguments

Python passes arguments by assignment:
- For immutable objects: function receives a copy of the reference, cannot modify original
- For mutable objects: function receives the same reference, can modify original

## Examples

### Task 19 - Copy a list
```python
def copy_list(l):
    return l[:]

my_list = [1, 2, 3]
new_list = copy_list(my_list)
print(new_list == my_list)  # True (same content)
print(new_list is my_list)  # False (different objects)
```

### Understanding mutability
```python
# Mutable objects
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)  # [1, 2, 3, 4] - modified because same object

# Immutable objects
a = 10
b = a
a += 1
print(b)  # 10 - unchanged because integers are immutable
```

## Repository Structure

```
alche-higher_level_programming/
└── python-everything_is_object/
    ├── README.md
    ├── 0-answer.txt through 28-answer.txt
    ├── 19-copy_list.py
    └── [test files]
```

## Author

This project is part of the ALX Higher Level Programming curriculum.
