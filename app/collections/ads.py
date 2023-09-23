from pymilvus import Collection

from app.embedding import create_embedding


class AdsCollection:
    def __init__(self, collection: Collection) -> None:
        self._collection = collection

    async def insert_entity(self, ad_id: str, project_name: str, text: str) -> None:
        entity = await self._prepare_entity_for_insert(ad_id, project_name, text)
        self._collection.insert(entity)
        self._collection.flush()

    async def search(self, project_name: str, text) -> list[dict]:
        self._collection.load()
        entity_to_search = create_embedding(text)
        search_params = {
            "metric_type": "L2",
            "params": {"nprobe": 10},
        }
        raw_result = self._collection.search(
            [entity_to_search],
            "embeddings",
            search_params,
            expr=f"project_name == '{project_name}'",
            limit=3,
            output_fields=["id", "project_name"],
        )
        result = []
        for hits in raw_result:
            for hit in hits:
                entity = hit.entity
                result.append({
                    "id": entity.get("id"),
                    "project_name": entity.get("project_name"),
                    "distance": hit.distance,
                })
        return result

    async def _prepare_entity_for_insert(
        self, ad_id: str,
        project_name: str,
        text: str,
    ) -> None:
        text_embedding = create_embedding(text)
        data = ({
            "id": ad_id,
            "project_name": project_name,
            "embeddings": text_embedding,
        })
        return data
