from pinject import copy_args_to_public_fields

class MenuRepository:

    @copy_args_to_public_fields
    def __init__(self, database_gateway):
        pass

    def create_item(self, item):
        self.database_gateway.insert("restaurant", "menuItems", item)

    def get_item(self, item):
        return self.database_gateway.get("restaurant", "menuItems", item)