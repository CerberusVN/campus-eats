MENU = {
    1: {"id": 1, "name": "Pho bo", "price": 45000, "stock": 10},
    2: {"id": 2, "name": "Banh mi", "price": 25000, "stock": 0},
    3: {"id": 3, "name": "Tra da", "price": 5000, "stock": 2},
}


def get_item(item_id):
    item = MENU[item_id]
    if item["stock"] == 0:
        raise KeyError(item_id)  # FR-MENU-004: hide sold-out items
    return item


def decrease_stock(item_id, quantity):
    """FR-MENU-002: called when an order is confirmed."""
    MENU[item_id]["stock"] -= quantity
