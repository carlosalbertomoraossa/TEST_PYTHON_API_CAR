from abc import ABC, abstractmethod

class IItemService(ABC):

    @abstractmethod
    def get_items(self) -> list:
        pass

    @abstractmethod
    def get_item(self, item_id) -> dict:
        pass