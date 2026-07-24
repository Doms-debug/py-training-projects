# Password Generator

CLI tool for generating secure, customizable passwords. By default, the generator uses only uppercase and lowercase letters. Numbers and special characters can be added dynamically via optional flags.

## Features

* Generates passwords of any specified length
* Includes uppercase and lowercase letters by default
* Expands the character pool with numbers using the `--use-numbers` flag
* Expands the character pool with special characters using the `--use-symbols` flag

## Setup and Installation

* Navigate to the project directory
* No external dependencies or virtual environments are required as the script uses only built-in Python modules

### Usage

Execute the script via terminal by providing the desired password length as a positional argument:

```bash
# Generate an 8-character password with letters only
python generator.py 8

# Generate a 12-character password with letters and numbers
python generator.py 12 --use-numbers

# Generate a 16-character password with letters, numbers, and symbols
python generator.py 16 --use-numbers --use-symbol
```