import openai

EMBEDDING_MODEL = 'text-embedding-ada-002'
EMBEDDING_CTX_LENGTH = 8191
EMBEDDING_ENCODING = 'cl100k_base'

async def create_embedding(text: str, model: str = EMBEDDING_MODEL) -> str:
    return openai.Embedding.create(input=text, model=model)["data"][0]["embedding"]
