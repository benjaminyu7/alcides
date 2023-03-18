from pinject import copy_args_to_internal_fields

class MenuRepository:

    @copy_args_to_internal_fields
    def __init__(self, database_gateway):
        pass

    def create_item(self, item):
        self.database_gateway.insert("restaurant", "menuItems", item)