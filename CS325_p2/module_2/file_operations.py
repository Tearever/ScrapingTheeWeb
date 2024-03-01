"""
File Operations Module

This module (file_operations.py) provides functionality for file-related operations.

Input:
- output_directory (str): Directory where output files will be saved.
- filename (str): Name of the file to be created.
- content (str): Content to be written to the file.

Working:
- Provides functions to save content to a file and create directories.

This module follows the Single Responsibility Principle (SOLID).

SOLID Principle:
- Single Responsibility Principle (SRP)

Benefit:
- Enhances maintainability by ensuring that each module has only one reason to change.

"""

import os

def save_to_file(output_directory, filename, content):
    output_path = os.path.join(output_directory, filename)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
