import unittest
from unittest.mock import MagicMock
from src.database.menu_repository import MenuRepository

class TestMenuRepository(unittest.TestCase):

    def test_add_menu_item(self):
        mock_menu_gateway = MagicMock()
        mock_menu_gateway.add_menu_item.return_value = False
        menu_repository = MenuRepository(mock_menu_gateway)
        menu_repository.create_item({"name": "banana"})

if __name__ == '__main__':
    unittest.main()