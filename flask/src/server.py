#!/usr/bin/env python
import os
import sys
sys.path.append('../src')

from pinject import new_object_graph
from flask import ( Flask )
from flask_login import LoginManager

from src.database.message_repository import MessageRepository
from src.database.account_repository import AccountRepository
from src.injection.bindings import Bindings
from src.orchestrator.account_orchestrator import AccountOrchestrator
from src.orchestrator.message_orchestrator import MessageOrchestrator
from src.blueprint.account_blueprint import account_blueprint
from src.blueprint.message_blueprint import message_blueprint

app = Flask(__name__)
# Remove the key from the repo
app.secret_key = 'supersecretkey'
app.register_blueprint(account_blueprint)
app.register_blueprint(message_blueprint)
    
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.unauthorized_handler
def unauthorized_handler():
    # TODO: integrate with the frontend with a useful code
    return 'Unauthorized message', 401

obj_graph = new_object_graph(binding_specs=[Bindings()])
account_orchestrator = obj_graph.provide(AccountOrchestrator)

@login_manager.user_loader
def load_user(user_id):
    app.logger.debug('load_user: ' + user_id)
    return account_orchestrator.load_user(user_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)