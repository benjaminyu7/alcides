from flask import ( Blueprint, request, jsonify, current_app )
from pinject import new_object_graph

from src.constants.database_constants import ( MESSAGES )
from src.constants.flask_constants import ( FLASK_ROUTING )
from src.constants.message_constants import ( MESSAGE, MESSAGE_SLICE_INDEX, NUMBER_OF_MESSAGES )
from src.injection.bindings import Bindings
from src.orchestrator.message_orchestrator import MessageOrchestrator

obj_graph = new_object_graph(binding_specs=[Bindings()])
message_orchestrator = obj_graph.provide(MessageOrchestrator)

message_blueprint = Blueprint('message', __name__)

@message_blueprint.route(FLASK_ROUTING + '/addMessage/<sender>/<recipient>', methods=['POST'])
def add_message(sender, recipient):
    current_app.logger.debug('add_message request: Sender: ' + sender + ', Recipient: ' + recipient + ', Request: ' + str(request))
    didSend = message_orchestrator.add_message(sender, recipient, request.json[MESSAGE])
    if(didSend):
        return jsonify({'status':'OK'}), 200
    else:
        return jsonify({'status':'ERROR'}), 400

@message_blueprint.route(FLASK_ROUTING + '/getMessages/<recipient>', methods=['GET'])
def get_messages(recipient):
    current_app.logger.debug('get_messages request: Recipient: ' + recipient)
    value = message_orchestrator.get_messages(recipient)
    current_app.logger.debug('get_messages response: ' + str(value))
    if value != None:
        return jsonify({MESSAGES: value[MESSAGES]})
    else:
        return jsonify({'status':'OK'}), 200

@message_blueprint.route(FLASK_ROUTING + '/getMessagesSlice/<recipient>', methods=['GET'])
def get_messages_slice(recipient):
    current_app.logger.debug('get_messages_slice request: Recipient: ' + recipient)
    value = message_orchestrator.get_messages_slice(recipient, 
                                                    int(request.args.get(MESSAGE_SLICE_INDEX)), 
                                                    int(request.args.get(NUMBER_OF_MESSAGES)))
    current_app.logger.debug('get_messages_slice response: ' + str(value))
    if value != None:
        return jsonify({MESSAGES: value[MESSAGES]})
    else:
        return jsonify({'status':'OK'}), 200