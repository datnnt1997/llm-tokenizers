from abc import ABC, abstractmethod

from pydantic import BaseModel


class TokenizerOutput(BaseModel):
    """
    Define output of the tokenizer as a dictionary with keys: "tokens", "input_ids", "num_tokens", "num_chars"
    """
    tokens: list[str]
    token_ids: list[int]
    num_tokens: int
    num_chars: int

    def __str__(self):
        return f"TokenizerOutput(num_tokens={self.num_tokens}, num_chars={self.num_chars}, tokens={self.tokens}, token_ids={self.token_ids})"


class BaseLLMTokenizer(ABC):
    __name__ = "BaseLLMTokenizer"

    def __init__(self, model_name: str):
        self.model_name = model_name

    def __str__(self):
        return f"{self.__name__}({self.model_name})"

    def __repr__(self):
        return f"{self.__name__}({self.model_name})"

    @classmethod
    @abstractmethod
    def list_model_names(cls) -> list[str]:
        """List available model names"""
        raise NotImplementedError("list_model_names method must be implemented")

    @abstractmethod
    def encode(self, text: str) -> list[int]:
        """Encode text into token ids"""
        raise NotImplementedError("Encode method must be implemented")

    @abstractmethod
    def tokenize(self, text: str) -> TokenizerOutput:
        raise NotImplementedError("Tokenize method must be implemented")

    def count_tokens(self, text: str) -> int:
        return len(self.encode(text))

    def __call__(self, text: str) -> TokenizerOutput:
        return self.tokenize(text)


