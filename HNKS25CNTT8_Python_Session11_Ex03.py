# 1) Phân tích và thiết kế giải pháp

# Input
# Lựa chọn menu: int
# Mã sản phẩm: str
# Tên sản phẩm: str
# Giá sản phẩm: int
# Số lượng sản phẩm: int

# Output
# Danh sách sản phẩm
# Thông báo thêm, cập nhật, xóa thành công
# Thông báo lỗi khi dữ liệu không hợp lệ

# Giải pháp
# Sử dụng list để lưu danh sách sản phẩm
# Mỗi sản phẩm là một dictionary
# Chuẩn hóa mã sản phẩm bằng:
# strip()
# upper()
# Kiểm tra trùng mã bằng vòng lặp
# Kiểm tra giá và số lượng:
# Phải chuyển được sang int
# Phải lớn hơn 0
# Xóa sản phẩm bằng remove()
# Cập nhật dữ liệu bằng cách gán lại giá trị cho key tương ứng

# Pseudocode
# Lặp vô hạn:
#     Hiển thị menu
#     Nhập lựa chọn
#     Nếu lựa chọn = 1:
#         Hiển thị danh sách sản phẩm
#     Nếu lựa chọn = 2:
#         Nhập thông tin sản phẩm
#         Chuẩn hóa mã
#         Kiểm tra trùng mã
#         Kiểm tra giá và số lượng hợp lệ
#         Thêm vào danh sách
#     Nếu lựa chọn = 3:
#         Nhập mã sản phẩm
#         Chuẩn hóa mã
#         Tìm sản phẩm
#         Nếu tìm thấy:
#             Cập nhật thông tin
#         Ngược lại:
#             Thông báo không tìm thấy
#     Nếu lựa chọn = 4:
#         Nhập mã sản phẩm
#         Chuẩn hóa mã
#         Tìm sản phẩm
#         Nếu tìm thấy:
#             Xóa sản phẩm
#         Ngược lại:
#             Thông báo không tìm thấy
#     Nếu lựa chọn = 5:
#         Thoát chương trình
#     Ngược lại:
#         Thông báo lựa chọn không hợp lệ

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            for i in range(len(product_list)):
                print(
                    f"{i+1}. Mã SP: {product_list[i]['product_id']} | "
                    f"Tên: {product_list[i]['product_name']} | "
                    f"Giá: {product_list[i]['price']} | "
                    f"Số lượng: {product_list[i]['quantity']}"
                )

    elif choice == "2":
        product_id = input("Nhập mã sản phẩm: ").strip().upper()

        is_duplicate = False
        for product in product_list:
            if product["product_id"] == product_id:
                is_duplicate = True

        if is_duplicate:
            print("Mã sản phẩm bị trùng")
            continue

        product_name = input("Nhập tên sản phẩm: ")
        price = input("Nhập giá sản phẩm: ")
        quantity = input("Nhập số lượng sản phẩm: ")

        if not price.isdigit() or not quantity.isdigit():
            print("Giá/Số lượng không hợp lệ")
            continue

        if int(price) <= 0 or int(quantity) <= 0:
            print("Giá/Số lượng không hợp lệ")
            continue

        product_list.append({
            "product_id": product_id,
            "product_name": product_name,
            "price": int(price),
            "quantity": int(quantity)
        })

        print("Thêm sản phẩm thành công")

    elif choice == "3":
        product_id = input(
            "Nhập mã sản phẩm cần cập nhật: "
        ).strip().upper()

        found = False

        for product in product_list:
            if product["product_id"] == product_id:
                found = True

                product_name = input("Nhập tên mới: ")
                price = input("Nhập giá mới: ")
                quantity = input("Nhập số lượng mới: ")

                if not price.isdigit() or not quantity.isdigit():
                    print("Giá/Số lượng không hợp lệ")
                    break

                if int(price) <= 0 or int(quantity) <= 0:
                    print("Giá/Số lượng không hợp lệ")
                    break

                product["product_name"] = product_name
                product["price"] = int(price)
                product["quantity"] = int(quantity)

                print("Cập nhật sản phẩm thành công")
                break

        if found == False:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")

    elif choice == "4":
        product_id = input(
            "Nhập mã sản phẩm cần xóa: "
        ).strip().upper()

        found = False

        for product in product_list:
            if product["product_id"] == product_id:
                product_list.remove(product)
                found = True
                print("Xóa sản phẩm thành công")
                break

        if found == False:
            print("Không tìm thấy mã sản phẩm cần xoá!")

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")