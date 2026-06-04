# 1. Phân tích và thiết kế giải pháp
# Input
# Lựa chọn menu: int
# Mã đơn hàng: string
# Output
# Danh sách đơn hàng hiện tại
# Thông báo thêm/xóa thành công
# Thông báo lỗi khi nhập sai hoặc không tìm thấy đơn hàng
# Giải pháp
# Dùng while True để hiển thị menu
# Dùng append() để thêm đơn hàng
# Dùng remove() để xóa đơn hàng
# Dùng strip() và upper() để chuẩn hóa mã đơn hàng
# Kiểm tra đơn hàng tồn tại bằng toán tử in
# Pseudocode
# Khởi tạo order_list

# Lặp vô hạn:
#     Hiển thị menu
#     Nhập lựa chọn

#     Nếu chọn 1:
#         Hiển thị danh sách

#     Nếu chọn 2:
#         Nhập mã đơn hàng
#         Chuẩn hóa
#         Thêm vào danh sách

#     Nếu chọn 3:
#         Nhập mã cần xóa
#         Chuẩn hóa
#         Nếu tồn tại:
#             Xóa
#         Ngược lại:
#             Thông báo không tìm thấy

#     Nếu chọn 4:
#         Thoát chương trình

#     Ngược lại:
#         Thông báo lựa chọn không hợp lệ


# Danh sách đơn hàng ban đầu
order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for index, order_code in enumerate(order_list, start=1):
                print(f"{index}. {order_code}")

    elif choice == "2":
        new_order = input("Nhập mã đơn hàng mới: ").strip().upper()
        order_list.append(new_order)
        print("Thêm đơn hàng thành công!")

    elif choice == "3":
        delete_order = input("Nhập mã đơn hàng cần xóa: ").strip().upper()

        if delete_order in order_list:
            order_list.remove(delete_order)
            print("Xóa đơn hàng thành công!")
        else:
            print("Không tìm thấy mã đơn hàng cần xóa!")

    elif choice == "4":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")