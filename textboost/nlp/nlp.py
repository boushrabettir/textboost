"""
Train Word2Vec embeddings: Use your 
dataset to train Word2Vec embeddings, 
which capture semantic relationships 
between words. Word2Vec learns word 
embeddings by predicting the context 
of words in a large corpus of text. 
This step helps in representing words 
as dense vectors in a multi-dimensional space.

Prepare the data: Tokenize your input 
text into sentences or individual words 
and convert them into Word2Vec embeddings. 
You can use the trained Word2Vec model to 
convert each word or sentence into its 
corresponding vector representation.

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

# Using BERT?
from transformers import BertTokenizer, BertForSequenceClassification

# TODO - Pip install below
from gensim.models import Word2Vec


def retrieve_data() -> List[object]:
    """Retrieves training data"""

    data = []
    with open("./nlp/data.json", "r") as file:
        data = json.load(file)

    return [i["description"] for i in data]


def vectorize_preprocessed_data() -> object:
    """Preprocesses data to a vectorized format"""

    descriptions = retrieve_data()
    tokenized = [d.lower().split() for d in descriptions]

    dimensions = 100

    model = Word2Vec(tokenized, size=dimensions, window=5, min_count=1, workers=4)

    vectorized_data = [model.wv[word] for word in tokenized[0]]

    return vectorized_data


def train_model() -> None:
    """Trains model"""
