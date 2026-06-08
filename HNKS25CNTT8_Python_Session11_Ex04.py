# 1) Phân tích và thiết kế giải pháp

# Input
# Lựa chọn menu (str)
# Mã sản phẩm (str)
# Số lượng mua (str -> int)
# Số lượng nhập kho (str -> int)

# Output
# Danh sách sản phẩm và trạng thái tồn kho
# Thông báo bán hàng thành công
# Thông báo nhập kho thành công
# Báo cáo doanh thu
# Các thông báo lỗi khi dữ liệu không hợp lệ

# Giải pháp
# Sử dụng list chứa các dictionary

# Chuẩn hóa mã sản phẩm bằng:

# strip().upper()

# Kiểm tra số lượng bằng:

# isdigit()
# Bán hàng:
# Trừ tồn kho
# Tăng số lượng đã bán
# Tính tiền thanh toán
# Nhập kho:
# Cộng thêm vào số lượng tồn kho
# Báo cáo:
# Doanh thu từng sản phẩm = price * sold
# Tổng doanh thu = tổng doanh thu các sản phẩm
# Tìm sản phẩm có sold lớn nhất

# Thuật toán
# Hiển thị menu
# Lặp vô hạn:
#     Nhập lựa chọn
#     Nếu chọn 1:
#         Hiển thị danh sách sản phẩm
#         Kiểm tra trạng thái tồn kho
#     Nếu chọn 2:
#         Nhập mã sản phẩm
#         Kiểm tra tồn tại
#         Nhập số lượng mua
#         Kiểm tra hợp lệ
#         Kiểm tra tồn kho
#         Cập nhật tồn kho và đã bán
#     Nếu chọn 3:
#         Nhập mã sản phẩm
#         Kiểm tra tồn tại
#         Nhập số lượng nhập
#         Cộng thêm vào tồn kho
#     Nếu chọn 4:
#         Tính doanh thu từng sản phẩm
#         Tính tổng doanh thu
#         Tìm sản phẩm bán chạy nhất
#     Nếu chọn 5:
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
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
    },
]

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sản phẩm hiện tại:")

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
                    f"Tồn kho: {quantity} | "
                    f"Đã bán: {product_list[i]['sold']} | "
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

                product["quantity"] -= quantity_buy
                product["sold"] += quantity_buy

                total_money = quantity_buy * product["price"]

                print("Bán hàng thành công")
                print("Khách cần thanh toán:", total_money)

                break

        if found == False:
            print("Không tìm thấy sản phẩm cần bán")

    elif choice == "3":
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

    elif choice == "4":
        print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")

        total_revenue = 0
        max_sold = 0
        best_seller = ""

        for i in range(len(product_list)):
            revenue = product_list[i]["price"] * product_list[i]["sold"]

            total_revenue += revenue

            print(
                f"{i+1}. {product_list[i]['product_name']} | "
                f"Đã bán: {product_list[i]['sold']} | "
                f"Doanh thu: {revenue}"
            )

            if product_list[i]["sold"] > max_sold:
                max_sold = product_list[i]["sold"]
                best_seller = product_list[i]["product_name"]

        if total_revenue == 0:
            print("Chưa có doanh thu phát sinh.")
        else:
            print("\nTổng doanh thu:", total_revenue)
            print("Sản phẩm bán chạy nhất:", best_seller)

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
