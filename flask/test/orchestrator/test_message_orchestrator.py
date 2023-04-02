import unittest
from unittest.mock import MagicMock
from src.orchestrator.message_orchestrator import MessageOrchestrator

class TestMenuOrchestrator(unittest.TestCase):
    ANY_SENDER = 'anySender'
    ANY_RECIPIENT = 'anyRecipient'
    EMPTY_MESSAGE = ''

    def test_add_message_empty_message_return_false(self):
        mock_message_repository = MagicMock()
        message_orchestator = MessageOrchestrator(mock_message_repository)
        self.assertFalse(message_orchestator.add_message(self.ANY_SENDER, self.ANY_RECIPIENT, self.EMPTY_MESSAGE))

    def test_add_message_none_message_return_false(self):
        mock_message_repository = MagicMock()
        message_orchestator = MessageOrchestrator(mock_message_repository)
        self.assertFalse(message_orchestator.add_message(self.ANY_SENDER, self.ANY_RECIPIENT, None))

if __name__ == '__main__':
    unittest.main()