class Item:

    def __init__(self, id, name, description):
        self.id: int = id
        self.name: str = name
        self.description: str = description

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
    
    @classmethod
    def from_dict(cls, data) -> any:
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"]
        )