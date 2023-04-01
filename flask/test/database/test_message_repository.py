import unittest
from unittest.mock import MagicMock
from src.database.message_repository import MessageRepository

class TestmessageRepository(unittest.TestCase):

    ANY_SENDER = "anySender"
    ANY_RECIPIENT = "anyRecipient"
    ANY_MESSAGE = "anyMessage"
    ANY_ID = "anyId"

    def test_add_message(self):
        mock_message_gateway = MagicMock()
        mock_message_gateway.add_message.return_value = {"id": self.ANY_ID}
        message_repository = MessageRepository(mock_message_gateway)
        message_repository.create_message(self.ANY_SENDER, self.ANY_RECIPIENT, self.ANY_MESSAGE)

        message_repository.get_messages(self.ANY_SENDER, self.ANY_RECIPIENT)

if __name__ == '__main__':
    unittest.main()