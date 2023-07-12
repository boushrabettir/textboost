# TODO- Pip install below
import transformers
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
import re
import csv
from typing import List
import pandas as pd
import numpy as np


# TODO - After figuring out this, modify conversion file
def modify_markdown_file(file_path: str) -> None:
    """Removes the first and last line of Markdown file"""

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    pattern = r'<a\s+name="br\d+"></a>'
    lines = [line for line in lines if not re.search(pattern, line)]

    # Write the updated content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


def read_file(file_path: str) -> str:
    """Returns the file text"""

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


modify_markdown_file("")
text_block = read_file("")


# TODO - Update dummy dataset
# https://huggingface.co/docs/transformers/model_doc/bert#transformers.models.bert.modeling_bert.BertForPreTrainingOutput.loss

dummy_dataset = [
    {"text": "This is a bold text.", "label": "**This is a bold text.**"},
    {"text": "Here is an italicized text.", "label": "*Here is an italicized text.*"},
    {"text": "This is a code snippet.", "label": "`This is a code snippet.`"},
    {"text": "This is a Heading 1", "label": "# This is a Heading 1"},
    {"text": "This is a Heading 2", "label": "## This is a Heading 2"},
    {"text": "This is a Heading 3", "label": "### This is a Heading 3"},
    {
        "text": "Here is a link to a website.",
        "label": "[Here is a link to a website.](https://www.example.com)",
    },
    {
        "text": "Here is a list:\n- Item 1\n- Item 2\n- Item 3",
        "label": "Here is a list:\n\n- Item 1\n- Item 2\n- Item 3",
    },
    {
        "text": "Here is a numbered list:\n1. Item 1\n2. Item 2\n3. Item 3",
        "label": "Here is a numbered list:\n\n1. Item 1\n2. Item 2\n3. Item 3",
    },
    {
        "text": "Here is an example of a table:\n| Column 1 | Column 2 |\n| -------- | -------- |\n| Data 1   | Data 2   |",
        "label": "Here is an example of a table:\n\n| Column 1 | Column 2 |\n| -------- | -------- |\n| Data 1   | Data 2   |",
    },
]


def create_csv() -> None:
    """Only called once. Creates csv file for datset."""

    file_path = "./markdown.csv"
    field_names = ["text", "label"]

    try:
        with open(file_path, "w", encoding="utf-8", newline="") as file:
            w = csv.DictReader(file, fieldnames=field_names)

            w.writeHeader()
            w.writerows(dummy_dataset)
    except OSError:
        print("Error creating csv file.")

    print("CSV file created.")


def tokenize_data(path: str, tokenizer_object) -> object:
    """Tokenzies the given dataset"""

    df = pd.read_csv(path)

    preprocessed_X_set = list(df["text"])
    preprocessed_Y_set = list(df["label"])

    X_set = []
    y_set = []

    for X_elem, y_elem in zip(preprocessed_X_set, preprocessed_Y_set):
        # Apply padding to ensure equal lengths

        tokenized_X_element = tokenizer_object(
            X_elem, padding="max_length", truncation=True
        )
        tokenized_y_element = tokenizer_object(
            y_elem, padding="max_length", truncation=True
        )

        X_set.append(tokenized_X_element)
        y_set.append(tokenized_y_element)

    return {"X_set": X_set, "y_set": y_set}


# TODO - Continue to finetune bert model
def fine_tune_model(bert_tokenzier) -> any:
    """Finetunes pretrained model for specifications in Markdown"""
    # https://stackoverflow.com/questions/61708486/whats-difference-between-tokenizer-encode-and-tokenizer-encode-plus-in-hugging
    # https://huggingface.co/docs/transformers/training

    model = transformers.TFAutoModelForSequenceClassification.from_pretrained(
        "bert-base-cased"
    )

    data = tokenize_data("./markdown.csv", bert_tokenzier)
    tokenized_X_set = data["X_set"]
    tokenized_Y_set = data["y_set"]

    # Mapping between tokens and their respective id's
    input_id = tf.concat(element["input_ids"] for element in tokenized_X_set)

    # Attention mask is used to prevent the model from looking at padded tokens
    attention_masks = tf.concat(
        element["attention_masks"] for element in tokenized_X_set
    )
    labels_input_id = tf.concat(element["input_ids"] for element in tokenized_Y_set)

    # Hugging face automatically chooses a loss thats appropriate for this task
    model.compile(optimizer=Adam(3e-5))

    model.fit(
        X={"input_ids": input_id, "attention_mask": attention_masks},
        y=labels_input_id,
        batch_size=16,
        epochs=10,
    )

    return model


def generate_markdown(model, text: str) -> str:
    """Generate markdown with pre-trained model"""

    tokenizer = transformers.AutoTokenizer.from_pretrained("bert-base-cased")

    tokenized_text = tokenizer.encode_plus(
        text, padding="max_length", truncation=True, return_tensors="tf"
    )

    # https://jaketae.github.io/category/common-sense/#:~:text=Simply%20calling%20the%20tokenizer%20results%20in%20a%20dictionary%2C,prevent%20the%20model%20from%20looking%20at%20padding%20tokens.

    # Mapping between tokens and their respective id's
    input_ids = tokenized_text["input_ids"]

    # Attention mask is used to prevent the model from looking at padded tokens
    attention = tokenized_text["attention_mask"]

    # Predict markdown

    predicted_input_ids = model.predict(
        {"input_ids": input_ids, "attention": attention}
    )
    predicted_labels = tf.argmax(predicted_input_ids)

    # Decode text
    markdown = tokenizer.decode(predicted_labels.squeeze(), skip_special_tokens=True)

    return markdown
