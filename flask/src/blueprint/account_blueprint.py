from flask import ( Blueprint, request, jsonify, current_app )
from pinject import new_object_graph

from src.orchestrator.account_orchestrator import AccountOrchestrator
from src.database.account_repository import AccountRepository
from src.constants.flask_constants import ( FLASK_ROUTING )
from src.injection.bindings import Bindings


account_blueprint = Blueprint('login', __name__)

obj_graph = new_object_graph(binding_specs=[Bindings()])
account_orchestrator = obj_graph.provide(AccountOrchestrator)

@account_blueprint.route(FLASK_ROUTING + '/addUser', methods=['POST'])
def add_user():
    """
    'POST'
    {
        username: 'username'
    }
    TODO: add addtional account information like password, email, etc
    """
    current_app.logger.debug('addUser request: ' + str(request))
    did_create = account_orchestrator.add_user(request.json['username'])
    if(did_create):
        return jsonify({'status':'OK'}), 200
    else:
        return jsonify({'status':'ERROR'}), 400
