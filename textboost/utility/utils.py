from typing import List
import os
from utility.file import File, FileUtilizer
import utility.conversion as cv
from ml import knn
from functools import partial

file_utilizer = FileUtilizer([])  # Holds the List[File]


def cli_command_utilizer(user_input: str, action_type: str) -> str:
    """A function containing CLI command user_inputs"""

    # Validates user input
    validator = return_value(len(user_input), action_type)

    # Determines which button was pressed
    action_to_function = {
        "add": partial(add_file_utilizer, user_input),
        "process": partial(process_file_utilizer, user_input),
        "view": access_unprocessed_list,
        "delete": partial(delete_file, user_input),
        "find": partial(find_file, user_input),
    }

    # If the user is valid, call the respective function
    if validator:
        return action_to_function[action_type]()

    return "Your command is not valid. Please type --help and try again."


def splitted_value(values: str) -> List[str]:
    """Splits a list into its corresponding list"""

    return values.split()


def return_value(user_input: str, action_type: str) -> bool:
    """Validates the users input"""

    # For each key, the corresponding value represents the size of the user input
    validation_object = {
        "add": [2],
        "process": [1],
        "view": [0],
        "delete": [0, 1],
        "find": [1],
    }

    # Determines if the file to path is valid
    valid_path = True
    # TODO-
    # user_splitted_input = user_input.split()
    if action_type == "add":
        valid_path = False

    value = validation_object[action_type]

    return (False if user_input not in value else True) and valid_path


def add_file_utilizer(file_list: List[str]) -> str:
    """Adds a file to the list of file(s)"""

    path_to_file, file_name = file_list

    # Create file object
    file = File(path_to_file, file_name)
    file_utilizer.list.append(file)

    return f"Successfully added '{path_to_file}'!"


def access_unprocessed_list() -> str:
    """Helper function to access the current unprocessed file(s)"""

    final_str = ""
    for i in file_utilizer.list:
        final_str += f"""
            File Path: {i.file_path}
            File Name: {i.file_name}\n
        """

    return final_str


def delete_file(file_name: str = "") -> str:
    """Deletes a specific file if given by user else removes the most recent File object"""

    # Specific file names will be deleted from the file utilizer list
    if file_name:
        index = file_utilizer.list.index(file_name)
        file_utilizer.list.pop(index)
    # Remove last file if no input is given
    else:
        file_utilizer.list.pop()

    return "Sucessfully deleted file."


def process_file_utilizer(user_input: str) -> None:
    """Processes file(s) from unprocessed list"""

    for i in file_utilizer.list:
        customized_user_pdf_creation(i.file_path, i.file_name, user_input)

    file_utilizer.list.clear()  # Clear the list once the pdf has been customized


def find_file(user_input: str) -> str:
    """Finds specific file from unprocessed list"""

    try:
        index = file_utilizer.list.index(user_input)
        return f"File found: {file_utilizer.list[index]}."
    except ValueError:
        return f"File '{user_input}' not found in list."


# ----------- PDF Creation -----------


def pdf_to_text_extraction(file: str) -> str:
    """Extracts text from the given PDF file by the user"""

    text = ""
    with open(file, "r", encoding="latin-1") as file:
        text = file.read()

    return text


def customized_user_pdf_creation(file_path: str, name: str, summarize: str) -> str:
    """Creates the customized PDF for the user"""

    # Extracts text from markdown
    text = pdf_to_text_extraction(file_path)

    # Download necessary resources
    knn.download_resources()

    # Determines folder location dependent on the model
    folder_location = knn.model_test(text)

    # Create modified folder in string literal
    modified_folder = f"./modified/{folder_location}"

    # Create the folder if the folder doesn't already exist
    if not os.path.exists(modified_folder):
        os.makedirs(modified_folder)

    # Modify the content with bionic reading effects
    cv.modify_content(file_path, name, modified_folder, summarize)

    # Create PDF from the modified markdown
    cv.md_to_pdf(name, modified_folder)

    return f"PDF sucessfully created. Please check '{folder_location}' for your modified PDF."
