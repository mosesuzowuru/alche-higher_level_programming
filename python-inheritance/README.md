# Python - Inheritance

This directory contains Python programming exercises focusing on inheritance, one of the fundamental concepts of object-oriented programming.

## Learning Objectives

At the end of this project, you should be able to explain:
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use pycodestyle (version 2.8.*)
- All files must be executable
- The length of your files will be tested using wc

### Python Test Cases
- All test files should be inside a folder tests
- All test files should be text files (extension: .txt)
- All tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All modules should have documentation
- All classes should have documentation
- All functions should have documentation

## Tasks

### 0. Lookup
**File:** `0-lookup.py`

Write a function that returns the list of available attributes and methods of an object.

**Prototype:** `def lookup(obj):`
- Returns a list object
- You are not allowed to import any module

### 1. My list
**Files:** `1-my_list.py`, `tests/1-my_list.txt`

Write a class MyList that inherits from list.

**Requirements:**
- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type int
- You are not allowed to import any module

### 2. Exact same object
**File:** `2-is_same_class.py`

Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.

**Prototype:** `def is_same_class(obj, a_class):`
- You are not allowed to import any module

### 3. Same class or inherit from
**File:** `3-is_kind_of_class.py`

Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.

**Prototype:** `def is_kind_of_class(obj, a_class):`
- You are not allowed to import any module

### 4. Only sub class of
**File:** `4-inherits_from.py`

Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.

**Prototype:** `def inherits_from(obj, a_class):`
- You are not allowed to import any module

### 5. Geometry module
**File:** `5-base_geometry.py`

Write an empty class BaseGeometry.

- You are not allowed to import any module

### 6. Improve Geometry
**File:** `6-base_geometry.py`

Write a class BaseGeometry (based on 5-base_geometry.py).

**Requirements:**
- Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
- You are not allowed to import any module

### 7. Integer validator
**Files:** `7-base_geometry.py`, `tests/7-base_geometry.txt`

Write a class BaseGeometry (based on 6-base_geometry.py).

**Requirements:**
- Public instance method: `def area(self):` that raises an Exception with the message `area() is not implemented`
- Public instance method: `def integer_validator(self, name, value):` that validates value
- You can assume name is always a string
- If value is not an integer: raise a TypeError exception, with the message `<name> must be an integer`
- If value is less or equal to 0: raise a ValueError exception with the message `<name> must be greater than 0`
- You are not allowed to import any module

### 8. Rectangle
**File:** `8-rectangle.py`

Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

**Requirements:**
- Instantiation with width and height: `def __init__(self, width, height):`
- width and height must be private. No getter or setter
- width and height must be positive integers, validated by integer_validator

### 9. Full rectangle
**File:** `9-rectangle.py`

Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

**Requirements:**
- Instantiation with width and height: `def __init__(self, width, height):`
- width and height must be private. No getter or setter
- width and height must be positive integers validated by integer_validator
- the area() method must be implemented
- print() should print, and str() should return, the following rectangle description: `[Rectangle] <width>/<height>`

### 10. Square #1
**File:** `10-square.py`

Write a class Square that inherits from Rectangle (9-rectangle.py).

**Requirements:**
- Instantiation with size: `def __init__(self, size):`
- size must be private. No getter or setter
- size must be a positive integer, validated by integer_validator
- the area() method must be implemented

### 11. Square #2
**File:** `11-square.py`

Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

**Requirements:**
- Instantiation with size: `def __init__(self, size):`
- size must be private. No getter or setter
- size must be a positive integer, validated by integer_validator
- the area() method must be implemented
- print() should print, and str() should return, the square description: `[Square] <width>/<height>`

## Key Concepts

### Inheritance Hierarchy
```
BaseGeometry
    └── Rectangle
            └── Square
```

### Class vs Instance vs Inheritance Checks
- `type(obj) is class` - Exact class match
- `isinstance(obj, class)` - Instance of class or inherited from it
- `isinstance(obj, class) and type(obj) is not class` - Inherited but not exact match

### Method Resolution Order (MRO)
Python uses Method Resolution Order to determine which method to call in inheritance hierarchies.

## Examples

### Task 1 - MyList inheritance
```python
my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
print(my_list)        # [1, 4, 2]
my_list.print_sorted() # [1, 2, 4]
print(my_list)        # [1, 4, 2] - original unchanged
```

### Task 9 - Rectangle implementation
```python
r = Rectangle(3, 5)
print(r)         # [Rectangle] 3/5
print(r.area())  # 15
```

### Task 11 - Square implementation
```python
s = Square(13)
print(s)         # [Square] 13/13
print(s.area())  # 169
```

## Repository Structure

```
alche-higher_level_programming/
└── python-inheritance/
    ├── README.md
    ├── 0-lookup.py
    ├── 1-my_list.py
    ├── 2-is_same_class.py
    ├── 3-is_kind_of_class.py
    ├── 4-inherits_from.py
    ├── 5-base_geometry.py
    ├── 6-base_geometry.py
    ├── 7-base_geometry.py
    ├── 8-rectangle.py
    ├── 9-rectangle.py
    ├── 10-square.py
    ├── 11-square.py
    ├── tests/
    │   ├── 1-my_list.txt
    │   └── 7-base_geometry.txt
    └── [test files]
```

## Author

This project is part of the ALX Higher Level Programming curriculum.
