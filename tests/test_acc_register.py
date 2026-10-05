import unittest
from acc.service import register, USERS


class TestRegister(unittest.TestCase):
    def setUp(self):
        USERS.clear()

    def test_register_new_email(self):
        self.assertEqual(register("a@uni.vn"), "a@uni.vn")

    def test_reject_duplicate_email(self):
        register("a@uni.vn")
        with self.assertRaises(ValueError):
            register("a@uni.vn")
