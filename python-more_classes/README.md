# Python - More Classes and Objects

This directory contains Python programming exercises focusing on advanced object-oriented programming concepts including class attributes, static methods, class methods, and special methods.

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
- What are the special __str__ and __repr__ methods and how to use them
- What is the difference between __str__ and __repr__
- What is a class attribute
- What is the difference between a object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain __dict__ of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the getattr function

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

### 0. Simple rectangle
**File:** `0-rectangle.py`

Write an empty class Rectangle that defines a rectangle.

- You are not allowed to import any module

### 1. Real definition of a rectangle
**File:** `1-rectangle.py`

Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

- Private instance attribute: width
- Private instance attribute: height
- Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
- Properties with validation for width and height

### 2. Area and Perimeter
**File:** `2-rectangle.py`

Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

- Add public instance method: `def area(self):` that returns the rectangle area
- Add public instance method: `def perimeter(self):` that returns the rectangle perimeter
- If width or height is equal to 0, perimeter is equal to 0

### 3. String representation
**File:** `3-rectangle.py`

Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

- `print()` and `str()` should print the rectangle with the character #
- If width or height is equal to 0, return an empty string

### 4. Eval is magic
**File:** `4-rectangle.py`

Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)

- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`

### 5. Detect instance deletion
**File:** `5-rectangle.py`

Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)

- Print the message `Bye rectangle...` when an instance of Rectangle is deleted

### 6. How many instances
**File:** `6-rectangle.py`

Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)

- Public class attribute `number_of_instances`:
  - Initialized to 0
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion

### 7. Change representation
**File:** `7-rectangle.py`

Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)

- Public class attribute `print_symbol`:
  - Initialized to #
  - Used as symbol for string representation
  - Can be any type

### 8. Compare rectangles
**File:** `8-rectangle.py`

Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)

- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
- Returns rect_1 if both have the same area value

### 9. A square is a rectangle
**File:** `9-rectangle.py`

Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)

- Class method `def square(cls, size=0):` that returns a new Rectangle instance with width == height == size

## How to Run

### Testing individual classes
```bash
./0-main.py
./1-main.py
./4-main.py
./9-main.py
```

## Examples

### Task 0 - Empty class
```python
my_rectangle = Rectangle()
print(type(my_rectangle))  # <class '0-rectangle.Rectangle'>
print(my_rectangle.__dict__)  # {}
```

### Task 4 - Eval magic
```python
my_rectangle = Rectangle(2, 4)
print(repr(my_rectangle))  # Rectangle(2, 4)
new_rectangle = eval(repr(my_rectangle))
print(new_rectangle is my_rectangle)  # False
print(type(new_rectangle) is type(my_rectangle))  # True
```

### Task 9 - Square method
```python
my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
# Area: 25 - Perimeter: 20
```

## Repository Structure

```
alche-higher_level_programming/
└── python-more_classes/
    ├── README.md
    ├── 0-rectangle.py
    ├── 1-rectangle.py
    ├── 2-rectangle.py
    ├── 3-rectangle.py
    ├── 4-rectangle.py
    ├── 5-rectangle.py
    ├── 6-rectangle.py
    ├── 7-rectangle.py
    ├── 8-rectangle.py
    ├── 9-rectangle.py
    └── [test files]
```

## Author

This project is part of the ALX Higher Level Programming curriculum.
