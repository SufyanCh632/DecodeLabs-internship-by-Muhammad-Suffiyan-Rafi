# Random Password Generator

## Project Overview

This project is a **Random Password Generator** built using Python.
It generates strong and secure passwords based on the length provided by the user.

The project demonstrates:

* Importing Python modules
* String manipulation
* Randomized password generation
* User input handling
* Exception handling

---

## Features

* Generate secure random passwords
* Supports:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* User-defined password length
* Error handling for invalid inputs

---

## Technologies Used

* Python 3
* `random` module
* `string` module

---

## Project Structure

```text
random_password_generator/
│
├── password_generator.py
└── README.md
```

---

## How It Works

1. The user enters the desired password length.
2. The program combines:

   * Alphabets
   * Digits
   * Symbols
3. A random password is generated and displayed.

---

## Python Code

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Please enter a positive number.")
    else:
        password = generate_password(length)
        print("\nGenerated Password:", password)

except ValueError:
    print("Invalid input! Please enter a number.")
```

---

## Example Output

```text
Enter password length: 10

Generated Password: x@9L#2pQ!7
```

---

## Concepts Used

* Functions
* Loops
* String manipulation
* Random module
* Exception handling
* User input

---

## Future Improvements

* Add password strength checker
* Save generated passwords to a file
* Create GUI version using Tkinter
* Generate multiple passwords at once

---

## Learning Outcome

By completing this project, you will learn how to:

* Use Python built-in libraries
* Generate secure random data
* Build beginner-level security tools
* Handle user input effectively

---

## Author

Muhammad Suffiyan Rafi
Python Developer | Industrial Training Project 2026

