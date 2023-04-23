#!/usr/bin/env python
import os
import sys
sys.path.append('../src')

from pinject import new_object_graph
from flask import ( Flask, request, jsonify )
from flask_login import LoginManager

from src.constants.database_constants import ( MESSAGES )
from src.constants.flask_constants import ( FLASK_ROUTING )
from src.database.message_repository import MessageRepository
from src.database.account_repository import AccountRepository
from src.injection.bindings import Bindings
from src.orchestrator.account_orchestrator import AccountOrchestrator
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

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized stuff', 401

account_orchestrator = obj_graph.provide(AccountOrchestrator)

@login_manager.user_loader
def load_user(user_id):
    app.logger.debug('load_user: ' + user_id)
    return account_orchestrator.load_user(user_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)