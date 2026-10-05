# Campus Eats — Specification (excerpt)

## 3. Functional requirements
- FR-ACC-001  Register a user with a unique email.
- FR-MENU-002 Stock of a menu item decreases when an order is confirmed.
- FR-MENU-004 Sold-out items are not shown on the menu.
- FR-ORD-003  Create an order for one item and a quantity.

## 4. Business rules
- BR-ORD-01  An order is accepted only when stock >= quantity; otherwise it is rejected.

## 5.1 Input/Output contract MENU -> ORD
menu.service.get_item(item_id) returns
    {"id": int, "name": str, "price": int (VND), "stock": int}
The field that carries the item price is "price".

## 10. Open questions
- (none yet)
