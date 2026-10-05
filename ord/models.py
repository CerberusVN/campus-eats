from dataclasses import dataclass


@dataclass
class Order:
    item_id: int
    quantity: int
    total: int
