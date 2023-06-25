from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
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

    labeling = label_folders()
    folder_path = "C:/Users/boush/OneDrive/Documents/GitHub/textboost/textboost/archive"
    folder_dir = return_list_folders()
    all_rows = []

    for folder in folder_dir:
        curr_file = os.listdir(f"{folder_path}/{folder}")
        for document in curr_file:
            with open(
                f"{folder_path}/{folder}/{document}", "r", encoding="utf-8"
            ) as file:
                all_rows.append([file.read(), labeling[folder]])

    return all_rows


class KNearestNeighbors:
    """A class defining the functionality for KNN"""

    def __init__(self, k=1):
        self.k = k
        self.tdif = TfidfVectorizer()
        self.KNN = KNeighborsClassifier(n_neighbors=3)

    def fit_list(self, X, y) -> None:
        self.X_train = X
        self.y_train = y
        self.KNN.fit(self.X_train, self.y_train)

    def transform_list(self, X) -> TfidfVectorizer:
        self.X_train = X
        return self.tdif.fit_transform(self.X_train)

    def predict_outcome(self, i) -> str:
        labels = {
            0: "business",
            1: "entertainment",
            2: "food",
            3: "graphics",
            4: "medical",
            5: "politics",
            6: "sport",
            7: "technologie",
        }

        return labels[i[0]]

    # TODO - Fix Comparison - Eucledian Distance
    def comparison(self, X_train, input):
        """Returns the index of the closest vector in X_train to the input vector"""
        transformed_input = self.tdif.transform([input])
        distances = np.linalg.norm(
            X_train.toarray() - transformed_input.toarray() ** 2, axis=1
        )
        closest_index = np.argmin(distances)
        print(closest_index)
        return closest_index

    def split_x_y(self) -> dict:
        """Splits data into X_train and y_train"""

        X_train = []
        y_train = []
        training_data = merge_training_data()

        for i in training_data:
            X_train.append(i[0])
            y_train.append(i[1])

        return {"X_train": X_train, "y_train": y_train}


def model_test(user_input) -> str:
    """Tests the model using KNN and TD-IDF to sucessfully analyze the overall subject of the corpus"""

    knn = KNearestNeighbors(k=1)

    training_data = knn.split_x_y()
    X_train = training_data["X_train"]
    y_train = training_data["y_train"]

    X_train_preprocess = stop_words_removal(X_train)
    X_train_transformed = knn.transform_list(X_train_preprocess)

    knn.fit_list(X_train_transformed, y_train)

    test = [user_input]
    new_test = knn.tdif.transform(test)
    predicted = knn.KNN.predict(new_test)
    print(predicted)
    return knn.predict_outcome(predicted)


def return_list_folders() -> List[str]:
    """Returns the list of folders"""
    folder_path = "C:/Users/boush/OneDrive/Documents/GitHub/textboost/textboost/archive"
    folder_dir = os.listdir(folder_path)

    return folder_dir


def label_folders() -> dict:
    """Labels each folder with their number"""

    labeling_dict = dict()
    folder_dir = return_list_folders()
    print(folder_dir)
    for i, folder in enumerate(folder_dir):
        labeling_dict[folder] = i
    print(labeling_dict)
    return labeling_dict
