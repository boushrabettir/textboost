# TODO

import os
import markdownify
import fitz
import PyPDF2
import mistune
import markdownify
import pdfdocument


def pdf_to_text_extraction(file: str) -> str:
    """Extracts text from the given PDF file by the user"""
    doc = fitz.open(file)
    text = ""

    for page in doc:
        text += page.get_text()

    return text


def modify_extracted_text(file: str) -> None:
    """Creates bionic reading string and modifies original file before file conversion"""

    text = pdf_to_text_extraction(file)
    formatted_list = []
    words = text.split()
    for word in words:
        formatted_list.append(f"**{word[:2]}**{word[2:]}")

    final_string = " ".join(formatted_list)

    return final_string


def create_pdf(modified_path: str, name: str, modified_text: str) -> None:
    """Creates PDF from modified extracted string"""

    path = os.path.join(modified_path, f"{name}.pdf")
    with open(path, "w") as file:
        file.write(modified_text)


def pdf_to_text(path: str) -> str:
    """"""

    text = ""
    with open(path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()

    modified_text = ""

    line = ""
    for word in text.split():
        modified_words = []  # Initialize the list for each word
        for x in word.split():
            if x[0] == "-":
                modified_words.append("\n -")
            else:
                modified_words.append(f"**{x[:2]}**{x[2:]}")

        line = " ".join(modified_words)  # Assign the modified words to the line
        modified_text += line + "\n"

    return modified_text


def html_content(modified_path: str, path: str) -> None:
    """"""
    temp_html = os.path.join(modified_path, "temp.html")
    modified_text = pdf_to_text(path)
    html_content = mistune.markdown(modified_text)

    with open(temp_html, "w") as file:
        file.write(html_content)

    with open(temp_html, "r") as file:
        html_content = file.read()

    markdown_content = markdownify.markdownify(html_content)

    temp_md = os.path.join(modified_path, "temp.md")
    with open(temp_md, "w") as file:
        file.write(markdown_content)


def create_pdf_content(modified_path: str, name: str) -> None:
    """"""

    temp_md = os.path.join(modified_path, "temp.md")

    with open(temp_md, "r") as file:
        content = file.read()

    pdf = pdfdocument.PDF()

    pdf.markdown(content)

    pdf.save(f"{modified_path}/{name}.pdf")


# def pdf_to_md_tesintg(path: str) -> None:
#     """Pdf to md"""

#     temp_md_path = os.path.join("./pre-modified/temp.md")
#     try:
#         with open(path, "rb") as file:
#             md = markdownify.markdownify(file)

#         with open(temp_md_path, "w") as file:
#             file.write(md)

#     except IsADirectoryError as dir:
#         print(dir)

#     with open(path, "r") as file:
#         content = file.read()

#     md_content = markdown2.markdown(content)

#     pdfkit.from_string(md_content, "output.pdf")


# def pdf_to_html(path: str, modified_path: str) -> None:
#     """Converts PDF to HTML file"""

#     temp_txt_path = os.path.join(modified_path, "temp.txt")

#     extracted_text = pdf_to_text_extraction(path)
#     print(extracted_text)
#     with open(temp_txt_path, "w") as file:
#         file.write(extracted_text)


# def html_to_md(modified_path: str) -> str:
#     """Converts HTML to Markdown file"""

#     temp_txt_path = os.path.join(modified_path, "temp.txt")
#     temp_md_path = os.path.join(modified_path, "temp.md")

#     try:
#         with open(temp_txt_path, "rb") as file:
#             # html = pdf_to_text_extraction(file.name)
#             md = markdownify.markdownify(file)
#         with open(temp_md_path, "w") as file:
#             file.write(md)
#             # os.remove(temp_txt_path)
#     except OSError as e:
#         print(f"Issue opening path to file: {e}")


# def md_to_pdf_t2(path: str, name: str) -> None:
#     """Converts Markdown to PDF file"""

#     try:
#         subprocess.run(
#             [
#                 "pandoc",
#                 f"{path}/temp.md",
#                 "-o",
#                 f"{path}/{name}.pdf",
#             ]
#         )
#     # os.remove(temp_txt_path)  # Remove TXT file once PDF file has been created
#     except Exception as e:
#         print(f"{e}")


# from markdown2pdf import convert_md_2_pdf


# def md_to_pdf(path: str, name: str) -> None:
#     """Converts markdown file to PDF file"""

#     try:
#         with open(f"{path}/temp.md", "r") as file:
#             text = file.read()
#         html = f"<html><body>{text}</body></html>"
#         HTML(string=html).write_pdf(f"{path}/{name}.pdf")
#     except FileNotFoundError:
#         print("Not found")


# def md_to_pdf(input_file: str, output_file: str) -> None:
#     """Converts Markdown file to PDF"""
#     try:
#         convert(input_file, output_file)
#         print(f"PDF successfully created: {output_file}")
#     except FileNotFoundError:
#         print(f"Input file '{input_file}' not found.")
