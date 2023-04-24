from pinject import copy_args_to_public_fields
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

from src.database.account_repository import AccountRepository

class AccountOrchestrator:

    @copy_args_to_public_fields
    def __init__(self, account_repository:AccountRepository):
        pass

    def login(self, email:str, password: str):
        user_data = self.account_repository.find_user_with_email(email)

        if user_data and check_password_hash(user_data.password, password):
            login_user(user_data)
            return 'Login Successful'
        else:
            return('Invalid email or password')
    
    def register(self, email:str, password:str):
        if self.account_repository.find_user_with_email(email):
            return('Email address already in use')
        else:
            password_hash = generate_password_hash(password)
            self.account_repository.create_new_user(email, password_hash)
            return('Registration successful, please log in')
    
    def load_user(self, id:str):
        return self.account_repository.find_user_with_id(id)