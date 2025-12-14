from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
from typing import Tuple, List
import string


class KNearestNeighbors:
    """A class defining the base functionality for KNN"""

    def __init__(self, k=10):
        self.k = k
        self.tfid = TfidfVectorizer(stop_words="english")
        self.KNN = KNeighborsClassifier(n_neighbors=self.k)

    def fit_list(self, X, y) -> None:
        """Fits X and y training data"""
        self.X_train = X
        self.y_train = y
        self.KNN.fit(self.X_train, self.y_train)

    def transform_list(self, X) -> TfidfVectorizer:
        """Transforms X training data"""
        self.X_train = X
        return self.tfid.fit_transform(self.X_train)

    def return_outcome(self, i: int) -> str:
        """Returns the folder name corresponding to predicted index"""
        folder_dir = return_list_folders()  # sorted
        return folder_dir[i]

    def comparison(self, X_train_transformed, input_text) -> int:
        """Returns the index of the closest vector in X_train to the input vector"""
        transformed_input = self.tfid.transform([input_text])
        distances = np.linalg.norm(
            (X_train_transformed.toarray() - transformed_input.toarray()) ** 2, axis=1
        )
        closest_index = np.argmin(distances)
        return self.y_train[closest_index]

    def split_x_y(self) -> dict:
        """Splits training data into X_train and y_train"""
        training_data = merge_training_data()
        X_train = [row[0] for row in training_data]
        y_train = [row[1] for row in training_data]
        return {"X_train": X_train, "y_train": y_train}


def model_test(user_input: str) -> str:
    """Predicts the folder based on user input text using KNN and TF-IDF."""

    nltk.download("punkt", quiet=True)
    nltk.download("stopwords", quiet=True)

    # Merge training data (one combined text per folder)
    training_data = merge_training_data()

    # Clean training text
    X_train = [stop_words_removal([text])[0] for text, _ in training_data]
    y_train = [label for _, label in training_data]

    # Clean user input
    input_clean = " ".join(
        [
            w
            for w in word_tokenize(user_input.lower())
            if w not in stopwords.words("english")
        ]
    )

    # Initialize KNN
    knn = KNearestNeighbors(k=1)  # k=1 is enough since one sample per folder

    # Fit KNN on TF-IDF vectors
    X_train_vec = knn.transform_list(X_train)
    knn.fit_list(X_train_vec, y_train)

    # Predict the closest folder
    predicted_index = knn.comparison(X_train_vec, input_clean)

    # Map prediction index to folder name
    predicted_folder = knn.return_outcome(predicted_index)

    return predicted_folder


def return_list_folders() -> List[str]:
    """Returns the list of folders, sorted alphabetically for deterministic behavior"""
    folder_path = "archive"
    folder_dir = sorted(os.listdir(folder_path))  # <- sorted!
    return folder_dir


def label_folders() -> dict:
    """Labels each folder with a number, consistently"""
    labeling_dict = {}
    folder_dir = return_list_folders()
    for i, folder in enumerate(folder_dir):
        labeling_dict[folder] = i
    return labeling_dict


def stop_words_removal(X_train: List[str]) -> List[str]:
    """Removes stop words and punctuation from a list of text strings"""
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
        cleaned_texts.append(
            cleaned_text.translate(str.maketrans("", "", string.punctuation))
        )

    return cleaned_texts


def merge_training_data() -> List[Tuple[str, int]]:
    """Merge all files in each folder into one text per folder for more reliable KNN."""
    labeling = label_folders()
    folder_path = "archive"
    all_rows = []

    for folder in return_list_folders():
        folder_texts = []
        for file_name in os.listdir(f"{folder_path}/{folder}"):
            with open(
                f"{folder_path}/{folder}/{file_name}", "r", encoding="utf-8"
            ) as f:
                folder_texts.append(f.read())
        combined_text = " ".join(folder_texts)
        all_rows.append((combined_text, labeling[folder]))

    return all_rows
