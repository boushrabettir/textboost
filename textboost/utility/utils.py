"""
https://github.com/nateshmbhat/pyttsx3
"""

from typing import List
from file import File, FileUtilizer
import file

file_utilizer = FileUtilizer([])


def cli_command_utilizer(input: any) -> str:
    """A function containing CLI command inputs"""

    validator = return_value(input)

    if validator:
        if input[0] == "--add-file":
            add_file_utilizer(input[1:])
        if input == "--process-file":
            process_file_utilizer()
        if input == "--view-unprocessed-files":
            access_unprocessed_list()
    else:
        return "Your command is not valid. Please type --help and try again."


def splitted_value(value: str) -> List[str]:
    """Splits list into its corresponding list"""

    return value.split()


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

    splitted = splitted_value(value)
    if any(splitted[0] == command for command in validator):
        return True

    return False


def add_file_utilizer(file_list: List[str]) -> FileUtilizer:
    """Adds a file to the list of files"""

    PATH_TO_FILE, FILE_NAME = file_list
    file = File(PATH_TO_FILE, FILE_NAME)
    file_utilizer.list.append(file)

    print("Successfully added your file! Add another or process your file!")
    return file_utilizer


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
        file.customized_user_pdf_creation(i.file_path, i.file_name)
