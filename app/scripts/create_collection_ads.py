from pymilvus import Collection, connections

from app.config import load_config
from app.schemas.ads import collection_name, schema


def connect_milvus():
    config = load_config()
    connections.connect(
        alias="default",
        user='username',
        password='password',
        host=config['milvus_host'],
        port=config['milvus_port'],
    )


def disconnect_milvus():
    connections.disconnect("default")


def build_ads_indexes(collection: Collection) -> None:
    index = {
        "index_type": "IVF_FLAT",
        "metric_type": "L2",
        "params": {"nlist": 128},
    }
    collection.create_index("embeddings", index)


def load_ads_collection(collection: Collection) -> Collection:
    collection.load()


def create_collection_ads():
    connect_milvus()

    collection = Collection(
        name=collection_name,
        schema=schema,
    )
    build_ads_indexes(collection)
    load_ads_collection(collection)

    disconnect_milvus()


if __name__ == "__main__":
    create_collection_ads()
