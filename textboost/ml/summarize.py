import transformers
from transformers import pipeline
from typing import List
import logging

# Stopping logging information shown on terminal
logging.getLogger("transformers").setLevel(logging.WARNING)
transformers.logging.set_verbosity_error()

# Create summarization pipeline instance
SUMMARIZATION_PIPELINE = pipeline("summarization")

# Max chunk words per sentences
MAX_TEXT_CHUNK = 500


def pdf_to_text_extraction(file: str) -> str:
    """Extracts text from the given PDF file by the user"""

    text = ""
    with open(file, "r", encoding="latin-1") as file:
        text = file.read()

    return text


def split_content(file_path: str) -> List[str]:
    """Splits content for preprocessing"""

    content = pdf_to_text_extraction(file_path)

    # Modify content for summarization
    content = content.replace(".", ".<eos>")
    content = content.replace("?", "?<eos>")
    content = content.replace("!", "!<eos>")
    content = content.replace("#", "")
    content = content.replace("##", "")
    content = content.replace("###", "")
    content = content.replace("####", "")
    content = content.replace("*", "")
    content = content.replace("**", "")

    sentences = content.split("<eos>")

    for indx, sentence in enumerate(sentences):
        if sentence == "":
            sentences.pop(indx)
        else:
            sentence = sentence.strip()

    return sentences


def create_chunks(file_path: str) -> List[str]:
    """Creates text chunks for summarization per chunk"""

    # Holds the word count of the current chunk
    current_chunk = 0

    # Holds all the text chunks
    text_chunk = []

    sentences = split_content(file_path)

    for sentence in sentences:
        if len(text_chunk) == current_chunk + 1:
            if (
                len(text_chunk[current_chunk]) + len(sentence.split(" "))
                <= MAX_TEXT_CHUNK
            ):
                text_chunk[current_chunk].extend(sentence.split(" "))
            else:
                current_chunk += 1
                text_chunk.append(sentence.split(" "))

        else:
            text_chunk.append(sentence.split(" "))

    for indx in range(len(text_chunk)):
        text_chunk[indx] = " ".join(text_chunk[indx])

    return text_chunk


def create_summarization(file_path: str) -> str:
    """Summarizes analyzed PDF"""

    text_chunks = create_chunks(file_path)

    response = SUMMARIZATION_PIPELINE(
        text_chunks, max_length=150, min_length=30, do_sample=False
    )

    # Create joined response
    finalized_response = " ".join([s["summary_text"] for s in response])

    return finalized_response
