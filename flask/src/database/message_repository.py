from pinject import copy_args_to_public_fields
from src.constants.database_constants import ( DATABASE_NAME, MESSAGE_COLLECTION_NAME, MESSAGES, MESSAGE_CONTENT, MESSAGE_RECIPIENT, MESSAGE_SENDER)

class MessageRepository:

    @copy_args_to_public_fields
    def __init__(self, database_gateway):
        pass

    def create_message(self, sender: str, recipient: str, message: str):
        self.database_gateway.create_or_update_list(DATABASE_NAME, MESSAGE_COLLECTION_NAME, 
                                                    {MESSAGE_RECIPIENT: recipient}, 
                                                    {MESSAGES: {MESSAGE_SENDER: sender, MESSAGE_CONTENT: message}})

    # TODO: Get a slice of the messages
    def get_messages(self, recipient: str):
        """
        returns {
            "messages": [
                {
                    "message_content": "any message content",
                    "sender": "anySender"
                }
            ]
        }
        """
        return self.database_gateway.get(DATABASE_NAME, MESSAGE_COLLECTION_NAME, {MESSAGE_RECIPIENT: recipient})

    def get_messages_slice(self, recipient: str, index: int, number_of_messages: int):
        return self.database_gateway.get_elements_from_list(DATABASE_NAME, MESSAGE_COLLECTION_NAME, 
                                                    {MESSAGE_RECIPIENT: recipient},
                                                    MESSAGES, index, number_of_messages)