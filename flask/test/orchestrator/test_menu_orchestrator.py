import unittest
from unittest.mock import MagicMock
from src.orchestrator.menu_orchestrator import MenuOrchestrator

class TestMenuOrchestrator(unittest.TestCase):

    def test_add_menu_item(self):
        mock_menu_repository = MagicMock()
        mock_menu_repository.add_menu_item.return_value = False
        menu_orchestrator = MenuOrchestrator(mock_menu_repository)
        self.assertTrue(menu_orchestrator.add_menu_item({"name": "banana"}))

if __name__ == '__main__':
    unittest.main()