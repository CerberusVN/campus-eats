import unittest
from ord.service import create_order


class TestOrderWithRealMenu(unittest.TestCase):
    def test_sold_out_item_is_rejected(self):  # BR-ORD-01 with real MENU data
        with self.assertRaises(ValueError):
            create_order(2, 1)

    def test_total_uses_real_menu_price(self):
        self.assertEqual(create_order(3, 2)["total"], 10000)
