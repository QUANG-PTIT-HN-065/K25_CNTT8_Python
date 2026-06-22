import unittest
from main import calculate_energy_financials


class TestEnergy(unittest.TestCase):

    def test_empty_list(self):

        result = calculate_energy_financials([])

        self.assertEqual(result, (0.0, 0.0, 0.0))

    def test_no_discount(self):

        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 10000,
                "status": "Normal",
            }
        ]

        total_kwh, discount, money = calculate_energy_financials(devices)

        self.assertEqual(total_kwh, 10000)
        self.assertEqual(discount, 0)
        self.assertEqual(money, 30000000)

    def test_discount_3_percent(self):

        devices = [
            {
                "id": "M01",
                "location": "A",
                "old_index": 0,
                "new_index": 50000,
                "status": "Normal",
            }
        ]

        total_kwh, discount, money = calculate_energy_financials(devices)

        self.assertEqual(total_kwh, 50000)
        self.assertEqual(discount, 3)
        self.assertEqual(money, 145500000)


if __name__ == "__main__":
    unittest.main()
