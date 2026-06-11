# 1) Phân tích và thiết kế
# Luồng dữ liệu (Pseudo-code)
# Người dùng nhập:
#     số lượng vé
#     hạng vé

# ↓
# calculate_ticket_cost(quantity, ticket_class)

#     tính giá vé theo hạng
#     tính tạm tính
#     tính phí dịch vụ 5%
#     tính tổng thanh toán

#     return subtotal, service_fee, final_total

# ↓

# book_flight(quantity, final_total)

#     kiểm tra ghế trống

#     nếu không đủ ghế
#         báo lỗi

#     nếu đủ ghế
#         available_seats -= quantity
#         flight_revenue += final_total

# ↓

# In vé xác nhận
# Tính toàn vẹn dữ liệu
# Biến toàn cục
# available_seats = 50
# flight_revenue = 0.0
# BASE_PRICE = 2000.0
# available_seats lưu trạng thái ghế của chuyến bay.
# flight_revenue lưu tổng doanh thu toàn bộ hệ thống.
# BASE_PRICE là hằng số giá vé cơ bản.
# Vì sao flight_revenue phải là biến toàn cục?
# Doanh thu được thay đổi ở nhiều giao dịch đặt vé và hủy vé.
# Mọi hàm phải cập nhật cùng một giá trị doanh thu chung.
# Nếu dùng biến cục bộ, mỗi hàm sẽ tạo bản sao riêng làm dữ liệu không đồng bộ.
# Hàm calculate_ticket_cost()

# Input

# quantity (int)
# ticket_class (int)

# Output

# subtotal (float)
# service_fee (float)
# final_total (float)
# Hàm book_flight()

# Input

# quantity (int)
# final_total (float)

# Output

# True / False
# Hàm cancel_booking()

# Input

# quantity (int)

# Output

# refund_amount (float)
# Hàm print_flight_report()

# Input

# Không có

# Output

# Không trả về giá trị

available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0
MAX_SEATS = 50


def calculate_ticket_cost(quantity, ticket_class):
    """
    Tính tổng chi phí đặt vé.

    Parameters:
        quantity (int): Số lượng vé.
        ticket_class (int): 1 = Economy, 2 = Business.

    Returns:
        tuple[float, float, float]:
        (subtotal, service_fee, final_total)
    """

    if ticket_class == 1:
        ticket_price = BASE_PRICE
    else:
        ticket_price = BASE_PRICE * 1.5

    subtotal = quantity * ticket_price
    service_fee = subtotal * 0.05
    final_total = subtotal + service_fee

    return subtotal, service_fee, final_total


def book_flight(quantity, final_total):
    """
    Xử lý đặt vé và cập nhật doanh thu.

    Returns:
        bool
    """

    global available_seats
    global flight_revenue

    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn " f"{available_seats} chỗ trống.")
        return False

    available_seats -= quantity
    flight_revenue += final_total

    return True


def cancel_booking(quantity):
    """
    Hủy vé và hoàn tiền.

    Returns:
        float | None
    """

    global available_seats
    global flight_revenue

    if available_seats + quantity > MAX_SEATS:
        print("Lỗi: Số lượng vé hủy vượt quá " "số vé đã bán ra.")
        return None

    refund_amount = quantity * BASE_PRICE * 0.8

    available_seats += quantity
    flight_revenue -= refund_amount

    if flight_revenue < 0:
        flight_revenue = 0

    return refund_amount


def print_flight_report():
    """
    Hiển thị báo cáo chuyến bay VN2026.

    Nội dung:
    - Sức chứa tối đa
    - Ghế đã đặt
    - Ghế trống
    - Tổng doanh thu hiện tại
    """

    booked_seats = MAX_SEATS - available_seats

    print("\n--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: {MAX_SEATS}")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue}")
    print("------------------------------------")


def input_positive_int(message):

    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print("Dữ liệu không hợp lệ.")
                continue

            return value

        except ValueError:
            print("Dữ liệu không hợp lệ.")


def input_ticket_class():

    while True:

        ticket_class = input("Chọn hạng vé (1: Economy, 2: Business): ")

        if ticket_class in ("1", "2"):
            return int(ticket_class)

        print("Hạng vé không hợp lệ.")


def main():

    while True:

        print("\n============= SKYBOOKING SYSTEM =============")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")
        print("=============================================")

        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":

            print("\n--- ĐẶT VÉ MÁY BAY ---")

            quantity = input_positive_int("Nhập số lượng vé: ")

            ticket_class = input_ticket_class()

            subtotal, service_fee, final_total = calculate_ticket_cost(
                quantity, ticket_class
            )

            if book_flight(quantity, final_total):

                ticket_name = "Economy" if ticket_class == 1 else "Business"

                print("-> Xác nhận đặt chỗ:")
                print(f"Số lượng: {quantity} | " f"Hạng: {ticket_name}")
                print(f"Tạm tính: ${subtotal}")
                print(f"Phí dịch vụ (5%): " f"${service_fee}")
                print(f"Tổng thanh toán: " f"${final_total}")
                print(
                    f"Đặt vé thành công! " f"Ghế trống còn lại: " f"{available_seats}"
                )

        elif choice == "2":

            print("\n--- HỦY VÉ & HOÀN TIỀN ---")

            quantity = input_positive_int("Nhập số lượng vé muốn hủy: ")

            refund_amount = cancel_booking(quantity)

            if refund_amount is not None:

                print(
                    f"Hủy vé thành công. "
                    f"Hệ thống đã hoàn lại: "
                    f"${refund_amount} "
                    f"(80% giá cơ bản)."
                )

                print(f"Ghế trống hiện tại: " f"{available_seats}")

        elif choice == "3":

            print_flight_report()

        elif choice == "4":

            print("Đóng hệ thống thành công.")
            print("Cảm ơn bạn đã sử dụng SkyBooking!")
            break

        else:

            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
