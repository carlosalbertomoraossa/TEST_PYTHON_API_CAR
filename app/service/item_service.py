from app.model.item import Item
from app.service.interface.item_interface import IItemService


class ItemService(IItemService):

    def __init__(self):
        first_item: Item = Item(1, "Item 1", "Description for Item 1")
        second_item: Item = Item(2, "Item 2", "Description for Item 2")
        third_item: Item = Item(3, "Item 3", "Description for Item 3")

        fourth_item: Item = Item.from_dict(
            {"id": 4, "name": "Item 4", "description": "Description for Item 4"})

        self.items = [first_item.to_dict(), second_item.to_dict(),
                      third_item.to_dict(), fourth_item.to_dict()]

    def get_items(self) -> list:
        return self.items

    def get_item(self, item_id) -> dict:
        item: Item = next(
            (item for item in self.items if item["id"] == item_id), None)
        if item:
            return item
        else:
            return {}