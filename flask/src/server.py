#!/usr/bin/env python
import os
import sys
sys.path.append('../src')

from pinject import new_object_graph
from flask import ( Flask, request, jsonify )

from src.constants.database_constants import ( MESSAGES )
from src.constants.flask_constants import ( FLASK_ROUTING )
from src.database.message_repository import MessageRepository
from src.database.account_repository import AccountRepository
from src.injection.bindings import Bindings
from src.orchestrator.message_orchestrator import MessageOrchestrator
from src.blueprint.account_blueprint import account_blueprint

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.register_blueprint(account_blueprint)
    
obj_graph = new_object_graph(binding_specs=[Bindings()])
message_orchestrator = obj_graph.provide(MessageOrchestrator)

@app.route(FLASK_ROUTING + '/addMessage/<sender>/<recipient>', methods=['POST'])
def add_message(sender, recipient):
    app.logger.debug('add_message request: Sender: ' + sender + ', Recipient: ' + recipient + ', Request: ' + str(request))
    didSend = message_orchestrator.add_message(sender, recipient, request.json['message'])
    if(didSend):
        return jsonify({'status':'OK'}), 200
    else:
        return jsonify({'status':'ERROR'}), 400

@app.route(FLASK_ROUTING + '/getMessages/<recipient>', methods=['GET'])
def get_messages(recipient):
    app.logger.debug('get_messages request: Recipient: ' + recipient)
    value = message_orchestrator.get_messages(recipient)
    app.logger.debug('get_messages response: ' + str(value))
    if value != None:
        return jsonify({MESSAGES: value[MESSAGES]})
    else:
        return jsonify({'status':'OK'}), 200

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from pymongo import MongoClient
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()
login_manager.init_app(app)

# Connect to MongoDB
client = MongoClient('mongo:27017')
db = client['user_database']
users = db['users']

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, user_data):
        self.id = user_data['_id']
        self.email = user_data['email']
        self.password = user_data['password']

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized stuff', 401

@login_manager.user_loader
def load_user(user_id):
    user_data = users.find_one({"_id": ObjectId(user_id)})
    app.logger.debug("user_data: "+ user_id + str(user_data))
    return User(user_data) if user_data else None

@app.route(FLASK_ROUTING + '/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_data = users.find_one({"email": email})

        app.logger.debug("login user_data: " + str(user_data))
        if user_data and check_password_hash(user_data['password'], password):
            user = User(user_data)
            login_user(user)
            return 'Login Successful'
        else:
            return('Invalid email or password')

    return render_template('login.html')

@app.route(FLASK_ROUTING + '/register', methods=['POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if users.find_one({"email": email}):
            return('Email address already in use')
        else:
            password_hash = generate_password_hash(password)
            users.insert_one({"email": email, "password": password_hash})
            return('Registration successful, please log in')

@app.route(FLASK_ROUTING + '/logout')
@login_required
def logout():
    logout_user()
    return "Logged out"

@app.route(FLASK_ROUTING + '/home')
@login_required
def home():
    return "home page"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
