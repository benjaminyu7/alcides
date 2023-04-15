import unittest
from unittest.mock import ( MagicMock )
from src.database.message_repository import MessageRepository
from src.constants.database_constants import ( MESSAGE_CONTENT, MESSAGE_RECIPIENT, MESSAGE_SENDER)

class TestMessageRepository(unittest.TestCase):

    ANY_SENDER = "anySender"
    ANY_RECIPIENT = "anyRecipient"
    ANY_MESSAGE = "anyMessage"
    ANY_ID = "anyId"
    ANY_GET_MESSAGES_RESPONSE = {MESSAGE_SENDER: ANY_SENDER, MESSAGE_RECIPIENT: ANY_RECIPIENT, MESSAGE_CONTENT: [ANY_MESSAGE]}

    def test_add_message(self):
        mock_message_gateway = MagicMock()
        mock_message_gateway.insert.return_value = {"id": self.ANY_ID}
        message_repository = MessageRepository(mock_message_gateway)
        message_repository.create_message(self.ANY_SENDER, self.ANY_RECIPIENT, self.ANY_MESSAGE)

    #TODO: Improve mocking of DB to include sender/recipient in the search
    def test_get_message(self):
        mock_message_gateway = MagicMock()
        mockDatabase = {}
        def add_message_side_effect(database: str, collection: str, query: dict, update_operator):
            query[MESSAGE_CONTENT] = [update_operator['$push'][MESSAGE_CONTENT]]
            mockDatabase[database] = {collection:query}
        mock_message_gateway.create_or_update_list = MagicMock(side_effect=add_message_side_effect)

        def get_messages_side_effect(database: str, collection: str, query: dict):
            if (database in mockDatabase and collection in mockDatabase[database]):
                return mockDatabase[database][collection]
            else:
                None
        mock_message_gateway.get = MagicMock(side_effect=get_messages_side_effect)
        message_repository = MessageRepository(mock_message_gateway)

        message_repository.create_message(self.ANY_SENDER, self.ANY_RECIPIENT, self.ANY_MESSAGE)
        message = message_repository.get_messages(self.ANY_SENDER, self.ANY_RECIPIENT)
        self.assertEqual(message, self.ANY_GET_MESSAGES_RESPONSE)

if __name__ == '__main__':
    unittest.main()