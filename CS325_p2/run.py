"""
Imports and uses DataProcessing and FileOperations classes to achieve the desired functionality.

"""

from module_1.data_processing import process_article
from module_2.file_operations import save_to_file, create_directory

def main():
    websites_file = "Data/raw/websites.txt"
    output_directory = "Data/processed"

    create_directory(output_directory)

    with open(websites_file, "r") as url_file:
        for i, url in enumerate(url_file, start=1):
            url = url.strip()  # Remove leading/trailing whitespaces and newlines
            headline, body = process_article(url)

            filename = f"article{i}.txt"
            save_to_file(output_directory, filename, f"Headline: {headline}\n{body}")


if __name__ == "__main__":
    main()
