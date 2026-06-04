# 1) Phân tích và thiết kế giải pháp
# Input
# Lựa chọn menu: string
# Mã đơn hàng: string
# Output
# Danh sách đơn hàng.
# Thông báo cập nhật trạng thái.
# Thông báo lỗi khi dữ liệu không hợp lệ.
# Giải pháp
# Sử dụng while True để hiển thị menu.
# Chuẩn hóa mã đơn hàng bằng strip().upper().
# Duyệt danh sách bằng enumerate().
# Tách mã đơn hàng và trạng thái bằng split(" - ").
# Cập nhật trạng thái bằng cách gán lại phần tử trong List.
# Kiểm tra luồng trạng thái theo yêu cầu nghiệp vụ.
# Pseudocode
# Khởi tạo order_list

# Lặp vô hạn:
#     Hiển thị menu
#     Nếu chọn 1:
#         Hiển thị danh sách đơn hàng
#     Nếu chọn 2:
#         Nhập mã đơn hàng
#         Tìm đơn hàng
#         Nếu trạng thái PENDING:
#             Chuyển thành ASSIGNED
#         Ngược lại:
#             Thông báo lỗi
#     Nếu chọn 3:
#         Nhập mã đơn hàng
#         Tìm đơn hàng
#         ASSIGNED -> DELIVERING
#         DELIVERING -> COMPLETED
#         Các trạng thái khác:
#             Thông báo phù hợp
#     Nếu chọn 4:
#         Nhập mã đơn hàng
#         Tìm đơn hàng
#         Nếu PENDING hoặc ASSIGNED:
#             Chuyển thành CANCELLED
#         Ngược lại:
#             Thông báo phù hợp
#     Nếu chọn 5:
#         Thoát
#     Ngược lại:
#         Báo lỗi

# Danh sách đơn hàng ban đầu
order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

while True:
    print("\n===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Gán tài xế cho đơn hàng")
    print("3. Cập nhật trạng thái giao hàng")
    print("4. Hủy đơn hàng")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")

    elif choice == "2":
        order_code = input("Nhập mã đơn hàng: ").strip().upper()

        found = False

        for index, order in enumerate(order_list):
            code, status = order.split(" - ")

            if code == order_code:
                found = True

                if status == "PENDING":
                    order_list[index] = f"{code} - ASSIGNED"
                    print("Gán tài xế thành công!")
                else:
                    print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý.")
                break

        if not found:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == "3":
        order_code = input("Nhập mã đơn hàng: ").strip().upper()

        found = False

        for index, order in enumerate(order_list):
            code, status = order.split(" - ")

            if code == order_code:
                found = True

                if status == "ASSIGNED":
                    order_list[index] = f"{code} - DELIVERING"
                    print("Cập nhật trạng thái thành DELIVERING.")

                elif status == "DELIVERING":
                    order_list[index] = f"{code} - COMPLETED"
                    print("Cập nhật trạng thái thành COMPLETED.")

                elif status == "PENDING":
                    print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")

                elif status == "COMPLETED":
                    print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")

                elif status == "CANCELLED":
                    print("Đơn hàng đã bị hủy, không thể cập nhật.")

                break

        if not found:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == "4":
        order_code = input("Nhập mã đơn hàng cần hủy: ").strip().upper()

        found = False

        for index, order in enumerate(order_list):
            code, status = order.split(" - ")

            if code == order_code:
                found = True

                if status in ["PENDING", "ASSIGNED"]:
                    order_list[index] = f"{code} - CANCELLED"
                    print("Hủy đơn hàng thành công.")

                elif status == "DELIVERING":
                    print("Đơn hàng đang được giao, không thể hủy.")

                elif status == "COMPLETED":
                    print("Đơn hàng đã hoàn tất, không thể hủy.")

                elif status == "CANCELLED":
                    print("Đơn hàng đã được hủy trước đó.")

                break

        if not found:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == "5":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")