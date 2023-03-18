from pymongo import MongoClient
from pinject import copy_args_to_internal_fields

class MongoGateway:

    @copy_args_to_internal_fields
    def __init__(self, mongo_client):
        pass

    def insert(self, database, collection, dictionary):
        database = self.client[database]
        collection = database[collection]
        collection.insert_one(dictionary)