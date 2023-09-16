import os

from dotenv import load_dotenv

load_dotenv()


def load_config() -> dict:
    return {
        'openai_secret': os.environ['OPENAPI_SECRET'],
        'milvus_host': os.environ['MILVUS_HOST'],
        'milvus_port': os.environ['MILVUS_PORT'],
    }
