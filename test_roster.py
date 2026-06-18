import unittest
from K25_CNTT8_Python_Session20_Ex04 import calculate_actual_pay


class TestCalculateActualPay(unittest.TestCase):

    # Test Case 1: Active nhận 100% lương
    def test_active_player(self):
        player = {"salary": 5000, "status": "Active"}

        self.assertEqual(calculate_actual_pay(player), 5000)

    # Test Case 2: Benched nhận 50% lương
    def test_benched_player(self):
        player = {"salary": 6000, "status": "Benched"}

        self.assertEqual(calculate_actual_pay(player), 3000)


if __name__ == "__main__":
    unittest.main()
