from pymilvus import Collection

from app.embedding import create_embedding


def insert_ads(collection: Collection, ads: list[dict]) -> None:
    ads_to_insert = []
    for ad in ads:
        ad_text_embedding = create_embedding(ad['text'])
        ads_to_insert.append({
            "id": ad["id"],
            "project_name": ad["project_name"],
            "embeddings": ad_text_embedding,
        })
    collection.insert(ads_to_insert)
    collection.flush()
