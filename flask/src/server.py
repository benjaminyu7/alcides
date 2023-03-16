#!/usr/bin/env python
import os

from flask import Flask
from orchestrator.menu_orchestrator import MenuOrchestrator
from database.menu_repository import MenuRepository
from database.mongo_gateway import MongoGateway

menu_orchestrator = MenuOrchestrator(MenuRepository(MongoGateway("mongo:27017")))

app = Flask(__name__)

@app.route('/addItem')
def addItem():
    return menu_orchestrator.add_menu_item({"name": "banana"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)

