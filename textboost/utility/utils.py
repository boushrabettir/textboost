"""
https://github.com/nateshmbhat/pyttsx3
"""

from typing import List
import os
from utility.file import File, FileUtilizer, key_type, index
from PyPDF2 import PdfReader
from knn import knn
import subprocess


file_utilizer = FileUtilizer([])  # Holds the List[File]


def cli_command_utilizer(input: any) -> str:
    """A function containing CLI command inputs"""

    validator = return_value(input)

    if validator:
        if input[0] == "--add-file":
            add_file_utilizer(input[1:])
        if input[0] == "--process-file":
            process_file_utilizer()
        if input[0] == "--view-unprocessed-files":
            access_unprocessed_list()
    else:
        return "Your command is not valid. Please type --help and try again. "


def splitted_value(values: str) -> List[str]:
    """Splits a list into its corresponding list"""

    return values.split()


def help() -> str:
    """Returns the list of avaliable commands"""


def return_value(value: str) -> str:
    """Validates the users input"""

    validator = [
        "--add-file",
        "--find-file",
        "--delete-file",
        "--process-file",
        "--view-unprocessed-file",
        "--read-file",
        "--help",
    ]

    if any(value[0] == command for command in validator):
        return True

    return False


def add_file_utilizer(file_list: List[str]) -> str:
    """Adds a file to the list of file(s)"""

    PATH_TO_FILE, FILE_NAME = file_list
    file = File(PATH_TO_FILE, FILE_NAME)
    file_utilizer.list.append(file)

    return "Successfully added your file! Add another or process your file!"


def access_unprocessed_list() -> str:
    """Helper function to access the current unprocessed file(s)"""

    final_str = ""
    for i in file_utilizer.list:
        final_str += f"""
            File Path: {i.file_path}
            File Name: {i.file_name}
        """

    return final_str


def process_file_utilizer() -> None:
    """Processes file(s) from FileUtilizer"""

    for i in file_utilizer.list:
        customized_user_pdf_creation(i.file_path, i.file_name)
    print("Processing your file...")
    file_utilizer.list.clear()  # Clear the list once the pdf has been customized


def pdf_to_text_extraction(file: str) -> str:
    """Extracts text from the given PDF file by the user"""

    with open(file, "rb") as fl:
        reader = PdfReader(fl)

        extracted_text = ""

        for current_page in range(len(reader.pages)):
            page = reader.pages[current_page]
            page_text = page.extract_text()

            extracted_text += page_text

    return extracted_text


# TODO
def str_to_md(text: str, name: str, folder: str) -> None:
    """Converts string to markdown file"""
    index = 1
    formatted_list = []
    words = text.split()
    for word in words:
        if word in key_type:
            formatted_list.append(key_type[word])
            if word == f"{index}" or word == f"{index}.":
                index += 1
        else:
            formatted_list.append(f"**{word[:2]}**{word[2:]}")

    final_string = " ".join(formatted_list)

    directory = "modified"
    file_path = os.path.join(directory, folder, f"{name}.md")

    try:
        with open(file_path, "w") as md:
            md.write(final_string)
        print(f"Markdown file '{name}.md' created successfully.")
    except Exception as e:
        print(f"Error occurred while creating the Markdown file: {str(e)}")


def md_to_pdf(name: str, folder: str) -> None:
    """Converts markdown file to PDF file"""

    try:
        subprocess.run(
            f"mdpdf -o modified/{folder}/{name}.pdf modified/{folder}/{name}.md "
        )
    except subprocess.CalledProcessError:
        print("Error calling subprocess.")
    except FileNotFoundError:
        print(f"File '{name}.md' not found.")

    os.remove(f"modified/{folder}/{name}.md")


def customized_user_pdf_creation(file_path, name) -> None:
    """Creates the customized PDF for the user"""

    text = pdf_to_text_extraction(file_path)

    folder_location = knn.model_test(text)

    modified_folder = f"./modified/{folder_location}"
    if not os.path.exists(modified_folder):
        os.makedirs(modified_folder)

    str_to_md(text, name, folder_location)
    md_to_pdf(name, folder_location)
