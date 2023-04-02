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

    def get_messages(self, sender: str, recipient: str):
        value = self.message_repository.get_messages(sender, recipient)
        print(value)
        return value
        
