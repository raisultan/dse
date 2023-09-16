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
