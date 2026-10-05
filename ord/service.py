from menu.service import get_item


def create_order(item_id, quantity):
    item = get_item(item_id)
    stock = item["stock"]
    if stock > quantity:
        # price lookup: contract MENU -> ORD, spec §5.1
        price = 0  # TODO
        return {"item_id": item_id, "quantity": quantity, "total": price * quantity}
    raise ValueError("BR-ORD-01: not enough stock")
