"""
Apply BERT model: BERT is a transformer-based model
that can understand the contextual relationships 
between words. You can use a pre-trained BERT model 
and fine-tune it on your specific task, such as 
title detection. Feed the Word2Vec embeddings of 
the input text into the BERT model.

Train the model: Train the BERT model on a labeled 
dataset where the titles are annotated. The model 
will learn to recognize the patterns and features 
that indicate the presence of a title in the text.

Prediction: Once the model is trained, you can input a 
new text and let the model predict the presence 
and location of the title within the text. The model 
will provide the predicted title or highlight the 
relevant portion of the text that represents the title.
"""
from typing import List
import json
import tensorflow as tf
import numpy as np


# TODO - Pip install below

import tensorflow_hub as hb
import tensorflow_text as txt


def retrieve_data() -> List[object]:
    """Retrieves training data"""

    data = []
    with open("./nlp/data.json", "r") as file:
        data = json.load(file)

    return data


# TODO  - Go in depth with what I've learned.
# Google colab -> https://colab.research.google.com/drive/1E1OqfBmSRNFbg4OcMnrAPT_1k4HJoSZS#scrollTo=MJ7PXwkwfWpJ


def vectorize_data_t2() -> dict:
    """Returns the vectorized descriptions using BERT"""

    description_data_holder = []
    title_data_holder = []
    descriptions = retrieve_data()
    for d in descriptions:
        description_data_holder.append(d["description"])
        title_data_holder.append(d["title"])

    encoder_model = "https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4"
    preprocess = "https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3"

    preprocess_bert = hb.KerasLayer(preprocess)
    preprocessed_description = preprocess_bert(description_data_holder)
    preprocessed_title = preprocess_bert(title_data_holder)

    model = hb.KerasLayer(encoder_model)
    description_result = model(preprocessed_description)
    title_result = model(preprocessed_title)

    return {
        "processed_titles": title_result["pooled_output"],
        "processed_descriptions": description_result["pooled_output"],
    }


# https://www.tensorflow.org/text/tutorials/classify_text_with_bert
def train_model() -> None:
    """Trains model"""
