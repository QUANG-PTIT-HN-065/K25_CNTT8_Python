"""
Main program for Highlands Mini POS.
"""

import logging

from pos_logic import HighlandsPOS, DRINK_MENU, ItemNotFoundError, InvalidQuantityError


def display_menu():
    """
    Display menu.
    """

    print("\n========== HIGHLANDS MINI POS ==========")
    print("1. Xem thực đơn")
    print("2. Thêm món vào giỏ")
    print("3. Xem giỏ hàng & Tính tổng tiền")
    print("4. Thanh toán & Xóa giỏ hàng")
    print("5. Thoát ca làm việc")
    print("========================================")


def view_drink_menu():
    """
    Display drink menu.
    """

    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")

    for code, info in DRINK_MENU.items():
        print(f"[{code}] - " f"{info['name']} - " f"{info['price']:,} VNĐ")


def view_order(pos_system):
    """
    Display current order.
    """

    if not pos_system.current_order:
        print("Giỏ hàng trống, vui lòng " "chọn món (Chức năng 2).")
        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print("Mã SP | Tên đồ uống | Đơn giá | " "Số lượng | Thành tiền")

    for item in pos_system.current_order:
        code = item["code"]
        quantity = item["quantity"]

        name = DRINK_MENU[code]["name"]
        price = DRINK_MENU[code]["price"]

        subtotal = price * quantity

        print(
            f"{code:<5} | "
            f"{name:<20} | "
            f"{price:>7,} | "
            f"{quantity:^8} | "
            f"{subtotal:>8,} VNĐ"
        )

    print("-" * 65)

    total = pos_system.calculate_total()

    print(f"Tổng tiền cần thanh toán: " f"{total:,} VNĐ")


def checkout(pos_system):
    """
    Checkout order.
    """

    if not pos_system.current_order:
        print("Giỏ hàng trống, vui lòng " "chọn món (Chức năng 2).")
        return

    total = pos_system.calculate_total()

    print("\n--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: " f"{total:,} VNĐ")

    answer = input(f"Xác nhận thanh toán " f"{total:,} VNĐ? (y/n): ")

    if answer.lower() == "y":

        logging.info("Checkout successful")

        print("Thanh toán thành công.")

        pos_system.clear_order()

        print("Giỏ hàng đã được làm trống.")

    elif answer.lower() == "n":
        print("Đã hủy thao tác thanh toán.")

    else:
        print("Lựa chọn không hợp lệ. " "Thanh toán đã bị hủy.")


def main():
    """
    Main function.
    """

    pos_system = HighlandsPOS()

    while True:

        display_menu()

        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":

            view_drink_menu()

        elif choice == "2":

            print("\n--- THÊM MÓN VÀO GIỎ ---")

            code = input("Nhập mã đồ uống: ")

            try:

                quantity = int(input("Nhập số lượng: "))

                pos_system.add_to_order(code, quantity)

                code = code.strip().upper()

                print(
                    f"Đã thêm {quantity} x "
                    f"{DRINK_MENU[code]['name']} "
                    f"vào giỏ hàng."
                )

            except ValueError:

                print("Vui lòng nhập số lượng " "là một số nguyên!")

                logging.error("ValueError - " "Invalid quantity input")

            except ItemNotFoundError:

                print("Mã đồ uống không hợp lệ, " "vui lòng kiểm tra lại " "thực đơn!")

            except InvalidQuantityError:

                print("Số lượng phải lớn hơn 0!")

        elif choice == "3":

            view_order(pos_system)

        elif choice == "4":

            checkout(pos_system)

        elif choice == "5":

            logging.info("Cashier logged out. " "System shutdown.")

            print("Đã thoát ca làm việc. " "Hẹn gặp lại!")

            break

        else:

            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
