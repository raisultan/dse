from pymilvus import CollectionSchema, FieldSchema, DataType

MODEL_CHUNK_SIZE = 8192
MODEL_OUTPUT_DIMENSIONS = 1536  # float vector dimensions


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
collection_name = "ads"
