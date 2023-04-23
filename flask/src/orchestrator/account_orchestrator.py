from pinject import copy_args_to_public_fields

class AccountOrchestrator:

    @copy_args_to_public_fields
    def __init__(self, account_repository):
        pass

    def add_user(self, username:str):
        """TODO: Make usernames unique"""
        if(username != None and username != ""):
            self.account_repository.create_user(username)
            return True
        else:
            return False