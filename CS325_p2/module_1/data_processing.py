"""
Data Processing Module

This module (data_processing.py) provides functionality to process article data from a given URL.

Input:
- url (str): URL of the article to be processed.

Output:
- headline (str): Extracted headline of the article.
- body (str): Extracted body content of the article.

Working:
- Utilizes the BeautifulSoup library to parse HTML content.
- Finds headline and body elements based on specified classes.
- Returns extracted headline and body content.

This module follows the Single Responsibility Principle (SOLID).

SOLID Principle:
- Single Responsibility Principle (SRP)

Benefit:
- Enhances maintainability by ensuring that each module has only one reason to change.

"""

import requests
from bs4 import BeautifulSoup

def process_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    headline_element = soup.find(class_="headline__text inline-placeholder")
    body_elements = soup.find_all(class_="paragraph inline-placeholder")

    headline = headline_element.text if headline_element else "No headline found"
    body = "\n".join(paragraph.text for paragraph in body_elements) if body_elements else "No body content found"

    return headline, body
