import unittest
from unittest.mock import MagicMock
from src.database.mongo_gateway import MongoGateway

class TestMenuRepository(unittest.TestCase):

    def test_add_menu_item(self):
        mock_mongo_client = MagicMock()
        mock_mongo_client.insert_one.return_value = False
        mongo_gateway = MongoGateway(mock_mongo_client)
        mongo_gateway.insert("any_databaes", "any_collection", {"name": "banana"})

if __name__ == '__main__':
    unittest.main()