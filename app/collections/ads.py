from pymilvus import Collection

from app.embedding import create_embedding


class AdsCollection:
    def __init__(self, collection: Collection) -> None:
        self._collection = collection

    async def insert_entity(self, ad_id: str, project_name: str, text: str) -> None:
        entity = await self._prepare_entity_for_insert(ad_id, project_name, text)
        self._collection.insert(entity)
        self._collection.flush()

    async def _prepare_entity_for_insert(
        self, ad_id: str,
        project_name: str,
        text: str,
    ) -> None:
        text_embedding = await create_embedding(text)
        data = ({
            "id": ad_id,
            "project_name": project_name,
            "embeddings": text_embedding,
        })
        return data
