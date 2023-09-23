start-app:
	@echo "Starting app..."
	python3 -m app.service

start-milvus:
	@echo "Starting Milvus..."
	docker-compose -f milvus-docker-compose.yaml up -d

stop-milvus:
	@echo "Stopping Milvus..."
	docker-compose -f milvus-docker-compose.yaml down

check-milvus-port:
	@echo "Checking Milvus port..."
	docker port milvus-standalone 19530/tcp

create-collection-ads:
	@echo "Creating collection Ads..."
	export PYTHONPATH="$(pwd)/" && python3 app/scripts/create_collection_ads.py
	@echo "Ads collection created successfully!"
