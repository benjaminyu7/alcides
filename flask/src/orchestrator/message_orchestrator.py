from pinject import copy_args_to_public_fields

class MessageOrchestrator:

    @copy_args_to_public_fields
    def __init__(self, message_repository):
        pass

    def add_message(self, sender:str , recipient:str , message:str ):
        if(message != None and message != ""):
            self.message_repository.create_message(sender, recipient, message)
            return True
        else:
            return False

    def get_messages(self, recipient: str):
        """
        returns {
            "messages": [
                {
                    "message_content": "Hello world!",
                    "sender": "anySender"
                }
            ]
        }
        """
        return self.message_repository.get_messages(recipient)
        

    def get_messages_slice(self, recipient: str, index:int, number_of_messages: int):
        return self.message_repository.get_messages_slice(recipient, index, number_of_messages)