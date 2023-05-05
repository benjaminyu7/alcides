from pymongo import MongoClient
from pinject import copy_args_to_public_fields

class MongoGateway:

    @copy_args_to_public_fields
    def __init__(self, mongo_client:MongoClient):
        pass

    def insert(self, database:str, collection:str, dictionary:dict):
        database = self.mongo_client[database]
        collection = database[collection]
        collection.insert_one(dictionary)

    def get(self, database: str, collection: str, dictionary:dict):
        database = self.mongo_client[database]
        collection = database[collection]
        return collection.find_one(dictionary)

    def create_or_update_list(self, database: str, collection: str, query: dict, pushListElementQuery: dict):
        database = self.mongo_client[database]
        collection = database[collection]
        collection.update_one(query, {"$push":pushListElementQuery}, upsert=True)

    def get_elements_from_list(self, database: str, 
                               collection: str, 
                               query: dict, 
                               element_member:str, 
                               index: int, 
                               number_of_elements: int):
        """
        Retrieves a slice of elements from a list within a document in a MongoDB collection.

        Args:
            database (str): The name of the database.
            collection (str): The name of the collection.
            query (dict): A MongoDB query to match the desired document.
            element_member (str): The name of the list field in the document.
            index (int): The starting index of the slice.
            number_of_elements (int): The number of elements to retrieve in the slice.

        Returns:
            dict: A dictionary representing the matched document with only the specified slice of elements
                in the list field. If no document is found, returns None.
        """
        database = self.mongo_client[database]
        collection = database[collection]
        return collection.find_one(query, {element_member: {'$slice': [index, number_of_elements]}})
