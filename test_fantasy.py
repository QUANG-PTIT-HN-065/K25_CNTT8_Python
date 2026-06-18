import unittest
from K25_CNTT8_Python_Session20_Ex05 import calc_actual_withdrawal


class TestFantasy(unittest.TestCase):

    # Test Case 1
    def test_withdraw_100(self):
        self.assertEqual(
            calc_actual_withdrawal(100),
            90.0
        )

    # Test Case 2
    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            calc_actual_withdrawal(-100)


if __name__ == "__main__":
    unittest.main()