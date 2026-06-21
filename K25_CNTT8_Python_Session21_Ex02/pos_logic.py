"""
Business logic for Highlands Mini POS.
"""

import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000},
}


class ItemNotFoundError(Exception):
    """
    Exception for invalid drink code.
    """


class InvalidQuantityError(Exception):
    """
    Exception for invalid quantity.
    """


class HighlandsPOS:
    """
    Highlands POS system.
    """

    def __init__(self):
        """
        Initialize empty order.
        """
        self.current_order = []

    def add_to_order(self, drink_code, quantity):
        """
        Add drink to current order.

        Args:
            drink_code (str): Drink code.
            quantity (int): Quantity.
        """

        drink_code = drink_code.strip().upper()

        if drink_code not in DRINK_MENU:
            logging.warning("ItemNotFoundError - Code: %s", drink_code)
            raise ItemNotFoundError

        if quantity <= 0:
            logging.warning("InvalidQuantityError - Quantity: %d", quantity)
            raise InvalidQuantityError

        self.current_order.append({"code": drink_code, "quantity": quantity})

        logging.info("Added %d of %s to order", quantity, drink_code)

    def calculate_total(self):
        """
        Calculate total amount.

        Returns:
            int: Total amount.
        """

        total = 0

        for item in self.current_order:
            code = item["code"]
            quantity = item["quantity"]

            total += DRINK_MENU[code]["price"] * quantity

        return total

    def clear_order(self):
        """
        Clear current order.
        """

        self.current_order.clear()
