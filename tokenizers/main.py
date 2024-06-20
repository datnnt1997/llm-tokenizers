from tokenizers.base import TokenizerOutput
from tokenizers import MODEL_TO_CONSTRUCTOR, MODEL_TO_ENCODING


def __validate_model(model_name: str) -> bool:
    """
    Validate model name
    :param model_name:
    :return:
    """
    if model_name not in MODEL_TO_ENCODING:
        raise ValueError(f"Model name '{model_name}' not found")
    return True


def tokenize(model_name: str, text: str) -> TokenizerOutput:
    """
    Tokenize text
    :param model_name:
    :param text:
    :return:
    """
    __validate_model(model_name)
    tokenizer = MODEL_TO_CONSTRUCTOR[MODEL_TO_ENCODING[model_name]](model_name)
    return tokenizer.tokenize(text)
