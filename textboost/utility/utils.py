"""
https://github.com/nateshmbhat/pyttsx3
"""

from typing import List, Tuple
import os
from utility.file import File, FileUtilizer
from PyPDF2 import PdfReader
from fpdf import FPDF
from knn import knn

# TODO -> MD -> PDF -> HTML

file_utilizer = FileUtilizer([])


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
    """Checks if the user command exists within the validation list"""

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
    """Adds a file to the list of files"""

    PATH_TO_FILE, FILE_NAME = file_list
    file = File(PATH_TO_FILE, FILE_NAME)
    file_utilizer.list.append(file)

    return "Successfully added your file! Add another or process your file!"


def access_unprocessed_list() -> str:
    """Helper function to access the current files in line"""

    final_str = ""
    for i in file_utilizer.list:
        final_str += f"""
            File Path: {i.file_path}
            File Name: {i.file_name}
        """

    return final_str


def process_file_utilizer() -> None:
    """Processes each and every file in the FileUtilizer object with the functions below"""

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
            extracted_text += page.extract_text()

    words = extracted_text.split()
    formatted = []

    # TODO
    for word in words:
        bold = ""
        for i in range(0, len(word), 2):
            bold += f"\033[1m{word[i : i + 2]}\033[0m"
        formatted.append(bold)

    return " ".join(formatted)


def customized_user_pdf_creation(file_path, name) -> None:
    """Creates the customized PDF for the user"""

    pdf = FPDF()
    text = pdf_to_text_extraction(file_path)
    folder_location = knn.model_test(text)

    modified_folder = f"./modified/{folder_location}"
    if not os.path.exists(modified_folder):
        os.makedirs(modified_folder)

    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.set_text_color(0, 0, 0)

    # TODO
    cell_width = 150
    line_height = 10

    pdf.multi_cell(cell_width, line_height, text, 0, "L", False)

    pdf.output(f"{modified_folder}/{name}.pdf", "F")
