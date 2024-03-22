"""
data_processing.py - Module for processing article data.

SOLID Principle:
    - Single Responsibility Principle (SRP)

Benefit:
    - Enhances maintainability by ensuring that each module has only one reason to change.

Usage:
    - process_article_from_file(file_path)
    - get_raw_html_content(url)

Input:
    - file_path (str): Path to the raw HTML file.
    - url (str): URL of the article to be processed.

Output:
    - process_article_from_file(): Extracted headline and body content.
    - get_raw_html_content(): Raw HTML content containing the <!DOCTYPE html> declaration.

Dependencies:
    - requests
    - bs4

"""

import requests
from bs4 import BeautifulSoup

def process_article_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    headline_element = soup.find(class_="headline__text inline-placeholder")
    body_elements = soup.find_all(class_="paragraph inline-placeholder")

    headline = headline_element.text if headline_element else "No headline found"
    body = "\n".join(paragraph.text for paragraph in body_elements) if body_elements else "No body content found"

    return headline, body

def get_raw_html_content(url):
    response = requests.get(url)
    doctype_start_index = response.text.find('<!DOCTYPE html>')
    if doctype_start_index != -1:
        return response.text[doctype_start_index:]
    return response.text
