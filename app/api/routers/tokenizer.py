from typing import Any

from fastapi import APIRouter

from tokenizers import MODEL_TO_ENCODING
from tokenizers.main import tokenize

from app.models import ModelsPublic, TokenizerInput, TokenizerOutput

router = APIRouter()


@router.get("/", summary="List available model names", response_model=ModelsPublic)
async def list_model_names() -> Any:
    return ModelsPublic(data=list(MODEL_TO_ENCODING.keys()), count=len(MODEL_TO_ENCODING))


@router.post("/tokenize", summary="Tokenize text", response_model=TokenizerOutput)
async def tokenize_text(inputs: TokenizerInput) -> Any:
    response = tokenize(inputs.model_name, inputs.text)

    return TokenizerOutput(
        tokens=response.tokens,
        token_ids=response.token_ids,
        num_tokens=response.num_tokens,
        num_chars=response.num_chars
    )
