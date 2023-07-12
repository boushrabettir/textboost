# TODO- Pip install below
import transformers
import re


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


def fine_tune_model() -> str:
    """Finetunes pretrained model for specifications in Markdown"""

    # https://huggingface.co/docs/transformers/training


# TODO https://huggingface.co/docs/transformers/model_doc/bert#transformers.models.bert.modeling_bert.BertForPreTrainingOutput.loss
def generate_markdown() -> str:
    """Generate markdown with pre-trained model"""

    tokenizer = transformers.AutoTokenizer.from_pretrained("bert-base-uncased")
    tf_tokenizer = transformers.TFBertTokenizer.from_tokenizer(tokenizer)

    tokens = tf_tokenizer(text_block, max_length=512)
    encoded_tokens = tf_tokenizer.encode_plus(tokens, return_attention_mask=True)

    markdown_string = tf_tokenizer.decode(
        encoded_tokens["input_ids"], skip_special_tokens=True
    )

    return markdown_string
