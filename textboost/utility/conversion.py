import os
import markdownify
import fitz
import PyPDF2
import mistune
import markdownify
import pdfdocument
import markdown_it
import string
import subprocess
import html2text


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


# TODO - Fix open/close
def convert_pdf_to_md(input_pdf_path, output_md_path) -> None:
    """Converts a PDF file to a Markdown file"""

    doc = fitz.open(input_pdf_path)

    with open(output_md_path, "w", encoding="utf-8") as md_file:
        for page in doc:
            modified = ""
            text = page.get_text().strip()
            splitted_text = text.split()
            # TODO - Look below
            # for t in splitted_text:
            #     modified += f"**{t[:2]}**{t[2:]}"

            # for s in splitted_text:
            #     # print(s)
            #     if s == "-":
            #         modified += f"\n{s} "
            #     else:
            #         modified += f"{s} "
            # if s.strip() == "-":
            #     modified += f"\n{s} "
            # else:
            #     modified += f"{s} "

            md_file.write(text)

    doc.close()


#  TODO - Fix bolding per word issue
def bionify_markdown_file(file_path) -> str:
    """Creates bionic reading effect"""

    final_string = ""
    temp = []
    with open(file_path, "r", encoding="utf-8") as file:
        first_line = file.readline().strip()

        if (
            first_line.split() not in list(string.punctuation)
            and len(first_line.split()) < 10
        ):
            temp.append(f"**{first_line[:2]}**{first_line[2:]}\n===\n ")
        else:
            temp.append(f"**{first_line[:2]}**{first_line[2:]}")

        # Read the remaining lines
        for line in file:
            temp.append(f"**{line[:2]}**{line[2:]}")

        for l in range(0, len(temp)):
            if temp[l] == " ":
                final_string += "\n\n"
            else:
                final_string += temp[l] + "\n"
            l += 1

    return final_string


def generate_markdown_with_headings(output_md_path):
    """Generates a"""
    text = bionify_markdown_file(output_md_path)
    md = markdown_it.MarkdownIt()

    # Configure the heading attributes
    md.options["heading_attributes"] = lambda level: {
        "id": f"heading-{level}",
        "class": "custom-heading-class",
    }

    # Convert plain text to Markdown with headings
    markdown = md.render(text)
    return markdown


def generate_html_file(content) -> None:
    """Generates HTML file from Markdown file"""

    markdown_content = html2text.html2text(content)

    # TODO - Fix hyphen issues
    # final = ""
    # for m in markdown_content.split():
    #     if m == "*":
    #         final += f"\n{m} "
    #     else:
    #         final += f"{m} "

    with open("temp.md", "w", encoding="utf-8") as file:
        file.write(markdown_content)


def create_modified_pdf(path, name) -> None:
    """Generates finalized PDF with bionic reading effects"""

    try:
        subprocess.run(["mdpdf", "-o", f"{name}.pdf", f"{path}"])
    except subprocess.CalledProcessError:
        print("Issue calling subprocess 'mdpdf' command.")


# -----------------------------------------------------------------------------------
# TODO - Delete everything below this line after updating code above
# -----------------------------------------------------------------------------------


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
