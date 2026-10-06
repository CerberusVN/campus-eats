import unittest
from menu.service import MENU, decrease_stock
from ord.service import create_order


class TestMenuStock(unittest.TestCase):
    def test_decrease_stock(self):
        before = MENU[1]["stock"]
        decrease_stock(1, 3)
        self.assertEqual(MENU[1]["stock"], before - 3)
        MENU[1]["stock"] = before

    def test_order_total_uses_menu_price(self):
        self.assertEqual(create_order(1, 2)["total"], 90000)
