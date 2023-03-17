from pymongo import MongoClient

class MongoGateway:

    def __init__(self, client_name):
        self.client = MongoClient(client_name)

    def insert(self, database, collection, dictionary):
        database = self.client[database]
        collection = database[collection]
        collection.insert_one(dictionary)
