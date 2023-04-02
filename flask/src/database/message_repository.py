from pinject import copy_args_to_public_fields
from src.constants.database_constants import ( DATABASE_NAME, MESSAGE_COLLECTION_NAME, MESSAGE_CONTENT, MESSAGE_RECIPIENT, MESSAGE_SENDER)

class MessageRepository:

    @copy_args_to_public_fields
    def __init__(self, database_gateway):
        pass

    def create_message(self, sender: str, recipient: str, message: str):
        self.database_gateway.insert(DATABASE_NAME, MESSAGE_COLLECTION_NAME, {MESSAGE_SENDER: sender, MESSAGE_RECIPIENT: recipient, MESSAGE_CONTENT: message})

    def get_messages(self, sender: str, recipient: str):
        return self.database_gateway.get(DATABASE_NAME, MESSAGE_COLLECTION_NAME, {MESSAGE_SENDER: sender, MESSAGE_RECIPIENT: recipient})