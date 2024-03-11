"""
run.py - Main script for processing articles from URLs or files.

Parameters:
    - URL: The URL of the article to be processed.
    - File: The name of the file containing article data.
    - argument: Specific argument based on the input type.

Folder Structure:
    Data/
    ├── processed/
    └── raw/

Dependencies:
    - module_1.data_processing
    - module_2.file_operations

Usage Example:
    python run.py

"""

from module_1.data_processing import process_article_from_file, get_raw_html_content
from module_2.file_operations import save_to_file, create_directory

def main():
    websites_file = "Data/raw/websites.txt"
    raw_output_directory = "Data/raw"
    processed_output_directory = "Data/processed"

    create_directory(raw_output_directory)
    create_directory(processed_output_directory)

    with open(websites_file, "r") as url_file:
        for i, url in enumerate(url_file, start=1):
            url = url.strip()  # Remove leading/trailing whitespaces and newlines
            raw_filename = f"raw_article{i}.html"
            raw_content = get_raw_html_content(url)
            save_to_file(raw_output_directory, raw_filename, raw_content)

            processed_filename = f"processed_article{i}.txt"
            file_path = f"{raw_output_directory}/{raw_filename}"
            headline, body = process_article_from_file(file_path)
            save_to_file(processed_output_directory, processed_filename, f"Headline: {headline}\n{body}")

if __name__ == "__main__":
    main()

