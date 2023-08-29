from app.service.item_service import ItemService


class ItemController:

    def __init__(self):
        self.item_service: ItemService = ItemService()

    def get_items(self)-> list:
        return self.item_service.get_items()

    def get_item(self, item_id) -> dict:
        return self.item_service.get_item(item_id)
