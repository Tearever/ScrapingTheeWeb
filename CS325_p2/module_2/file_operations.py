"""
file_operations.py - Module for file-related operations.

SOLID Principle:
    - Single Responsibility Principle (SRP)

Benefit:
    - Enhances maintainability by ensuring that each module has only one reason to change.

Usage:
    - save_to_file(output_directory, filename, content)
    - create_directory(directory)

Input:
    - output_directory (str): Directory where output files will be saved.
    - filename (str): Name of the file to be created.
    - content (str): Content to be written to the file.

Output:
    - save_to_file(): Save content to a file.
    - create_directory(): Create a directory if it does not exist.

Dependencies:
    - os

"""

import os

def save_to_file(output_directory, filename, content):
    output_path = os.path.join(output_directory, filename)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
