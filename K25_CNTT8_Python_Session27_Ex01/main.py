"""
1) Phân tích và thiết kế giải pháp
1. Sơ đồ cấu trúc
            BaseAccount (Abstract)
             /                  \
   SavingsAccount         CreditAccount
          ^
          |
DigitalPremiumMixin
          ^
          |
    HybridAccount
(SavingsAccount, DigitalPremiumMixin)

BaseAccount: Lớp cha, chứa thuộc tính và phương thức chung.
HybridAccount: Đa kế thừa từ SavingsAccount và DigitalPremiumMixin, kết hợp tính lãi và hoàn tiền.

2. Báo cáo kỹ thuật
MRO: Python tìm phương thức theo thứ tự:
HybridAccount -> SavingsAccount -> BaseAccount -> DigitalPremiumMixin -> object.
Duck Typing: Hàm thanh toán chỉ cần đối tượng có execute_pay(), nên có thể thêm nhiều cổng thanh toán mới mà không cần sửa lớp BaseAccount hay các lớp tài khoản.

"""

from object import *

accounts = []
current_account = None


def create_account():
    global current_account

    while True:

        print(
            "\n========== OPEN ACCOUNT ==========\n"
            "1. Savings Account\n"
            "2. Credit Account\n"
            "3. Hybrid Account\n"
            "4. Back\n"
        )

        choice = input("Choose: ")

        if choice in ("1", "2", "3", "4"):
            break

        print("Invalid choice.")

    if choice == "4":
        return

    account_number = input("Account Number (10 digits): ")

    if not BaseAccount.validate_account_number(account_number):
        print("Invalid account number.")
        return

    owner_name = input("Owner Name: ")

    try:
        balance = float(input("Initial Balance: "))

        if balance < 0:
            print("Balance cannot be negative.")
            return

    except ValueError:
        print("Invalid balance.")
        return

    if choice == "1":

        try:
            interest_rate = float(input("Interest Rate: "))

        except ValueError:
            print("Invalid interest rate.")
            return

        account = SavingsAccount(account_number, owner_name, interest_rate, balance)

    elif choice == "2":

        try:
            credit_limit = float(input("Credit Limit: "))

            if credit_limit < 0:
                print("Credit limit cannot be negative.")
                return

        except ValueError:
            print("Invalid credit limit.")
            return

        account = CreditAccount(account_number, owner_name, credit_limit, balance)

    else:

        try:
            interest_rate = float(input("Interest Rate: "))

        except ValueError:
            print("Invalid interest rate.")
            return

        account = HybridAccount(account_number, owner_name, interest_rate, balance)

    accounts.append(account)
    current_account = account

    print("\nCreate account successfully.")
    print("Owner:", account.owner_name)


def show_account():

    if current_account is None:
        print("No account.")
        return

    print("\n========== ACCOUNT ==========")

    print("Type:", type(current_account).__name__)
    print("Bank:", current_account.bank_name)
    print("Account Number:", current_account.account_number)
    print("Owner:", current_account.owner_name)
    print(f"Balance: {current_account.balance:,.0f} VND")

    if isinstance(current_account, SavingsAccount):
        print(f"Interest Rate: " f"{current_account.interest_rate * 100:.2f}%")

    if isinstance(current_account, CreditAccount):
        print(f"Credit Limit: " f"{current_account.credit_limit:,.0f} VND")

    print("\n========== MRO ==========")

    for cls in type(current_account).__mro__:
        print(cls.__name__)


def transaction():

    if current_account is None:
        print("No account.")
        return

    print("\n1. Deposit\n" "2. Withdraw")

    choice = input("Choose: ")

    try:
        amount = float(input("Amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    if choice == "1":

        current_account.deposit(amount)

        if isinstance(current_account, HybridAccount):
            current_account.cashback_reward(amount)

    elif choice == "2":

        current_account.withdraw(amount)

    else:
        print("Invalid choice.")


def interest():

    if current_account is None:
        print("No account.")
        return

    if isinstance(current_account, SavingsAccount):

        current_account.apply_interest()

    else:
        print("Current account doesn't support interest.")


def overloading():

    global current_account

    if current_account is None:
        print("No current account.")
        return

    if len(accounts) < 2:
        print("Need at least 2 accounts.")
        return

    print("\n========== ACCOUNT LIST ==========")

    available_accounts = []

    index = 1

    for account in accounts:

        if account is not current_account:

            available_accounts.append(account)

            print(
                f"{index}. "
                f"{account.account_number} | "
                f"{account.owner_name} | "
                f"{account.balance:,.0f} VND"
            )

            index += 1

    try:
        choice = int(input("Choose account: "))

        if choice < 1 or choice > len(available_accounts):
            print("Invalid choice.")
            return

    except ValueError:
        print("Invalid input.")
        return

    other = available_accounts[choice - 1]

    try:

        total = current_account + other

        print(f"\nTotal Balance: {total:,.0f} VND")

        if current_account < other:
            print("Current account has less balance.")

        elif other < current_account:
            print("Current account has greater balance.")

        else:
            print("Both accounts have the same balance.")

    except TypeError:
        print("Operator overloading failed.")


def payment():

    if current_account is None:
        print("No account.")
        return

    print("\n1. VNPay\n" "2. Viettel Money")

    choice = input("Choose: ")

    try:
        amount = float(input("Amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    if choice == "1":

        gateway = VNPayGateway()

    elif choice == "2":

        gateway = ViettelMoneyGateway()

    else:
        print("Invalid choice.")
        return

    process_payment(gateway, current_account, amount)


# ==========================================================
# MAIN
# ==========================================================
def main():

    while True:

        print(
            "\n========== VIETCOMBANK DIGIBANK PRO ==========\n"
            "1. Open Account\n"
            "2. Show Account & MRO\n"
            "3. Deposit / Withdraw\n"
            "4. Apply Interest\n"
            "5. Operator Overloading\n"
            "6. Payment Gateway\n"
            "7. Exit\n"
        )

        choice = input("Choose: ")

        if choice == "1":

            create_account()

        elif choice == "2":

            show_account()

        elif choice == "3":

            transaction()

        elif choice == "4":

            interest()

        elif choice == "5":

            overloading()

        elif choice == "6":

            payment()

        elif choice == "7":

            print("Good Bye.")
            break

        else:

            print("Invalid choice.")


main()
