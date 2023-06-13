"""
IDEAS IN UTILS.PY FILE

1. Use Textual to create a command-line interface (CLI).

2. Implement commands for various functionalities, such 
as processing text files or scraping web content.

3. Provide options within commands for customization, 
such as adjusting bold formatting or specifying input/output files.

4. Handle errors and exceptions using Textual's 
error handling mechanisms.

5. Create a user-friendly CLI interface with informative prompts, 
messages, and progress indicators.

6. Utilize Textual's logging capabilities to record 
important events and provide feedback to the user.

7. Incorporate Textual's input validation features to ensure valid user inputs.

8. Use Textual's built-in commands for common 
operations like help, exit, or command history.

9. Integrate text-to-speech functionality using the pyttsx3 library.
https://www.geeksforgeeks.org/convert-text-speech-python/
https://github.com/nateshmbhat/pyttsx3
"""
from PyPDF2 import PdfReader
from fpdf import FPDF
from typing import List
import argparse
from file import File

# TODO -
FILE_TYPE_LIST: List[File] = []
PATH_TO_FILE: str = ""
FONT_SIZE: str = ""
BOLDING: str = ""
FILE_NAME: str = "output"


def cli_command_utilizer() -> None:
    """A function containing cli command inputs"""

    parser = argparse.ArgumentParser(description="Command to navigate Textboost")

    parser.add_argument(
        "--add-file",
        nargs=4,
        metavar=("file_name", "font_size", "bolding_per_char", "name_of_file"),
        help="Add the relative path to your file along with font size, bolding per word, and file name.",
    )

    parser.add_argument(
        "--find-file", type=str, help="Add name of file to find relative path."
    )

    parser.add_argument(
        "--process-file",
        type=None,
        help="Process all files.",
    )

    parser.add_argument(
        "--view-unprocessed-file", type=None, help="View all unprocessed file(s)."
    )

    arguments = parser.parse_args()

    # Conditions dependent on CLI command

    if arguments.add_file:
        add_file_utilizer(arguments.add_file)

    if arguments.find_file:
        """"""
        pass

    elif arguments.process_file:
        process_file_utilizer()


def add_file_utilizer(file_list: List[str]) -> List[File]:
    """Adds a file to the list of files"""
    # TODO - For the class, self.list

    print(file_list[1])
    PATH_TO_FILE = file_list[0]
    FONT_SIZE = file_list[1]
    BOLDING = file_list[2]
    FILE_NAME = file_list[3]

    file = File(PATH_TO_FILE, FONT_SIZE, BOLDING, FILE_NAME)

    FILE_TYPE_LIST.append(file)

    return FILE_TYPE_LIST


def process_file_utilizer() -> List[File]:
    """Processes each and every file in the List[File]"""
    pass


# -----------------------------------------------------


def pdf_to_text_extraction(file: str) -> str:
    """Extracts text from the given PDF file by the user"""
    with open(file, "rb") as fl:
        reader = PdfReader(fl)

        extracted_text = ""

        for current_page in reader.pages():
            extracted_text += current_page.extract_text()

    return extracted_text


def customized_user_pdf_creation(extracted_text, font_size) -> None:
    """Creates the customized PDF to the user"""
    pass
