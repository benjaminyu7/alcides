from flask_login import UserMixin

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, user_data):
        self.id = user_data['_id']
        self.email = user_data['email']
        self.password = user_data['password']