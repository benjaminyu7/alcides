#!/usr/bin/env python
import os

from flask import ( Flask, request, jsonify )
from orchestrator.message_orchestrator import MessageOrchestrator
from database.message_repository import MessageRepository
from injection.bindings import Bindings
from pinject import new_object_graph

app = Flask(__name__)
FLASK_ROUTING = "/flask"
    
obj_graph = new_object_graph(binding_specs=[Bindings()])
message_orchestrator = obj_graph.provide(MessageOrchestrator)

@app.route(FLASK_ROUTING + '/addMessage/<sender>/<recipient>', methods=['POST'])
def add_item(sender, recipient):
    didSend = message_orchestrator.add_message(sender, recipient, request.json['message'])
    if(didSend):
        return jsonify({'status':'OK'}), 200
    else:
        return jsonify({'status':'ERROR'}), 400

@app.route(FLASK_ROUTING + '/getMessages/<sender>/<recipient>', methods=['GET'])
def get_item(sender, recipient):
    value = message_orchestrator.get_messages(sender, recipient);
    app.logger.info(value)
    return value['message']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)
