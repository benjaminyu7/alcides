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
