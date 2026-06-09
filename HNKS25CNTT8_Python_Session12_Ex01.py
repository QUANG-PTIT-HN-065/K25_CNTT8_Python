# 1) Phân tích và thiết kế giải pháp

# Input
# Menu
# choice: int (1-5)
# Thêm sản phẩm
# id: str
# name: str
# number: int (> 0)
# price: float hoặc int (>= 0)
# Cập nhật sản phẩm
# id: str
# new_number: int (> 0)
# Xóa sản phẩm
# id: str

# Output
# Chức năng 1
# Danh sách sản phẩm trong giỏ hàng
# Tổng số lượng sản phẩm
# Tổng tiền
# Chức năng 2
# Thêm mới sản phẩm hoặc tăng số lượng sản phẩm đã tồn tại
# Chức năng 3
# Cập nhật số lượng sản phẩm
# Chức năng 4
# Xóa sản phẩm khỏi giỏ hàng
# Chức năng 5
# Thoát chương trình
# Thông báo lỗi
# Số lượng không hợp lệ
# Đơn giá không hợp lệ
# Mã sản phẩm không tồn tại
# Lựa chọn menu không hợp lệ

# Đề xuất giải pháp
# Hàm xem giỏ hàng
# Duyệt danh sách sản phẩm
# Tính tổng số lượng
# Tính tổng tiền
# Hàm thêm sản phẩm
# Kiểm tra số lượng > 0
# Kiểm tra đơn giá >= 0
# Tìm sản phẩm theo id
# Nếu tồn tại -> cộng dồn số lượng
# Nếu chưa tồn tại -> append vào list
# Hàm cập nhật số lượng
# Kiểm tra số lượng > 0
# Tìm sản phẩm theo id
# Nếu tồn tại -> cập nhật
# Nếu không tồn tại -> báo lỗi
# Hàm xóa sản phẩm
# Tìm sản phẩm theo id
# Nếu tồn tại -> remove
# Nếu không tồn tại -> báo lỗi
# Validation menu
# Chỉ chấp nhận giá trị từ 1 đến 5

# Pseudocode
# Khởi tạo cart_items
# Lặp vô hạn
#     Hiển thị menu
#     Nhập lựa chọn
#     Nếu lựa chọn = 1
#         Hiển thị giỏ hàng
#     Nếu lựa chọn = 2
#         Nhập thông tin sản phẩm
#         Kiểm tra dữ liệu
#         Nếu hợp lệ
#             Nếu mã đã tồn tại
#                 Tăng số lượng
#             Ngược lại
#                 Thêm mới

#     Nếu lựa chọn = 3
#         Nhập mã sản phẩm
#         Nhập số lượng mới
#         Kiểm tra dữ liệu
#         Nếu tồn tại
#             Cập nhật số lượng
#         Ngược lại
#             Báo lỗi
#     Nếu lựa chọn = 4
#         Nhập mã sản phẩm
#         Nếu tồn tại
#             Xóa sản phẩm
#         Ngược lại
#             Báo lỗi
#     Nếu lựa chọn = 5
#         Kết thúc chương trình
#     Ngược lại
#         Báo lỗi menu

cart_items = [
    {"id": "P001", "name": "Dien thoai iPhone 15", "number": 1, "price": 25000000},
    {"id": "P002", "name": "Op lung Silicon", "number": 2, "price": 150000},
]

while True:
    print("\n===== MENU =====")
    print("1. Xem chi tiet gio hang")
    print("2. Them san pham")
    print("3. Cap nhat so luong")
    print("4. Xoa san pham")
    print("5. Thoat")

    try:
        choice = int(input("Nhap lua chon: "))

        if choice == 1:
            total_quantity = 0
            total_amount = 0

            print(
                "\n{:<10}{:<30}{:<10}{:<15}".format(
                    "ID", "TEN SAN PHAM", "SL", "DON GIA"
                )
            )

            for item in cart_items:
                print(
                    "{:<10}{:<30}{:<10}{:<15}".format(
                        item["id"], item["name"], item["number"], item["price"]
                    )
                )

                total_quantity += item["number"]
                total_amount += item["number"] * item["price"]

            print("-" * 70)
            print("Tong so luong:", total_quantity)
            print("Tong tien:", total_amount)

        elif choice == 2:
            product_id = input("Nhap ma san pham: ")
            product_name = input("Nhap ten san pham: ")

            quantity = int(input("Nhap so luong: "))
            price = float(input("Nhap don gia: "))

            if quantity <= 0 or price < 0:
                print("Du lieu khong hop le.")
                continue

            found = False

            for item in cart_items:
                if item["id"] == product_id:
                    item["number"] += quantity
                    found = True
                    print("Da tang so luong san pham.")
                    break

            if not found:
                cart_items.append(
                    {
                        "id": product_id,
                        "name": product_name,
                        "number": quantity,
                        "price": price,
                    }
                )
                print("Them san pham thanh cong.")

        elif choice == 3:
            product_id = input("Nhap ma san pham: ")
            new_quantity = int(input("Nhap so luong moi: "))

            if new_quantity <= 0:
                print("So luong khong hop le.")
                continue

            found = False

            for item in cart_items:
                if item["id"] == product_id:
                    item["number"] = new_quantity
                    found = True
                    print("Cap nhat thanh cong.")
                    break

            if not found:
                print("Ma san pham khong ton tai trong gio hang.")

        elif choice == 4:
            product_id = input("Nhap ma san pham can xoa: ")

            found = False

            for item in cart_items:
                if item["id"] == product_id:
                    cart_items.remove(item)
                    found = True
                    print("Xoa san pham thanh cong.")
                    break

            if not found:
                print("Ma san pham khong ton tai trong gio hang.")

        elif choice == 5:
            print("Thoat chuong trinh.")
            break

        else:
            print("Lua chon khong hop le.")

    except ValueError:
        print("Lua chon khong hop le.")
