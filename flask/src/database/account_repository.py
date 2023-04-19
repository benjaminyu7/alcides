from pinject import copy_args_to_public_fields
from src.constants.database_constants import ( DATABASE_NAME, ACCOUNT_COLLECTION_NAME, USERNAME )

class AccountRepository:

    @copy_args_to_public_fields
    def __init__(self, database_gateway):
        pass

    def create_user(self, username:str):
        self.database_gateway.insert(DATABASE_NAME, ACCOUNT_COLLECTION_NAME, {USERNAME: username})