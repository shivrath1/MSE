# Review of the Student Login Decorator Project

## Overview

The project demonstrates the use of Python decorators in a simple student management system. The program contains functions for:

- Student login
- Assignment submission
- Viewing grades

A custom decorator named `log_activity` is used to automatically track and display activity information whenever a function is executed.

---

# Decorators

A decorator in Python is a function that adds extra functionality to another function without changing the original function code.

In this project, the decorator is used to:
- Display the function name
- Show the current date and time
- Print activity start and completion messages

This reduces duplicate code because the logging functionality is written once and reused for multiple functions.

---

# Understanding of the Project Structure

The project is divided into three files:

## 1. `main.py`

- Controls the execution flow of the program
- Calls all user-related functions

## 2. `users.py`

Contains the main student operations:
- Student login
- Assignment submission
- Viewing grades

## 3. `decorators.py`

- Contains the reusable `log_activity` decorator
- Handles logging functionality for all decorated functions

This project helped in understanding Decorators, Wrapper functions, `*args` and `**kwargs`, Code reusability and Modular programming

---

# Runtime and Syntax Errors

## Syntax Errors

No syntax errors were found in the project.

---

## Runtime Errors

The program runs successfully without runtime errors.

However, there is one logical inconsistency in `main.py`:

```python
view_grades("Alex")
```

Earlier functions use the username `"Mohammad"`, but the grades are viewed using `"Alex"`.

This is not a runtime error, but it may create confusion in the output. 
