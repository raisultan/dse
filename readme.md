## Vector Database
### Start Milvus Vector Database
```shell
make start-milvus
```

### Stop Milvus
```shell
make stop-milvus
```

### Check Milvus Port
```shell
make check-milvus-port
```

### Create Collection On Empty Database
```shell
make create-collection-ads
```

## App
### Start App on :8080
```shell
make start-app
```

## Importing Ads From JSON Dump
```shell
make import-ads DUMP_PATH="$(pwd)/dumps/my_dump.json" PROJECT_NAME="my_project"
```
