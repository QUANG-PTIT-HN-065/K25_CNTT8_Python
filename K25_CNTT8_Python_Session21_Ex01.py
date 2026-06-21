"""
MoMo Wallet Simulation
"""

import logging
import re

logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class InvalidAmountError(Exception):
    """
    Exception for invalid amount.
    """


class InsufficientBalanceError(Exception):
    """
    Exception for insufficient balance.
    """


class Wallet:
    """
    Wallet class.
    """

    def __init__(self):
        """
        Initialize wallet.
        """
        self.balance = 0

    def deposit(self, amount):
        """
        Deposit money into wallet.

        Args:
            amount (int): Amount to deposit.
        """

        if amount <= 0:
            logging.error("InvalidAmountError: Attempted to process %d VND.", amount)
            raise InvalidAmountError

        self.balance += amount

        logging.info(
            "Deposit successful: +%d VND. Current Balance: %d", amount, self.balance
        )

    def transfer(self, phone, amount):
        """
        Transfer money.

        Args:
            phone (str): Receiver phone number.
            amount (int): Transfer amount.
        """

        if amount <= 0:
            logging.error("InvalidAmountError: Attempted to process %d VND.", amount)
            raise InvalidAmountError

        if amount > self.balance:
            logging.error(
                "InsufficientBalanceError: Attempted to transfer "
                "%d VND with balance %d VND.",
                amount,
                self.balance,
            )
            raise InsufficientBalanceError

        if amount >= 10_000_000:
            logging.warning(
                "High value transaction detected: %d VND to %s", amount, phone
            )

        self.balance -= amount

        logging.info(
            "Transfer successful: -%d VND to %s. " "Current Balance: %d",
            amount,
            phone,
            self.balance,
        )

    def get_balance(self):
        """
        Return current balance.
        """
        logging.info("Balance checked. Current Balance: %d", self.balance)

        return self.balance


def display_menu():
    """
    Display menu.
    """

    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("====================================")


def input_amount():
    """
    Input amount from keyboard.
    """

    while True:
        try:
            amount = int(input("Nhập số tiền: "))
            return amount

        except ValueError:
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
            logging.error("ValueError: Invalid numeric input.")


def input_phone():
    """
    Input phone number.
    """

    while True:
        phone = input("Nhập số điện thoại người nhận: ")

        if re.fullmatch(r"\d{10}", phone):
            return phone

        print("Số điện thoại phải gồm đúng 10 chữ số.")


def deposit_menu(wallet):
    """
    Deposit menu.
    """

    print("\n--- NẠP TIỀN VÀO VÍ ---")

    amount = input_amount()

    try:
        wallet.deposit(amount)

        print(f"\nNạp tiền thành công: +{amount:,} VND")
        print(f"Số dư hiện tại: {wallet.balance:,} VND")

    except InvalidAmountError:
        print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")


def transfer_menu(wallet):
    """
    Transfer menu.
    """

    print("\n--- CHUYỂN TIỀN ---")

    phone = input_phone()

    amount = input_amount()

    try:
        wallet.transfer(phone, amount)

        print(f"\nChuyển tiền thành công tới số " f"{phone}")

        print(f"Số tiền đã chuyển: {amount:,} VND")

        print(f"Số dư còn lại: {wallet.balance:,} VND")

    except InvalidAmountError:
        print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")

    except InsufficientBalanceError:
        print("\nGiao dịch thất bại: " "Số dư của bạn không đủ.")

        print(f"Số dư hiện tại: {wallet.balance:,} VND")


def show_balance(wallet):
    """
    Show current balance.
    """

    balance = wallet.get_balance()

    print("\n--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {balance:,} VND")


def main():
    """
    Main function.
    """

    wallet = Wallet()

    while True:
        display_menu()

        choice = input("\nChọn chức năng (1-4): ")

        if choice == "1":
            deposit_menu(wallet)

        elif choice == "2":
            transfer_menu(wallet)

        elif choice == "3":
            show_balance(wallet)

        elif choice == "4":
            print("\nCảm ơn bạn đã sử dụng dịch vụ.")

            logging.info("System shutdown")

            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
