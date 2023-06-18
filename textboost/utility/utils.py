"""
https://github.com/nateshmbhat/pyttsx3
"""

from typing import List
import argparse
from file import File, FileUtilizer

# import file as fl


def cli_command_utilizer() -> str:
    """A function containing CLI command inputs"""

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
    parser.add_argument(
        "--delete-file", type=None, help="Deletes the most recent added file."
    )
    parser.add_argument("--read-file", type=str, help="Helps read pdf file")
    parser.add_argument("--help", str=None, help="Views all avaliable commands")

    arguments = parser.parse_args()

    if arguments.add_file:
        # Handle add-file command
        return "add-file command successfully called"

    if arguments.find_file:
        # Handle find-file command
        return "find-file command successfully called"

    if arguments.process_file:
        # Handle process-file command
        return "process-file command successfully called"

    if arguments.view_unprocessed_file:
        # Handle view-unprocessed-file command
        return "view-unprocessed-file command successfully called"

    if arguments.delete_file:
        # Handle delete-file command
        return "delete-file command successfully called"

    if arguments.read_file:
        # Handle read-file command
        pass

    if arguments.help:
        # Handles help command
        pass

    return f"Please try again, no valid command was given."


cli_command_utilizer()


def help() -> str:
    """Returns the list of avaliable commands"""


def add_file_utilizer(file_list: List[str]) -> str:
    """Adds a file to the list of files"""

    # PATH_TO_FILE = file_list[0]
    # FONT_SIZE = file_list[1]
    # BOLDING = file_list[2]
    # FILE_NAME = file_list[3]

    # file = File(PATH_TO_FILE, FONT_SIZE, BOLDING, FILE_NAME)

    # file_utilizer = FileUtilizer([])
    # file_utilizer.list.append(file)
    # print(file_utilizer)
    return "Called File Utilizer"


def access_unprocessed_list() -> str:
    """Helper function to access the current files in line"""
    return "Called accseed"


def process_file_utilizer() -> str:
    """Processes each and every file in the List[File] with the functions below"""
    # all_files = access_unprocessed_list()
    return "Called Processed"
    # e.g. fl.pdf_to_text_extraction({FILE_PATH})
    # e.g. fl.customized_user_pdf_creation({ARGS})
