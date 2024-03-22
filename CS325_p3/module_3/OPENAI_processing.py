"""
OPENAI_processing.py - Module for requesting summary from LLM such as OpenAI.

SOLID Principle:
    - Single Responsibility Principle (SRP)

Benefit:
    - Enhances maintainability by ensuring that each module has only one reason to change.

Usage:
    - openai_processing(file_path, filename, output_directory)

Input:
    - file_path (str): Path to the processed text file.
    - filename (str): Name of the file to be read from

Output:
    - openai_processing(): Extracted AI title for txt file and summary.

Dependencies:
    - openai
    - os

"""
from dotenv import load_dotenv
from openai import OpenAI
import os

def configure():
    load_dotenv()

def openai_processing(file_path, filename):
    #api_key = ""
    api_key = os.environ.get("OPENAI_API_KEY")

    client = OpenAI(api_key= api_key)

    with open(f"{file_path}/{filename}", "r", encoding="utf-8") as file:
                article_content = file.read()

                completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"summarize this article in 50 words\n\n{article_content}"}
                ]
                )

                unique = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"Generate a title with up to three words. this will be a name of a file so make sure to have a title that follows the rules of a filename. Make it catchy so it makes the user want to read it. No whitespaces and avoid special characters and punctuation. \n\n{article_content}"}
                ]
                )

                if completion.choices and completion.choices[0].message:
                    AI_headline = f"{unique.choices[0].message.content}.txt"
                    summary = completion.choices[0].message.content
                else:
                    print("No response received from OpenAI.")

                return AI_headline, summary