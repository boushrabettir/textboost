"""
https://github.com/nateshmbhat/pyttsx3
"""

from typing import List
import os
from utility.file import File, FileUtilizer
from PyPDF2 import PdfReader
from knn import knn
from utility import conversion as cv
import fitz

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
        if input[0] == "--delete-file":
            # TODO
            delete_file(input[1])
    else:
        return "Your command is not valid. Please type --help and try again. "


def splitted_value(values: str) -> List[str]:
    """Splits a list into its corresponding list"""

    return values.split()


def return_value(value: str) -> str:
    """Validates the users input"""

    validation_list = [
        "--add-file",
        "--find-file",
        "--delete-file",
        "--process-file",
        "--view-unprocessed-file",
    ]

    if not any(value[0] == command for command in validation_list):
        return "This is not a valid command. Please type --help and try again."


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


def delete_file(file_name: str) -> str:
    """Deletes a specific file if given by user else removes the most recent File object"""

    if file_name:
        for file in file_utilizer:
            if file_name in file[0]:
                file_utilizer.list.pop()
                break
    else:
        file_utilizer.list.pop()

    return "Sucessfully deleted. Please add a file or process your current file(s)."


def process_file_utilizer() -> None:
    """Processes file(s) from FileUtilizer"""
    print("Processing your file...")
    for i in file_utilizer.list:
        customized_user_pdf_creation(i.file_path, i.file_name)

    file_utilizer.list.clear()  # Clear the list once the pdf has been customized


def pdf_to_text_extraction(file: str) -> str:
    """Extracts text from the given PDF file by the user"""

    text = ""
    with open(file, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def customized_user_pdf_creation(file_path, name) -> None:
    """Creates the customized PDF for the user"""

    text = pdf_to_text_extraction(file_path)

    folder_location = knn.model_test(text)

    modified_folder = f"./modified/{folder_location}"
    if not os.path.exists(modified_folder):
        os.makedirs(modified_folder)

    cv.modify_content(file_path, name, modified_folder)
    cv.md_to_pdf(name, modified_folder)
