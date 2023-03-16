class MenuRepository:

    def __init__(self, database_gateway):
        self.database_gateway = database_gateway

    def create_item(self, item):
        self.database_gateway.insert("restaurant", "menuItems", item)