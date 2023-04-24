from flask import ( Blueprint, request, jsonify, current_app )
from pinject import new_object_graph
from flask import request
from flask_login import logout_user, current_user, login_required

from src.orchestrator.account_orchestrator import AccountOrchestrator
from src.database.account_repository import AccountRepository
from src.constants.flask_constants import ( FLASK_ROUTING )
from src.constants.account_constants import ( EMAIL, PASSWORD )
from src.injection.bindings import Bindings

account_blueprint = Blueprint('login', __name__)

obj_graph = new_object_graph(binding_specs=[Bindings()])
account_orchestrator = obj_graph.provide(AccountOrchestrator)

@account_blueprint.route(FLASK_ROUTING + '/register', methods=['POST'])
def register():
    if current_user.is_authenticated:
        # TODO: integrate with the frontend with a useful code
        return "Already Logged in"

    email = request.form[EMAIL]
    password = request.form[PASSWORD]
    return account_orchestrator.register(email, password)

@account_blueprint.route(FLASK_ROUTING + '/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        # TODO: integrate with the frontend with a useful code
        return "Already Logged in"
    
    email = request.form[EMAIL]
    password = request.form[PASSWORD]
    current_app.logger.debug("login email: " + str(email))
    return account_orchestrator.login(email, password)
    
@account_blueprint.route(FLASK_ROUTING + '/logout')
@login_required
def logout():
    logout_user()
    # TODO: integrate with the frontend with a useful code
    return "Logged out"

@account_blueprint.route(FLASK_ROUTING + '/home')
@login_required
def home():
    # TODO: integrate with the frontend with a useful code
    return "home page"
