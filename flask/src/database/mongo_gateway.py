from pymongo import MongoClient
from pinject import copy_args_to_public_fields

class MongoGateway:

    @copy_args_to_public_fields
    def __init__(self, mongo_client):
        pass

    def insert(self, database, collection, dictionary):
        database = self.mongo_client[database]
        collection = database[collection]
        collection.insert_one(dictionary)

    def get(self, database, collection, dictionary):
        database = self.mongo_client[database]
        collection = database[collection]
        return collection.find_one(dictionary)

    def create_or_update_list(self, database, collection, query, listElement):
        database = self.mongo_client[database]
        collection = database[collection]
        collection.update_one(query, listElement, upsert=True)