from transformers import T5Tokenizer, T5ForConditionalGeneration


def summarize(text: str) -> str:
    """Pre-trained model summarizing text"""

    tokenizer = T5Tokenizer.from_pretrained("d0rj/rut5-base-summ")
    model = T5ForConditionalGeneration.from_pretrained("d0rj/rut5-base-summ").eval()

    input_ids = tokenizer(text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary
