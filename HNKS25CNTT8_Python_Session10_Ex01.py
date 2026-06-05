# 1) Phân tích và thiết kế giải pháp
# Input
# Lựa chọn menu (int)
# Mã sản phẩm (str)
# Tên sản phẩm (str)
# Số lượng (int)
# Đơn giá (int)

# Output
# Danh sách sản phẩm trong giỏ hàng
# Tổng số lượng sản phẩm
# Tổng tiền giỏ hàng
# Thông báo thêm, cập nhật, xóa sản phẩm
# Thông báo lỗi khi dữ liệu không hợp lệ

# Đề xuất giải pháp
# Chức năng 1: Xem giỏ hàng
# Duyệt danh sách cart_items
# Hiển thị thông tin từng sản phẩm
# Tính:
# Tổng số lượng
# Tổng tiền = số lượng × đơn giá
# Chức năng 2: Thêm sản phẩm
# Nhập mã, tên, số lượng, đơn giá
# Kiểm tra:
# Số lượng > 0
# Đơn giá > 0
# Nếu mã đã tồn tại:
# Cộng dồn số lượng
# Nếu chưa tồn tại:
# Thêm sản phẩm mới bằng append()
# Chức năng 3: Cập nhật số lượng
# Nhập mã sản phẩm
# Tìm sản phẩm theo mã
# Nếu tìm thấy:
# Cập nhật số lượng mới
# Nếu không:
# Thông báo lỗi
# Chức năng 4: Xóa sản phẩm
# Nhập mã sản phẩm
# Tìm sản phẩm
# Nếu tồn tại:
# Xóa bằng remove()
# Nếu không:
# Thông báo lỗi
# Chức năng 5: Thoát
# Kết thúc chương trình

# Pseudocode
# Khởi tạo cart_items

# Lặp vô hạn:
#     Hiển thị menu

#     Nhập lựa chọn

#     Nếu lựa chọn = 1:
#         Hiển thị giỏ hàng
#         Tính tổng số lượng
#         Tính tổng tiền

#     Nếu lựa chọn = 2:
#         Nhập thông tin sản phẩm

#         Nếu số lượng <= 0 hoặc đơn giá <= 0:
#             Báo lỗi
#         Ngược lại:
#             Tìm mã sản phẩm

#             Nếu đã tồn tại:
#                 Cộng dồn số lượng
#             Nếu chưa tồn tại:
#                 Thêm sản phẩm mới

#     Nếu lựa chọn = 3:
#         Nhập mã sản phẩm
#         Nhập số lượng mới

#         Nếu số lượng <= 0:
#             Báo lỗi
#         Ngược lại:
#             Tìm sản phẩm

#             Nếu tồn tại:
#                 Cập nhật số lượng
#             Nếu không:
#                 Báo lỗi

#     Nếu lựa chọn = 4:
#         Nhập mã sản phẩm

#         Nếu tồn tại:
#             Xóa sản phẩm
#         Nếu không:
#             Báo lỗi

#     Nếu lựa chọn = 5:
#         Thoát chương trình

#     Ngược lại:
#         Báo lựa chọn không hợp lệ

# Danh sách giỏ hàng ban đầu
cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("\n===== SHOPEE CART MANAGEMENT SYSTEM =====")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")

    choice = input("Mời bạn chọn chức năng (1-5): ").strip()

    if choice == "1":
        print("\n===== GIỎ HÀNG =====")

        if len(cart_items) == 0:
            print("Giỏ hàng đang trống.")
            continue

        print(f"{'Mã SP':<10}{'Tên sản phẩm':<30}{'SL':<10}{'Đơn giá':<15}{'Thành tiền'}")

        total_quantity = 0
        total_amount = 0

        for item in cart_items:
            product_id = item[0]
            product_name = item[1]
            quantity = item[2]
            price = item[3]
            amount = quantity * price
            total_quantity += quantity
            total_amount += amount
            print(
                f"{product_id:<10}"
                f"{product_name:<30}"
                f"{quantity:<10}"
                f"{price:<15,}"
                f"{amount:,}"
            )
        print("-" * 80)
        print("Tổng số lượng:", total_quantity)
        print("Tổng tiền:", f"{total_amount:,} VND")

    elif choice == "2":
        product_id = input("Nhập mã sản phẩm: ").strip().upper()
        product_name = input("Nhập tên sản phẩm: ").strip()

        try:
            quantity = int(input("Nhập số lượng: "))
            price = int(input("Nhập đơn giá: "))
            if quantity <= 0 or price <= 0:
                print("Số lượng và đơn giá phải lớn hơn 0.")
                continue
            found = False
            for item in cart_items:
                if item[0] == product_id:
                    item[2] += quantity
                    found = True
                    print("Đã cộng dồn số lượng sản phẩm.")
                    break
            if not found:
                cart_items.append([
                    product_id,
                    product_name,
                    quantity,
                    price
                ])
                print("Đã thêm sản phẩm mới.")
        except ValueError:
            print("Số lượng và đơn giá phải là số nguyên.")
    elif choice == "3":
        product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        try:
            new_quantity = int(input("Nhập số lượng mới: "))
            if new_quantity <= 0:
                print("Số lượng phải lớn hơn 0.")
                continue
            found = False
            for item in cart_items:
                if item[0] == product_id:
                    item[2] = new_quantity
                    found = True
                    print("Cập nhật số lượng thành công.")
                    break
            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        except ValueError:
            print("Số lượng phải là số nguyên.")

    elif choice == "4":
        product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()

        found = False

        for item in cart_items:
            if item[0] == product_id:
                cart_items.remove(item)
                found = True
                print("Đã xóa sản phẩm khỏi giỏ hàng.")
                break

        if not found:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5.")