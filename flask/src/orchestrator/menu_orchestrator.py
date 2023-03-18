from pinject import copy_args_to_internal_fields

class MenuOrchestrator:

    @copy_args_to_internal_fields
    def __init__(self, menu_repository):
        pass

    def add_menu_item(self, item):
        self.menu_repository.create_item(item)
        return True
