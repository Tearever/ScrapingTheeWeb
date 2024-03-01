# Project-2: Data Processing and File Operations

## Table of Contents

1. [Project-2: Data Processing and File Operations](#project-2-data-processing-and-file-operations)
    1.1 [Description](#description)
    1.2 [Folder Structure](#folder-structure)
    1.3 [Modules](#modules)
        1.3.1 [module_1/data_processing.py](#module_1data_processingpy)
        1.3.2 [module_2/file_operations.py](#module_2file_operationspy)
    1.4 [SOLID Principle](#solid-principle)
    1.5 [Class Diagram](#class-diagram)
    1.6 [Usage](#usage)
    1.7 [Contributing](#contributing)
    1.8 [License](#license)
    1.9 [Contact Information](#contact-information)


## Description

Project-2 aims to refactor and enhance the functionality of Project-1 by breaking down the code into two logical modules, implementing a folder structure, and incorporating SOLID principles. The project involves the following tasks:

1. **Code Refactoring:**
   - Break down Project-1 code into two logically different modules.
   - Use `import` to call the functionality of one file into another.

2. **Folder Structure:**
   - Utilize the given folder structure.
   - Create a `Data/raw` folder to store unprocessed/raw data files.
   - Create a `Data/processed` folder to store processed articles.

3. **Main Program:**
   - Implement a `run.py` file containing the main function.
   - Call the rest of the modules from the main program.

4. **Documentation:**
   - Document code with comments in each Python file explaining input, output, and functionality.
   - Use comments to describe the working of the code.

5. **SOLID Principles:**
   - Implement one of the SOLID principles (Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, Dependency Inversion Principle).
   - Mention the SOLID principle used and its benefits at the top of the relevant Python file.

6. **Class Diagram:**
   - Create a UML class diagram of the entire software.
   - Save the class diagram as a JPEG/PNG and upload it to GitHub.

## Folder Structure

The project adheres to the following folder structure:


<img src="images/Screenshot%202024-03-01%20142824.png" alt="image of folder structure"/>



## Modules

### `module_1/data_processing.py`

This module processes raw article data from a given URL.

- **Functions/Classes:**
  - `process_article(url: str) -> Tuple[str, str]`: Processes the article and returns the headline and body.

...

### `module_2/file_operations.py`

This module handles file-related operations.

- **Functions/Classes:**
  - `save_to_file(output_directory: str, filename: str, content: str) -> None`: Saves content to a file.
  - `create_directory(directory: str) -> None`: Creates a directory if it doesn't exist.

...

## SOLID Principle

This project adheres to the Single Responsibility Principle (SOLID).

- **SOLID Principle:**
  - Single Responsibility Principle (SRP)

- **Benefits:**
  - Enhances maintainability by ensuring that each module has only one reason to change.

## Class Diagram

View the UML class diagram for this project [here](link_to_your_class_diagram_image).

## Usage

To use this project, follow these steps:

1. Clone the repository.
2. Navigate to the project root.
3. Run the main program: `python3 run.py URL/File/argument`

...





