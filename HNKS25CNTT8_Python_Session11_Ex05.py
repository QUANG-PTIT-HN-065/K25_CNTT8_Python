# 1) Phân tích và thiết kế giải pháp

# Input
# Lựa chọn menu (str)
# Mã sản phẩm (str)
# Số lượng mua (str)
# Số lượng đổi trả (str)
# Phần trăm giảm giá (str)
# Số lượng nhập kho (str)

# Output
# Danh sách sản phẩm
# Tổng tiền khách cần thanh toán
# Số tiền hoàn trả
# Thông báo cập nhật giảm giá thành công
# Thông báo nhập kho thành công
# Các thông báo lỗi

# Giải pháp
# Dùng list chứa các dictionary

# Chuẩn hóa mã sản phẩm:

# product_id = input().strip().upper()
# Kiểm tra dữ liệu số bằng isdigit()
# Bán hàng:
# Trừ tồn kho
# Tăng số lượng đã bán
# Tính tiền sau giảm giá
# Đổi trả:
# Giảm số lượng đã bán
# Tăng tồn kho
# Tăng số lượng đổi trả
# Tính tiền hoàn
# Giảm giá:
# Kiểm tra từ 0 đến 70
# Nhập kho:
# Cộng thêm tồn kho

# Thuật toán
# Lặp vô hạn
#     Hiển thị menu
#     Nếu chọn 1:
#         Hiển thị danh sách sản phẩm
#     Nếu chọn 2:
#         Bán sản phẩm
#     Nếu chọn 3:
#         Đổi trả sản phẩm
#     Nếu chọn 4:
#         Cập nhật giảm giá
#     Nếu chọn 5:
#         Nhập thêm hàng
#     Nếu chọn 6:
#         Thoát chương trình
#     Ngược lại:
#         Báo lỗi

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0,
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10,
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15,
    },
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Xử lý đổi trả sản phẩm")
    print("4. Áp dụng giảm giá cho sản phẩm")
    print("5. Nhập thêm hàng vào kho cửa hàng")
    print("6. Thoát chương trình")

    choice = input("Chọn chức năng: ")

    if choice == "1":

        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            for i in range(len(product_list)):

                quantity = product_list[i]["quantity"]

                if quantity == 0:
                    status = "Hết hàng"
                elif quantity <= 5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"

                print(
                    f"{i+1}. Mã SP: {product_list[i]['product_id']} | "
                    f"Tên: {product_list[i]['product_name']} | "
                    f"Giá: {product_list[i]['price']} | "
                    f"Tồn kho: {product_list[i]['quantity']} | "
                    f"Đã bán: {product_list[i]['sold']} | "
                    f"Đổi trả: {product_list[i]['returned']} | "
                    f"Giảm giá: {product_list[i]['discount']}% | "
                    f"Trạng thái: {status}"
                )

    elif choice == "2":

        product_id = input("Nhập mã sản phẩm khách muốn mua: ").strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                found = True

                quantity_buy = input("Nhập số lượng khách mua: ")

                if not quantity_buy.isdigit():
                    print("Số lượng mua không hợp lệ")
                    break

                quantity_buy = int(quantity_buy)

                if quantity_buy <= 0:
                    print("Số lượng mua không hợp lệ")
                    break

                if quantity_buy > product["quantity"]:
                    print("Số lượng trong kho không đủ để bán")
                    break

                discount_price = product["price"] * (100 - product["discount"]) / 100

                total_money = discount_price * quantity_buy

                product["quantity"] -= quantity_buy
                product["sold"] += quantity_buy

                print("Bán hàng thành công")
                print("Tổng tiền:", int(total_money))

                break

        if found == False:
            print("Không tìm thấy sản phẩm cần bán")

    elif choice == "3":

        product_id = input("Nhập mã sản phẩm khách muốn đổi/trả: ").strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                found = True

                quantity_return = input("Nhập số lượng đổi/trả: ")

                if not quantity_return.isdigit():
                    print("Số lượng đổi/trả không hợp lệ")
                    break

                quantity_return = int(quantity_return)

                if quantity_return <= 0:
                    print("Số lượng đổi/trả không hợp lệ")
                    break

                if quantity_return > product["sold"]:
                    print("Số lượng đổi/trả không được vượt quá số lượng đã bán")
                    break

                refund_price = product["price"] * (100 - product["discount"]) / 100

                refund_money = refund_price * quantity_return

                product["sold"] -= quantity_return
                product["quantity"] += quantity_return
                product["returned"] += quantity_return

                print("Đổi trả thành công")
                print("Tiền hoàn lại:", int(refund_money))

                break

        if found == False:
            print("Không tìm thấy sản phẩm cần đổi trả")

    elif choice == "4":

        product_id = input("Nhập mã sản phẩm cần áp dụng giảm giá: ").strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                found = True

                discount = input("Nhập phần trăm giảm giá: ")

                if not discount.isdigit():
                    print("Phần trăm giảm giá không hợp lệ")
                    break

                discount = int(discount)

                if discount < 0 or discount > 70:
                    print("Phần trăm giảm giá không hợp lệ")
                    break

                product["discount"] = discount

                print("Cập nhật giảm giá thành công")

                break

        if found == False:
            print("Không tìm thấy sản phẩm cần áp dụng giảm giá")

    elif choice == "5":

        product_id = input("Nhập mã sản phẩm cần nhập thêm: ").strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                found = True

                quantity_add = input("Nhập số lượng nhập thêm: ")

                if not quantity_add.isdigit():
                    print("Số lượng nhập kho không hợp lệ")
                    break

                quantity_add = int(quantity_add)

                if quantity_add <= 0:
                    print("Số lượng nhập kho không hợp lệ")
                    break

                product["quantity"] += quantity_add

                print("Nhập kho thành công")

                break

        if found == False:
            print("Không tìm thấy sản phẩm cần nhập kho")

    elif choice == "6":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
