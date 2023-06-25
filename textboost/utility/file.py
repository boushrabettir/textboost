from dataclasses import dataclass
from typing import List
from PyPDF2 import PdfReader
from fpdf import FPDF
from ..knn import knn


@dataclass
class File:
    """Struct to hold file related data"""

    file_path: str
    file_name: str


@dataclass
class FileUtilizer:
    """Struct which holds the current List[File]"""

    list: List[File]


def pdf_to_text_extraction(file: str) -> str:
    """Extracts text from the given PDF file by the user"""

    with open(file, "rb") as fl:
        reader = PdfReader(fl)

        extracted_text = ""

        for current_page in range(len(reader.pages)):
            page = reader.pages[current_page]
            extracted_text += page.extract_text()

    return extracted_text


def customized_user_pdf_creation(file_path, name) -> None:
    """Creates the customized PDF to the user"""

    pdf = FPDF()
    text = pdf_to_text_extraction(file_path)
    folder_location = knn.model_test(text)
    pdf.add_page()
    pdf.set_font("Arial", 16)
    pdf.cell(40, 10, text)
    pdf.output(f"{folder_location}/{name}.pdf", "F")
