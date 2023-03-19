from pinject import BindingSpec
from pymongo import MongoClient
from flask import Flask
from database.mongo_gateway import MongoGateway

class Bindings(BindingSpec):

    def provide_mongo_client(self):
        return MongoClient("mongo:27017")

    def configure(self, bind):
        bind('database_gateway', to_class=MongoGateway)