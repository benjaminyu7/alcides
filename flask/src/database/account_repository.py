from bson import ObjectId
from pinject import copy_args_to_public_fields
from src.constants.database_constants import ( DATABASE_NAME, ACCOUNT_COLLECTION_NAME, USERNAME, PASSWORD, DOCUMENT_ID)
from src.model.user_model import User

class AccountRepository:

    @copy_args_to_public_fields
    def __init__(self, database_gateway):
        pass

    def create_user(self, username:str):
        self.database_gateway.insert(DATABASE_NAME, ACCOUNT_COLLECTION_NAME, {USERNAME: username})

    def find_user_with_email(self, email:str):
        """
        returns User {
            'email': 'any_email'
            'password': 'hashed-password'
        }
        """
        user_data = self.database_gateway.get(DATABASE_NAME, ACCOUNT_COLLECTION_NAME, {USERNAME: email})
        if user_data:
            return User(user_data)
        else:
            return False

    def find_user_with_id(self, user_id:str):
        user_data = self.database_gateway.get(DATABASE_NAME, ACCOUNT_COLLECTION_NAME, {DOCUMENT_ID: ObjectId(user_id)})
        return User(user_data) if user_data else None
    
    def create_new_user(self, email:str, password:str):
        self.database_gateway.insert(DATABASE_NAME, ACCOUNT_COLLECTION_NAME, {USERNAME: email, PASSWORD: password})