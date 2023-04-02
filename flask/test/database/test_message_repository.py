import unittest
from unittest.mock import ( MagicMock )
from src.database.message_repository import MessageRepository
from src.constants.database_constants import ( DATABASE_NAME, MESSAGE_COLLECTION_NAME, MESSAGE_CONTENT, MESSAGE_RECIPIENT, MESSAGE_SENDER)

class TestMessageRepository(unittest.TestCase):

    ANY_SENDER = "anySender"
    ANY_RECIPIENT = "anyRecipient"
    ANY_MESSAGE = "anyMessage"
    ANY_ID = "anyId"
    ANY_GET_MESSAGES_RESPONSE = {MESSAGE_SENDER: ANY_SENDER, MESSAGE_RECIPIENT: ANY_RECIPIENT, MESSAGE_CONTENT: ANY_MESSAGE}

    def test_add_message(self):
        mock_message_gateway = MagicMock()
        mock_message_gateway.insert.return_value = {"id": self.ANY_ID}
        message_repository = MessageRepository(mock_message_gateway)
        message_repository.create_message(self.ANY_SENDER, self.ANY_RECIPIENT, self.ANY_MESSAGE)

    def test_get_message(self):
        mock_message_gateway = MagicMock()
        #TODO: mock the insert as well
        def get_messages_side_effect(database: str, collection: str, dictionary: dict):
            if (database == DATABASE_NAME and collection == MESSAGE_COLLECTION_NAME and dictionary == {MESSAGE_SENDER: self.ANY_SENDER, MESSAGE_RECIPIENT: self.ANY_RECIPIENT}):
                return self.ANY_GET_MESSAGES_RESPONSE
            else:
                None
        mock_message_gateway.get = MagicMock(side_effect=get_messages_side_effect)
        message_repository = MessageRepository(mock_message_gateway)

        message = message_repository.get_messages(self.ANY_SENDER, self.ANY_RECIPIENT)
        self.assertEqual(message, self.ANY_GET_MESSAGES_RESPONSE)

if __name__ == '__main__':
    unittest.main()