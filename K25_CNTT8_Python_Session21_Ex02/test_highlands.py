"""
Unit tests for Highlands POS.
"""

import unittest

from pos_logic import HighlandsPOS, InvalidQuantityError


class TestHighlandsPOS(unittest.TestCase):
    """
    Test Highlands POS.
    """

    def setUp(self):
        """
        Create POS object.
        """

        self.pos_system = HighlandsPOS()

    def test_calculate_total(self):
        """
        Test calculate_total().
        """

        self.pos_system.current_order = [
            {"code": "P1", "quantity": 2},
            {"code": "F1", "quantity": 1},
        ]

        result = self.pos_system.calculate_total()

        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        """
        Test InvalidQuantityError.
        """

        with self.assertRaises(InvalidQuantityError):

            self.pos_system.add_to_order("P1", -1)


if __name__ == "__main__":
    unittest.main()
