import unittest
from unittest.mock import MagicMock
from src.database.mongo_gateway import MongoGateway

class TestMenuRepository(unittest.TestCase):

    def test_add_menu_item(self):
        mock_mongo_client = MagicMock()
        mock_mongo_client.update_one.return_value = False
        mongo_gateway = MongoGateway(mock_mongo_client)
        mongo_gateway.create_or_update_list("any_database", "any_collection", {"name": "banana"}, {"messages": ["message"]})

if __name__ == '__main__':
    unittest.main()