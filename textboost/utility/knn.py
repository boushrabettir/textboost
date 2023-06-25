from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import change as ch


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
            6: "space",
            7: "sport",
            8: "technologie",
        }
        return labels[i]

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
        training_data = ch.merge_training_data()

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

    X_train_preprocess = ch.stop_words_removal(X_train)
    X_train_transformed = knn.transform_list(X_train_preprocess)

    knn.fit_list(X_train_transformed, y_train)

    test = ["Potato"]
    new_test = knn.tdif.transform(test)
    predicted = knn.KNN.predict(new_test)
    print(knn.predict_outcome(predicted))
    return knn.predict_outcome(predicted)


model_test("nice")
