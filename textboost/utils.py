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
