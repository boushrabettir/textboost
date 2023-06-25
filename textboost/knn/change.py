import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from ..utility import utils as ut
import os
from typing import Tuple, List
import string

nltk.download("stopwords")
nltk.download("punkt")


def stop_words_removal(X_train) -> List[str]:
    """Removes stop words from the corpus and cleans up punctuation"""

    cached_stop_words = stopwords.words("english")

    cleaned_texts = []

    for text in X_train:
        tokens = word_tokenize(text)
        cleaned_tokens = [
            word
            for word in tokens
            if word.lower() not in cached_stop_words and word not in string.punctuation
        ]
        cleaned_text = " ".join(cleaned_tokens)
        fixed = cleaned_text.translate(str.maketrans("", "", string.punctuation))
        cleaned_texts.append(fixed)

    return cleaned_texts


def merge_training_data() -> List[List[Tuple[str, int]]]:
    """Merges the data together within each folder - X_train and y_train"""

    labeling = ut.label_folders()
    folder_path = "../archive"
    folder_dir = ut.return_list_folders()
    all_rows = []

    for folder in folder_dir:
        curr_file = os.listdir(f"{folder_path}/{folder}")
        for document in curr_file:
            with open(
                f"{folder_path}/{folder}/{document}", "r", encoding="utf-8"
            ) as file:
                all_rows.append([file.read(), labeling[folder]])

    return all_rows
