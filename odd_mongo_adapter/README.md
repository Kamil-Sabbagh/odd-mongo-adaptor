## ODD Mongo adapter

ODD Mongo adapter is used for extracting schemas from MongoDB. This adapter is implementation of pull model (see more https://github.com/opendatadiscovery/opendatadiscovery-specification/blob/main/specification/specification.md#discovery-models). By default application gather data from MongoDB every minute, put it inside local cache and then ready to give it away by /entities API.

This service based on Python Flask and Connexion frameworks with APScheduler.

#### Data entities:
| Entity type | Entity source |
|:----------------:|:---------:|
|Dataset|Collections, Documents, Columns|


For more information about data entities see https://github.com/opendatadiscovery/opendatadiscovery-specification/blob/main/specification/specification.md#data-model-specification

## Quickstart
Application is ready to run out of the box by the docker-compose (see more https://docs.docker.com/compose/).
Strongly recommended to override next variables in docker-compose .env file:

```
environment:
      - MONGO_INITDB_DATABASE=${oddadapter}
      - MONGO_INITDB_ROOT_USERNAME=${oddadapter}
      - MONGO_INITDB_ROOT_PASSWORD=${odd-adapter-password}
```

After docker-compose run successful, application is ready to accept connection on port :8080.
For more information about variables see next section.

## Environment
Adapter is ready to work out of box, but you probably will need to redefine some variables in compose .env file:

```Python
MONGO_HOST=odd-mongo-db #Host of your MongoDB database.
MONGO_DATABASE=oddadapter #Name of your MongoDB database.
MONGO_USER=oddadapter #Username of your MongoDB database.
MONGO_PASSWORD=odd-adapter-mongo #Password of your MongoDB database.

```

## Requirements
- Python 3.8
- pymongo = 4.0.1
- dnspython= 2.2.0
