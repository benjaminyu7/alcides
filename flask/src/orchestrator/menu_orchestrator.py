class MenuOrchestrator:
    def __init__(self, menu_repository):
        self.menu_repository = menu_repository

    def add_menu_item(self, item):
        self.menu_repository.create_item(item)
        return True
