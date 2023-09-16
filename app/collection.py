from pymilvus import Collection, CollectionSchema, FieldSchema, DataType

from app.embedding import create_embedding

MODEL_CHUNK_SIZE = 8192
MODEL_OUTPUT_DIMENSIONS = 1536  # float vector dimensions


# Schem Fields
ad_id = FieldSchema(
  name="id",
  dtype=DataType.INT64,
  is_primary=True,
  auto_id=False,
)
project_name = FieldSchema(
  name="project_name",
  dtype=DataType.VARCHAR,
  max_length=200,
)
ad_embeddings = FieldSchema(
  name="embeddings",
  dtype=DataType.FLOAT_VECTOR,
  dim=MODEL_OUTPUT_DIMENSIONS,
)

schema = CollectionSchema(
  fields=[ad_id, project_name, ad_embeddings],
  description="Ads",
)
collection_name = "ad"


# Creating a Colection
def create_collection() -> None:
    return Collection(
        name=collection_name,
        schema=schema,
    )


async def insert_ads(collection: Collection, ads: list[dict]) -> None:
    ads_to_insert = []
    for ad in ads:
        ad_text_embedding = await create_embedding(ad['text'])
        ads_to_insert.append({
            "id": ad["id"],
            "project_name": ad["project_name"],
            "embeddings": ad_text_embedding,
        })
    collection.insert(ads_to_insert)
    collection.flush()


async def build_ads_indexes(collection: Collection) -> None:
    index = {
        "index_type": "IVF_FLAT",
        "metric_type": "L2",
        "params": {"nlist": 128},
    }
    collection.create_index("embeddings", index)


async def load_ads(collection: Collection) -> Collection:
    collection.load()


ads = [
    {
        "id": 1,
        "project_name": "test_1",
        "text": "The shards_num parameter in the Collection constructor specifies the number of shards to create for the collection. A shard is a logical partition of a collection. Shards are distributed across multiple data nodes in a Milvus cluster.",
    },
    {
        "id": 2,
        "project_name": "test_1",
        "text": "When you insert data into a collection, Milvus will distribute the data across the shards. This allows Milvus to handle large datasets and perform similarity search efficiently.",
    },
    {
        "id": 3,
        "project_name": "test_1",
        "text": "The number of shards you need will depend on the size and complexity of your dataset. If you have a small dataset, you may only need a few shards. If you have a large and complex dataset, you may need more shards.",
    },
    {
        "id": 4,
        "project_name": "test_1",
        "text": "The shards_num parameter in the collection constructor specifies the number of shards to create for the collection. A shard is a logical partition of a so called collection. The shards are distributed across multiple data nodes in a Milvus cluster.",
    },
]
