import logging
import pymongo
from odd_models.models import DataEntity
from pymongo import MongoClient
from typing import List, Dict
from odd_mongo_adapter.mappers.schemas import map_collection
from odd_mongo_adapter.mongo_generator import MongoGenerator


class MongoAdapter:

    def __init__(self, config) -> None:
        self.__host = config['ODD_HOST']
        self.__database = config['ODD_DATABASE']
        self.__user = config['ODD_USER']
        self.__password = config['ODD_PASSWORD']
        self.__oddrn_generator = MongoGenerator(host_settings=f"{self.__host}", databases=self.__database)

    def get_data_source_oddrn(self) -> str:
        return self.__oddrn_generator.get_data_source_oddrn()

    def get_schema_entities(self) -> List[DataEntity]:
        """
        This function will convert a dictionary schema into
        an odd list of data entities
        """
        try:
            self.connect()
            schemas = self.retrive_scheams()

            return map_collection(self.__oddrn_generator, schemas, self.__database)
        except Exception as e:
            logging.error('Failed to load metadata for tables')
            logging.exception(e)
        finally:
            self.disconnect()
        return []

    def retrive_scheams(self) :
        """
        This function is used to collect the schemas of a MongoDB,
        it will go return one schema for each collection. For each
        collection, the schema returned is dictionary contains the
        combination of all the types used across the first N document.
        """
        try:
            collections = self.__connection.list_collection_names()
            schemas = []
            max_number_of_iterations = 10
            for collection_name in collections:
                iterations = 1
                collection = self.__connection[collection_name]
                results = collection.find({})
                schema = {"title": collection_name, "required": [], "properties": {}}
                for res in results :
                    if iterations > max_number_of_iterations:
                        break
                    for key, value in res.items():
                        if key not in schema['required']:
                            schema["required"].append(key)
                            schema["properties"][key] = {"bsonType": type(value).__name__}
                    iterations += 1
                schemas.append(schema)


            return schemas

        except Exception as e:
            print("something wrong with the schemas!")


    def connect(self):
        try:
            self.__cluster = MongoClient(
                f"mongodb+srv://{self.__user}:{self.__password}{self.__host}")

            self.__connection = self.__cluster[self.__database]
        except pymongo.errors.ConnectionFailure as err:
            logging.error(err)
            raise DBException('Database error')

    def disconnect(self):
        try:
            if self.__cluster:
                self.__cluster.close()
        except Exception:
            pass


class DBException(Exception):
    pass




