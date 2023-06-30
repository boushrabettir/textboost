# TODO
import subprocess
from PyPDF2 import PdfReader
import os
import aspose.words as aw
import markdownify
import fitz


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


def pdf_to_html(path: str, modified_path: str) -> None:
    """Converts PDF to HTML file"""

    temp_txt_path = os.path.join(modified_path, "temp.txt")

    extracted_text = pdf_to_text_extraction(path)
    print(extracted_text)
    with open(temp_txt_path, "w") as file:
        file.write(extracted_text)


def html_to_md(modified_path: str) -> str:
    """Converts HTML to Markdown file"""

    temp_txt_path = os.path.join(modified_path, "temp.txt")
    temp_md_path = os.path.join(modified_path, "temp.md")

    try:
        with open(temp_txt_path, "rb") as file:
            # html = pdf_to_text_extraction(file.name)
            md = markdownify.markdownify(file)
        with open(temp_md_path, "w") as file:
            file.write(md)
            # os.remove(temp_txt_path)
    except OSError as e:
        print(f"Issue opening path to file: {e}")


def md_to_pdf_t2(path: str, name: str) -> None:
    """Converts Markdown to PDF file"""

    try:
        subprocess.run(
            [
                "pandoc",
                f"{path}/temp.md",
                "-o",
                f"{path}/{name}.pdf",
            ]
        )
    # os.remove(temp_txt_path)  # Remove TXT file once PDF file has been created
    except Exception as e:
        print(f"{e}")


# from markdown2pdf import convert_md_2_pdf

from weasyprint import HTML


def md_to_pdf(path: str, name: str) -> None:
    """Converts markdown file to PDF file"""

    try:
        with open(f"{path}/temp.md", "r") as file:
            text = file.read()
        html = f"<html><body>{text}</body></html>"
        HTML(string=html).write_pdf(f"{path}/{name}.pdf")
    except FileNotFoundError:
        print("oh")
    # try:
    #     subprocess.run(f"md2pdf {path}/temp.md")
    # except subprocess.CalledProcessError:
    #     print("Issue calling subprocess 'mdpdf' command.")
    # except FileNotFoundError:
    #     print(f"File '{name}.md' not found.")

    # os.remove(f"modified/{folder}/{name}.md")


# def md_to_pdf(input_file: str, output_file: str) -> None:
#     """Converts Markdown file to PDF"""
#     try:
#         convert(input_file, output_file)
#         print(f"PDF successfully created: {output_file}")
#     except FileNotFoundError:
#         print(f"Input file '{input_file}' not found.")
