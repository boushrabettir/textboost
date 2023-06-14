from dataclasses import dataclass
from typing import List
from PyPDF2 import PdfReader
from fpdf import FPDF


@dataclass
class File:
    """Struct to hold file related data"""

    file_path: str
    font_size: str
    bolding_per_word: str
    file_name: str


@dataclass
class FileUtilizer:
    """Holds the current List[File]"""

    list: List[File]


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
