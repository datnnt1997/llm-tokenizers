from tokenizers.base import BaseLLMTokenizer, TokenizerOutput

import tiktoken


class OpenAITokenizer(BaseLLMTokenizer):
    __name__ = "OpenAITokenizer"

    def __init__(self, model_name: str):
        super().__init__(model_name)
        self.tokenizer = tiktoken.model.encoding_for_model(model_name)

    @classmethod
    def list_model_names(cls):
        return list(tiktoken.model.MODEL_TO_ENCODING.keys())

    def encode(self, text: str):
        return self.tokenizer.encode(text)

    def tokenize(self, text: str) -> TokenizerOutput:
        token_ids = self.encode(text)
        tokens = [token.decode("utf-8", errors='replace') for token in self.tokenizer.decode_tokens_bytes(token_ids)]
        return TokenizerOutput(
            tokens=tokens,
            token_ids=token_ids,
            num_tokens=len(tokens),
            num_chars=len(text)
        )


if __name__ == "__main__":
    tokenizer = OpenAITokenizer("gpt-4")
    text = """Many words map to one token, but some don't: indivisible.

Unicode characters like emojis may be split into many tokens containing the underlying bytes: 🤚🏾

Sequences of characters commonly found next to each other may be grouped together: 1234567890"""
    print(tokenizer(text))
    print(tokenizer.count_tokens(text))
