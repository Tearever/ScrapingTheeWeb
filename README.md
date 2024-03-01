# Project 2

Breaks Down Project 1 code into logically two different files/modules.

## Table of Contents

1. [Introduction](#introduction)
2. [Folder Structure](#folder-structure)
3. [Modules](#modules)
4. [SOLID Principle](#solid-principle)
5. [Class Diagram](#class-diagram)

## Introduction

Welcome to Project 2! This project breaks down project-1 code into logically two different files/modules.

## Folder Structure

This project is organized with the following folder structure:
<img src="images/Screenshot%202024-03-01%20142824.png" alt="image of folder structure"/>


## Modules

### `module_1/data_processing.py`

The `data_processing` module is responsible for processing article data from a given URL.

- **Functions/Classes:**
  - `process_article(url: str) -> Tuple[str, str]`: Processes the article and returns the headline and body.

...

### `module_2/file_operations.py`

The `file_operations` module handles file-related operations.

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

 ...

## Class Diagram





