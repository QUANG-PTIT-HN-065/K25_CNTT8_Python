# 1) Phân tích và thiết kế
# Biến Global
# atm_vault_balance = 50000000
# user_account_balance = 10000000
# atm_vault_balance: Tiền mặt hiện có trong ATM
# user_account_balance: Số dư tài khoản khách hàng

# Các hàm deposit_money() và execute_withdrawal() cần cập nhật trực tiếp các biến này nên phải sử dụng global

# Truyền Arguments vào hàm

# Các dữ liệu nhập từ người dùng cần truyền qua tham số:

# deposit_money(amount)
# check_withdrawal_rules(amount)
# execute_withdrawal(total_deduction, amount_to_dispense)

# Điều này giúp hàm tái sử dụng và dễ kiểm thử

# Hàm display_balances()

# Input: Không có

# Output: Không trả về giá trị

# Chức năng: Hiển thị số dư tài khoản và tiền mặt trong ATM

# Hàm deposit_money(amount)

# Input:

# amount (int)

# Output:

# True nếu thành công
# False nếu thất bại

# Chức năng:

# Tăng số dư tài khoản
# Tăng tiền mặt trong ATM
# Hàm check_withdrawal_rules(amount)

# Input:

# amount (int)

# Output:

# "INVALID_AMOUNT"
# "INVALID_MULTIPLE"
# "INSUFFICIENT_FUNDS"
# "ATM_OUT_OF_CASH"
# "OK"

# Chức năng:

# Kiểm tra điều kiện rút tiền
# Hàm execute_withdrawal(total_deduction, amount_to_dispense)

# Input:

# total_deduction (int)
# amount_to_dispense (int)

# Output: Không trả về giá trị

# Chức năng:

# Trừ tiền trong tài khoản
# Trừ tiền mặt trong ATM
# In biên lai

atm_vault_balance = 50000000
user_account_balance = 10000000


def display_balances():
    """
    Hiển thị số dư tài khoản và tiền mặt ATM.

    Parameters:
        None

    Returns:
        None
    """

    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    """
    Nạp tiền vào tài khoản.

    Parameters:
        amount (int): Số tiền muốn nạp.

    Returns:
        bool: True nếu thành công.
    """

    global user_account_balance
    global atm_vault_balance

    user_account_balance += amount
    atm_vault_balance += amount

    return True


def check_withdrawal_rules(amount):
    """
    Kiểm tra điều kiện rút tiền.

    Parameters:
        amount (int): Số tiền cần rút.

    Returns:
        str: Trạng thái giao dịch.
    """

    fee = 1100
    total_deduction = amount + fee

    if amount <= 0:
        return "INVALID_AMOUNT"

    if amount % 50000 != 0:
        return "INVALID_MULTIPLE"

    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"

    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"

    return "OK"


def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Thực hiện giao dịch rút tiền.

    Parameters:
        total_deduction (int): Tổng tiền bị trừ.
        amount_to_dispense (int): Tiền thực nhận.

    Returns:
        None
    """

    global user_account_balance
    global atm_vault_balance

    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense

    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công " f"{amount_to_dispense:,} VND.")
    print(f"Số dư tài khoản còn lại: " f"{user_account_balance:,} VND.")


def input_positive_amount(message):
    """
    Nhập số tiền hợp lệ.

    Parameters:
        message (str): Nội dung nhập.

    Returns:
        int: Số tiền hợp lệ.
    """

    while True:
        try:
            amount = int(input(message))

            if amount <= 0:
                print("Số tiền không hợp lệ")
                continue

            return amount

        except ValueError:
            print("Số tiền không hợp lệ")


def main():
    """
    Hàm điều khiển chương trình ATM.

    Parameters:
        None

    Returns:
        None
    """

    while True:

        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")

        choice = input("Vui lòng chọn giao dịch (1-4): ").strip()

        if choice == "1":

            display_balances()

        elif choice == "2":

            print("\n--- NẠP TIỀN ---")

            amount = input_positive_amount("Nhập số tiền muốn nạp: ")

            if deposit_money(amount):
                print(
                    f"Giao dịch thành công! "
                    f"Số dư tài khoản hiện tại: "
                    f"{user_account_balance:,} VND."
                )

        elif choice == "3":

            print("\n--- RÚT TIỀN ---")

            amount = input_positive_amount("Nhập số tiền cần rút: ")

            status = check_withdrawal_rules(amount)

            if status == "INVALID_MULTIPLE":
                print("Số tiền rút phải là " "bội số của 50,000")

            elif status == "INSUFFICIENT_FUNDS":
                print("Giao dịch thất bại: " "Số dư tài khoản không đủ.")

            elif status == "ATM_OUT_OF_CASH":
                print("Giao dịch thất bại: " "Máy ATM không đủ tiền mặt " "để phục vụ.")

            elif status == "OK":

                fee = 1100
                total_deduction = amount + fee

                execute_withdrawal(total_deduction, amount)

        elif choice == "4":

            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break

        else:

            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
