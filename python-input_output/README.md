# Python - Input/Output

This directory contains Python programming exercises focusing on file input/output operations, JSON serialization/deserialization, and working with files and data structures.

## Learning Objectives

At the end of this project, you should be able to explain:
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

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

## Tasks

### 0. Read file
**File:** `0-read_file.py`

Write a function that reads a text file (UTF8) and prints it to stdout.

**Prototype:** `def read_file(filename=""):`
- You must use the with statement
- You don't need to manage file permission or file doesn't exist exceptions
- You are not allowed to import any module

### 1. Write to a file
**File:** `1-write_file.py`

Write a function that writes a string to a text file (UTF8) and returns the number of characters written.

**Prototype:** `def write_file(filename="", text=""):`
- You must use the with statement
- You don't need to manage file permission exceptions
- Your function should create the file if doesn't exist
- Your function should overwrite the content of the file if it already exists
- You are not allowed to import any module

### 2. Append to a file
**File:** `2-append_write.py`

Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

**Prototype:** `def append_write(filename="", text=""):`
- If the file doesn't exist, it should be created
- You must use the with statement
- You don't need to manage file permission or file doesn't exist exceptions
- You are not allowed to import any module

### 3. To JSON string
**File:** `3-to_json_string.py`

Write a function that returns the JSON representation of an object (string).

**Prototype:** `def to_json_string(my_obj):`
- You don't need to manage exceptions if the object can't be serialized

### 4. From JSON string to Object
**File:** `4-from_json_string.py`

Write a function that returns an object (Python data structure) represented by a JSON string.

**Prototype:** `def from_json_string(my_str):`
- You don't need to manage exceptions if the JSON string doesn't represent an object

### 5. Save Object to a file
**File:** `5-save_to_json_file.py`

Write a function that writes an Object to a text file, using a JSON representation.

**Prototype:** `def save_to_json_file(my_obj, filename):`
- You must use the with statement
- You don't need to manage exceptions if the object can't be serialized
- You don't need to manage file permission exceptions

### 6. Create object from a JSON file
**File:** `6-load_from_json_file.py`

Write a function that creates an Object from a "JSON file".

**Prototype:** `def load_from_json_file(filename):`
- You must use the with statement
- You don't need to manage exceptions if the JSON string doesn't represent an object
- You don't need to manage file permissions / exceptions

### 7. Load, add, save
**File:** `7-add_item.py`

Write a script that adds all arguments to a Python list, and then save them to a file.

**Requirements:**
- You must use your function save_to_json_file from 5-save_to_json_file.py
- You must use your function load_from_json_file from 6-load_from_json_file.py
- The list must be saved as a JSON representation in a file named add_item.json
- If the file doesn't exist, it should be created
- You don't need to manage file permissions / exceptions

### 8. Class to JSON
**File:** `8-class_to_json.py`

Write a function that returns the dictionary description with simple data structure for JSON serialization of an object.

**Prototype:** `def class_to_json(obj):`
- obj is an instance of a Class
- All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
- You are not allowed to import any module

### 9. Student to JSON
**File:** `9-student.py`

Write a class Student that defines a student by:

**Requirements:**
- Public instance attributes: first_name, last_name, age
- Instantiation with first_name, last_name and age: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a Student instance
- You are not allowed to import any module

### 10. Student to JSON with filter
**File:** `10-student.py`

Write a class Student that defines a student by: (based on 9-student.py)

**Requirements:**
- Public instance attributes: first_name, last_name, age
- Instantiation with first_name, last_name and age: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance
- If attrs is a list of strings, only attribute names contained in this list must be retrieved
- Otherwise, all attributes must be retrieved
- You are not allowed to import any module

### 11. Student to disk and reload
**File:** `11-student.py`

Write a class Student that defines a student by: (based on 10-student.py)

**Requirements:**
- Public instance attributes: first_name, last_name, age
- Instantiation with first_name, last_name and age: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance
- Public method `def reload_from_json(self, json):` that replaces all attributes of the Student instance
- You can assume json will always be a dictionary
- A dictionary key will be the public attribute name
- A dictionary value will be the value of the public attribute
- You are not allowed to import any module

### 12. Pascal's Triangle
**File:** `12-pascal_triangle.py`

Create a function that returns a list of lists of integers representing the Pascal's triangle of n.

**Prototype:** `def pascal_triangle(n):`
- Returns an empty list if n <= 0
- You can assume n will be always an integer
- You are not allowed to import any module

## Key Concepts

### File Operations
- **Reading files**: Use `with open(filename, 'r')` for safe file handling
- **Writing files**: Use `with open(filename, 'w')` to create/overwrite
- **Appending files**: Use `with open(filename, 'a')` to add content

### JSON Operations
- **Serialization**: Convert Python objects to JSON strings using `json.dumps()`
- **Deserialization**: Convert JSON strings to Python objects using `json.loads()`
- **File operations**: Use `json.dump()` and `json.load()` for direct file operations

### Class Serialization
- Use `obj.__dict__` to get all instance attributes as a dictionary
- Filter attributes using list comprehension or conditional logic
- Reload attributes using `setattr()` function

## Examples

### Task 1 - Write file
```python
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)  # 24
```

### Task 7 - Add item script
```bash
./7-add_item.py Best School
./7-add_item.py 89 Python C
# Results in: ["Best", "School", "89", "Python", "C"]
```

### Task 12 - Pascal's Triangle
```python
print_triangle(pascal_triangle(5))
# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
# [1,4,6,4,1]
```

## Repository Structure

```
alche-higher_level_programming/
└── python-input_output/
    ├── README.md
    ├── 0-read_file.py
    ├── 1-write_file.py
    ├── 2-append_write.py
    ├── 3-to_json_string.py
    ├── 4-from_json_string.py
    ├── 5-save_to_json_file.py
    ├── 6-load_from_json_file.py
    ├── 7-add_item.py
    ├── 8-class_to_json.py
    ├── 9-student.py
    ├── 10-student.py
    ├── 11-student.py
    ├── 12-pascal_triangle.py
    └── [test files]
```

## Author

This project is part of the ALX Higher Level Programming curriculum.
