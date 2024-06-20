from pydantic import BaseModel


class ModelsPublic(BaseModel):
    """
    ModelsPublic is a class response to return the list of available models.
    """
    data: list[str]
    count: int


class TokenizerInput(BaseModel):
    """
    TokenizerInput is a class to validate the input data for the tokenizer service.
    """
    text: str
    model_name: str


class TokenizerOutput(BaseModel):
    """
    Define output of the tokenizer as a dictionary with keys: "tokens", "token_ids", "num_tokens", "num_chars"
    """
    tokens: list[str]
    token_ids: list[int]
    num_tokens: int
    num_chars: int
