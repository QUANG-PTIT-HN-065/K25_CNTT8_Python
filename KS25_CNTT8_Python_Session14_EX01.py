# 1) Phân tích và thiết kế
# Biến Global
# inventory_stock = 100
# total_revenue = 0.0
# inventory_stock: Lưu số lượng hàng tồn kho.
# total_revenue: Lưu tổng doanh thu.

# Hai biến này được sử dụng và cập nhật ở nhiều hàm nên phải khai báo toàn cục.

# Biến Local

# Trong các hàm:

# amount
# quantity
# price
# subtotal
# discount
# vat
# final_total

# Các biến này chỉ tồn tại trong phạm vi hàm nên là biến cục bộ.

# Hàm add_stock(amount)

# Input:

# amount (int)

# Output:

# Không trả về giá trị.

# Chức năng:

# Cộng thêm hàng vào inventory_stock.
# Hàm process_sale(quantity)

# Input:

# quantity (int)

# Output:

# True nếu đủ hàng.
# False nếu không đủ hàng.

# Chức năng:

# Kiểm tra tồn kho trước khi bán.
# Hàm calculate_final_price(quantity, price)

# Input:

# quantity (int)
# price (float)

# Output:

# subtotal
# discount
# vat
# final_total

# Chức năng:

# Tính tiền hàng.
# Giảm giá 10% nếu đủ điều kiện.
# Tính VAT 8%.
# Trả về kết quả.
# Hàm print_report()

# Input:

# Không có.

# Output:

# Không trả về giá trị.

# Chức năng:

# Hiển thị tồn kho.
# Hiển thị doanh thu.

inventory_stock = 100
total_revenue = 0.0


def add_stock(amount):
    """
    Thêm sản phẩm vào kho.

    Parameters:
        amount (int): Số lượng cần nhập thêm.

    Returns:
        None
    """
    global inventory_stock

    inventory_stock += amount

    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")


def process_sale(quantity):
    """
    Kiểm tra tồn kho trước khi bán.

    Parameters:
        quantity (int): Số lượng khách muốn mua.

    Returns:
        bool: True nếu đủ hàng, False nếu không đủ hàng.
    """
    if quantity > inventory_stock:
        print(
            f"Lỗi: Không đủ hàng trong kho. "
            f"Tồn kho hiện tại chỉ còn {inventory_stock}."
        )
        return False

    return True


def calculate_final_price(quantity, price):
    """
    Tính hóa đơn cuối cùng.

    Parameters:
        quantity (int): Số lượng mua.
        price (float): Đơn giá.

    Returns:
        tuple: (subtotal, discount, vat, final_total)
    """

    subtotal = quantity * price

    discount = 0

    if subtotal >= 1000:
        discount = subtotal * 0.10

    after_discount = subtotal - discount

    vat = after_discount * 0.08

    final_total = after_discount + vat

    return subtotal, discount, vat, final_total


def print_report():
    """
    Hiển thị báo cáo tổng quan của hệ thống.

    Bao gồm:
    - Số lượng hàng tồn kho hiện tại.
    - Tổng doanh thu đã ghi nhận.
    """

    print("\n--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")
    print("--------------------------")


def input_positive_int(message):
    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print("Dữ liệu nhập vào phải lớn hơn 0.")
                continue

            return value

        except ValueError:
            print("Vui lòng nhập đúng kiểu dữ liệu số.")


def input_positive_float(message):
    while True:
        try:
            value = float(input(message))

            if value <= 0:
                print("Dữ liệu nhập vào phải lớn hơn 0.")
                continue

            return value

        except ValueError:
            print("Vui lòng nhập đúng kiểu dữ liệu số.")


def main():
    global inventory_stock
    global total_revenue

    while True:

        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (Tính toán hóa đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":

            print("\n--- NHẬP HÀNG ---")

            amount = input_positive_int("Nhập số lượng sản phẩm muốn thêm: ")

            add_stock(amount)

        elif choice == "2":

            print("\n--- BÁN HÀNG ---")

            quantity = input_positive_int("Nhập số lượng mua: ")

            price = input_positive_float("Nhập đơn giá ($): ")

            if not process_sale(quantity):
                continue

            subtotal, discount, vat, final_total = calculate_final_price(
                quantity, price
            )

            inventory_stock -= quantity
            total_revenue += final_total

            print("-> Hóa đơn chi tiết:")
            print(f"Số lượng: {quantity} | " f"Đơn giá: ${price}")
            print(f"Tạm tính: ${subtotal}")
            print(f"Giảm giá (10%): ${discount}")
            print(f"Thuế VAT (8%): ${vat}")
            print(f"Tổng thanh toán: ${final_total}")
            print("Đã bán thành công!")

        elif choice == "3":

            print_report()

        elif choice == "4":

            print("Lưu dữ liệu thành công.")
            print("Thoát chương trình.")
            break

        else:

            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
