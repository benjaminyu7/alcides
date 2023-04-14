#!/usr/bin/env python
import os
import sys
sys.path.append('../src')

from flask import ( Flask, request, jsonify )
from src.orchestrator.message_orchestrator import MessageOrchestrator
from src.database.message_repository import MessageRepository
from src.injection.bindings import Bindings
from pinject import new_object_graph

app = Flask(__name__)
FLASK_ROUTING = "/flask"
    
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

@app.route(FLASK_ROUTING + '/getMessages/<sender>/<recipient>', methods=['GET'])
def get_messages(sender, recipient):
    app.logger.debug('get_messages request: Sender: ' + sender + ', Recipient: ' + recipient)
    value = message_orchestrator.get_messages(sender, recipient)
    app.logger.debug('get_messages response: ' + str(value))
    if value != None:
        return jsonify({'message': value['message']})
    else:
        return jsonify({'status':'OK'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
