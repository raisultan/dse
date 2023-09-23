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

## Importing Data Into Vector Database
### Export from Django as JSON
```shell
python manage.py dumpdata adverts.Advert --output=bazaraki-master_ads.json
```

### Importing Ads From JSON Dump
```shell
make import-ads DUMP_PATH="$(pwd)/dumps/bazaraki-master_ads.json" PROJECT_NAME="bazaraki-master"
```
