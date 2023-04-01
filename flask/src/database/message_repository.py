from pinject import copy_args_to_public_fields

class MessageRepository:

    @copy_args_to_public_fields
    def __init__(self, database_gateway):
        pass

    def create_message(self, sender, recipient, message):
        self.database_gateway.insert('alcides', 'messages', {'sender': sender, 'recipient': recipient, 'message': message})

    def get_messages(self, sender, recipient):
        return self.database_gateway.get('alcides', 'messages', {'sender': sender, 'recipient': recipient})