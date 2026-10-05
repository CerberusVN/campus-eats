import unittest
from unittest.mock import patch
from ord.service import create_order


def fake_item(stock):
    # stub of MENU.get_item, written before MENU was finished
    return {"id": 1, "name": "Pho bo", "unit_price": 45000, "stock": stock}


class TestCreateOrder(unittest.TestCase):
    @patch("ord.service.get_item")
    def test_accept_when_stock_equals_quantity(self, get_item):
        get_item.return_value = fake_item(stock=2)  # BR-ORD-01 boundary
        self.assertEqual(create_order(1, 2)["quantity"], 2)

    @patch("ord.service.get_item")
    def test_reject_when_stock_less_than_quantity(self, get_item):
        get_item.return_value = fake_item(stock=1)
        with self.assertRaises(ValueError):
            create_order(1, 2)
