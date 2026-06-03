# 1. Phân tích và thiết kế
# Input

# | Dữ liệu          | Kiểu |
# | ---------------- | ---- |
# | menu_choice      | int  |
# | sender_name      | str  |
# | sender_phone     | str  |
# | pickup_address   | str  |
# | receiver_name    | str  |
# | receiver_phone   | str  |
# | delivery_address | str  |
# | order_note       | str  |
# | order_code       | str  |
# | find_keyword     | str  |
# | replace_keyword  | str  |

# Output
# Thông tin đơn hàng đã chuẩn hóa.
# Mã đơn hàng đã chuẩn hóa.
# Số điện thoại đã được ẩn.
# Kết quả tìm kiếm và thay thế từ khóa.
# Thông báo lỗi cho các trường dữ liệu không hợp lệ.
# Giải pháp

# Sử dụng các phương thức chuỗi:

# strip() -> loại bỏ khoảng trắng đầu cuối.
# title() -> viết hoa chữ cái đầu mỗi từ.
# upper() -> chuyển thành chữ hoa.
# lower() -> chuyển thành chữ thường.
# split() + ' '.join() -> chuẩn hóa khoảng trắng.
# replace() -> thay thế từ khóa.
# count() -> đếm số lần xuất hiện.
# isdigit() -> kiểm tra số điện thoại.

# Kiểm tra dữ liệu:

# Không cho phép dữ liệu rỗng.
# Số điện thoại phải gồm đúng 10 chữ số.
# Menu phải nằm trong khoảng 1-5.
# Pseudocode
# Khai báo order_note = ""
# sender_phone = ""
# receiver_phone = ""

# Lặp vô hạn:
#     Hiển thị menu

#     Nhập lựa chọn

#     Nếu không phải số:
#         Báo lỗi
#         Tiếp tục

#     Nếu không thuộc 1-5:
#         Báo lỗi
#         Tiếp tục

#     Nếu chọn 1:
#         Nhập thông tin đơn hàng
#         Kiểm tra dữ liệu rỗng
#         Hiển thị báo cáo

#     Nếu chọn 2:
#         Chuẩn hóa mã đơn hàng

#     Nếu chọn 3:
#         Kiểm tra số điện thoại
#         Hiển thị số điện thoại đã ẩn

#     Nếu chọn 4:
#         Kiểm tra ghi chú tồn tại
#         Tìm kiếm và thay thế từ khóa

#     Nếu chọn 5:
#         Thoát chương trình
#         Kết thúc

# Dữ liệu dùng chung
order_note = ""
sender_phone = ""
receiver_phone = ""


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NỘI DUNG ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại khách hàng")
    print("4. Tìm kiếm và thay thế từ khóa trong ghi chú đơn hàng")
    print("5. Thoát chương trình")

    try:
        menu_choice = int(input("Mời bạn chọn chức năng (1-5): "))

        if menu_choice < 1 or menu_choice > 5:
            print("Lựa chọn không hợp lệ")
            continue

    except ValueError:
        print("Lựa chọn không hợp lệ")
        continue

    # Chức năng 1
    if menu_choice == 1:
        sender_name = input("Tên người gửi: ")
        sender_phone = input("SĐT người gửi: ")
        pickup_address = input("Địa chỉ lấy hàng: ")
        receiver_name = input("Tên người nhận: ")
        receiver_phone = input("SĐT người nhận: ")
        delivery_address = input("Địa chỉ giao hàng: ")
        order_note = input("Ghi chú giao hàng: ")

        fields = {
            "Tên người gửi": sender_name,
            "SĐT người gửi": sender_phone,
            "Địa chỉ lấy hàng": pickup_address,
            "Tên người nhận": receiver_name,
            "SĐT người nhận": receiver_phone,
            "Địa chỉ giao hàng": delivery_address,
            "Ghi chú giao hàng": order_note
        }

        is_valid = True

        for field_name, field_value in fields.items():
            if field_value.strip() == "":
                print(f"{field_name} không được bỏ trống")
                is_valid = False

        if not is_valid:
            continue

        pickup_address = " ".join(pickup_address.split())
        delivery_address = " ".join(delivery_address.split())

        print("\n===== BÁO CÁO THỐNG KÊ =====")
        print("Tên người gửi:",
              sender_name.strip().title())
        print("Tên người nhận:",
              receiver_name.strip().title())
        print("Địa chỉ lấy hàng:",
              pickup_address)
        print("Địa chỉ giao hàng:",
              delivery_address)
        print("Ghi chú giao hàng:",
              order_note.strip())
        print("Độ dài ghi chú:",
              len(order_note.strip()))
        print("Số lượng từ:",
              len(order_note.strip().split()))
        print("Ghi chú chữ thường:")
        print(order_note.strip().lower())
        print("Ghi chú chữ hoa:")
        print(order_note.strip().upper())

    # Chức năng 2
    elif menu_choice == 2:
        order_code = input("Nhập mã đơn hàng: ")
        if order_code.strip() == "":
            print("Mã đơn hàng không được bỏ trống")
            continue
        order_code = order_code.strip().upper()
        order_code = "-".join(order_code.split())
        if not order_code.startswith("GRAB-"):
            order_code = "GRAB-" + order_code
        print("Mã đơn hàng chuẩn hóa:", order_code)
    # Chức năng 3
    elif menu_choice == 3:
        def hide_phone(phone_number):
            return (
                phone_number[:3]
                + "*" * 5
                + phone_number[-2:]
            )
        if sender_phone == "" or receiver_phone == "":
            print("Chưa có thông tin số điện thoại")
            continue
        if not sender_phone.isdigit():
            print("Số điện thoại người gửi không hợp lệ")
            continue
        if not receiver_phone.isdigit():
            print("Số điện thoại người nhận không hợp lệ")
            continue
        if len(sender_phone) != 10:
            print(
                "Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự"
            )
            continue
        if len(receiver_phone) != 10:
            print(
                "Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự"
            )
            continue
        print("SĐT người gửi:",
              hide_phone(sender_phone))

        print("SĐT người nhận:",
              hide_phone(receiver_phone))

    # Chức năng 4
    elif menu_choice == 4:
        if order_note.strip() == "":
            print("Chưa có ghi chú giao hàng để tìm kiếm")
            continue
        find_keyword = input("Nhập từ khóa cần tìm: ")
        replace_keyword = input("Nhập từ khóa thay thế: ")
        count_keyword = order_note.count(find_keyword)
        if count_keyword > 0:
            new_note = order_note.replace(
                find_keyword,
                replace_keyword
            )
            print(
                f"Số lần xuất hiện của từ khóa: {count_keyword}"
            )
            print("Ghi chú đơn hàng sau khi thay thế:")
            print(new_note)

            order_note = new_note
        else:
            print(
                "Không tìm thấy từ khóa trong ghi chú giao hàng"
            )
    # Chức năng 5
    else:
        print("Thoát chương trình")
        break