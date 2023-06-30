import subprocess
from PyPDF2 import PdfReader
import os

import fitz
import markdownify


def pdf_to_text_extraction(file: str) -> str:
    """Extracts text from the given PDF file by the user"""

    doc = fitz.open(file)
    text = ""

    for page in doc:
        text += page.get_text()

    return text


def modify_extracted_text(text: str, path: str) -> None:
    """Creates bionic reading string and modifies original file before file conversion"""

    formatted_list = []
    words = text.split()
    for word in words:
        formatted_list.append(f"**{word[:2]}**{word[2:]}")

    final_string = " ".join(formatted_list)

    try:
        with open(path, "w") as file:
            file.write(final_string)
    except OSError as os:
        print(os)


def pdf_to_html(path: str) -> None:
    """Converts PDF to HTML file"""

    extracted_text = pdf_to_text_extraction(path)
    modify_extracted_text(extracted_text, path)

    try:
        subprocess.run(["pdf2htmlEX", "--zoom", "1.3", path])
    except subprocess.CalledProcessError:
        print("Issue calling subprocess 'pdf2htmlEX' command.")
    except Exception as e:
        print(f"File path does not exist: {e}")


def html_to_md(path: str) -> str:
    """Converts HTML to Markdown file"""

    temp_txt_path = "./pre-modified/temp.txt"
    if not os.path.exists(temp_txt_path):
        os.makedirs(temp_txt_path)

    try:
        with open(path, "rb") as file:
            html = pdf_to_text_extraction(path)
            md = markdownify.markdownify(html, heading_style="ATX")

        with open(temp_txt_path, "w") as file:
            file.write(md)
    except OSError as e:
        print(f"Issue opening path to file: {e}")


def md_to_pdf(path: str, name: str) -> None:
    """Converts Markdown to PDF file"""

    temp_txt_path = "./pre-modified/temp.txt"
    try:
        subprocess.run(
            ["pandoc", temp_txt_path, "--pdf-engine=xelatex", "-o", f"{path}/{name}"]
        )
        os.remove(temp_txt_path)  # Remove TXT file once PDF file has been created
    except Exception as e:
        print(f"{e}")


def md_to_pdf(name: str, folder: str) -> None:
    """Converts markdown file to PDF file"""

    try:
        subprocess.run(
            [
                "mdpdf",
                "-o",
                f"modified/{folder}/{name}.pdf",
                f"modified/{folder}/{name}.md",
            ]
        )
    except subprocess.CalledProcessError:
        print("Issue calling subprocess 'mdpdf' command.")
    except FileNotFoundError:
        print(f"File '{name}.md' not found.")

    os.remove(f"modified/{folder}/{name}.md")
