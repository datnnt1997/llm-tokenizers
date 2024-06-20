from tokenizers.base import BaseLLMTokenizer
from tokenizers.openai import OpenAITokenizer


def __regist_model_to_encoding() -> dict[str, str]:
    providers = [OpenAITokenizer]
    model_to_encoding = {}
    for provider in providers:
        for model_name in provider.list_model_names():
            model_to_encoding[model_name] = provider.__name__
    return model_to_encoding


def __regist_model_to_constructor() -> dict[str, BaseLLMTokenizer]:
    providers = [OpenAITokenizer]
    model_to_constructor = {}
    for provider in providers:
            model_to_constructor[provider.__name__] = provider
    return model_to_constructor


MODEL_TO_ENCODING: dict[str, str] = {
    **__regist_model_to_encoding()
}

MODEL_TO_CONSTRUCTOR: dict[str, BaseLLMTokenizer] = {
    **__regist_model_to_constructor()
}


if __name__ == "__main__":
    print(MODEL_TO_ENCODING)
    print(MODEL_TO_CONSTRUCTOR)
