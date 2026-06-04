# 1) Phân tích và thiết kế giải pháp
# Input
# Lựa chọn menu: int
# Mã đơn hàng: string
# Trạng thái đơn hàng: string
# Vị trí cần sửa/xóa: int
# Output
# Danh sách đơn hàng.
# Thông báo thêm, sửa, xóa thành công.
# Báo cáo thống kê theo trạng thái.
# Thông báo lỗi khi dữ liệu không hợp lệ.
# Giải pháp
# Dùng while True để tạo menu chính và menu con.
# Dùng append() để thêm đơn hàng.
# Dùng gán qua index để sửa đơn hàng.
# Dùng pop(index) để xóa đơn hàng theo vị trí.
# Dùng strip() và upper() để chuẩn hóa dữ liệu.
# Dùng split(" - ") để tách trạng thái khi thống kê.
# Kiểm tra vị trí bằng isdigit() và giới hạn từ 1 đến len(order_list).
# Pseudocode
# Khởi tạo order_list

# Lặp vô hạn:
#     Hiển thị menu chính
#     Nhập lựa chọn
#     Nếu chọn 1:
#         Hiển thị danh sách
#     Nếu chọn 2:
#         Hiển thị menu cập nhật
#         Nếu thêm:
#             Nhập mã và trạng thái
#             Chuẩn hóa
#             append()
#         Nếu sửa:
#             Nhập vị trí
#             Kiểm tra hợp lệ
#             Nhập dữ liệu mới
#             Cập nhật bằng index
#         Nếu xóa:
#             Nhập vị trí
#             Kiểm tra hợp lệ
#             pop(index)
#         Nếu quay lại:
#             Trở về menu chính
#     Nếu chọn 3:
#         Thống kê số lượng từng trạng thái
#     Nếu chọn 4:
#         Thoát chương trình
#     Ngược lại:
#         Báo lỗi

# Danh sách đơn hàng ban đầu
order_list = ["GE001 - PENDING", "GE002 - DELIVERING", "GE003 - CANCELLED"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")

    elif choice == "2":
        while True:
            print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")

            sub_choice = input("Nhập lựa chọn: ").strip()

            if sub_choice == "1":
                order_code = input("Nhập mã đơn hàng: ").strip().upper()
                status = input("Nhập trạng thái: ").strip().upper()

                order_list.append(f"{order_code} - {status}")
                print("Thêm đơn hàng thành công!")

            elif sub_choice == "2":
                position = input("Nhập vị trí cần sửa: ").strip()

                if not position.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue

                position = int(position)

                if position < 1 or position > len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này!")
                    continue

                order_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                status = input("Nhập trạng thái mới: ").strip().upper()

                order_list[position - 1] = f"{order_code} - {status}"
                print("Cập nhật thành công!")

            elif sub_choice == "3":
                position = input("Nhập vị trí cần xóa: ").strip()

                if not position.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue

                position = int(position)

                if position < 1 or position > len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này!")
                    continue

                deleted_order = order_list.pop(position - 1)
                print("Đã xóa:", deleted_order)

            elif sub_choice == "4":
                break

            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

    elif choice == "3":
        pending_count = 0
        delivering_count = 0
        completed_count = 0
        cancelled_count = 0

        for order in order_list:
            status = order.split(" - ")[1]

            if status == "PENDING":
                pending_count += 1
            elif status == "DELIVERING":
                delivering_count += 1
            elif status == "COMPLETED":
                completed_count += 1
            elif status == "CANCELLED":
                cancelled_count += 1

        print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
        print(f"PENDING: {pending_count}")
        print(f"DELIVERING: {delivering_count}")
        print(f"COMPLETED: {completed_count}")
        print(f"CANCELLED: {cancelled_count}")
        print(f"Tổng số đơn hàng: {len(order_list)}")

    elif choice == "4":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
