# Phân tích và thiết kế
# Input
# | Dữ liệu             | Kiểu |
# | ------------------- | ---- |
# | menu_choice         | int  |
# | shop_name           | str  |
# | product_name        | str  |
# | product_description | str  |
# | category_name       | str  |
# | keywords            | str  |
# | discount_code       | str  |
# | find_keyword        | str  |
# | replace_keyword     | str  |

#  Output
# Thông tin sản phẩm đã chuẩn hóa.
# Thống kê mô tả sản phẩm.
# Tên shop đã chuẩn hóa.
# Kết quả kiểm tra mã giảm giá.
# Kết quả tìm kiếm và thay thế từ khóa.
# Giải pháp

# Sử dụng các hàm xử lý chuỗi:

# strip() -> loại bỏ khoảng trắng đầu cuối.
# title() -> viết hoa chữ cái đầu mỗi từ.
# lower() -> chuyển thành chữ thường.
# upper() -> chuyển thành chữ hoa.
# split() -> tách chuỗi.
# replace() -> thay thế chuỗi.
# startswith() -> kiểm tra tiền tố.
# isalnum() -> kiểm tra chỉ chứa chữ và số.

# Kiểm tra dữ liệu:

# Tên shop không được rỗng.
# Mô tả sản phẩm không được rỗng.
# Mã giảm giá phải đúng định dạng.
# Menu phải từ 1-5 và là số nguyên.
# Pseudocode
# Khai báo product_description = ""

# Lặp vô hạn:
#     Hiển thị menu

#     Nhập lựa chọn

#     Nếu nhập sai kiểu dữ liệu:
#         Báo lỗi
#         Tiếp tục

#     Nếu ngoài khoảng 1-5:
#         Báo lỗi
#         Tiếp tục

#     Nếu chọn 1:
#         Nhập dữ liệu sản phẩm
#         Kiểm tra tên shop
#         Kiểm tra mô tả
#         Hiển thị thống kê

#     Nếu chọn 2:
#         Chuẩn hóa tên shop

#     Nếu chọn 3:
#         Kiểm tra mã giảm giá

#     Nếu chọn 4:
#         Tìm kiếm và thay thế từ khóa

#     Nếu chọn 5:
#         Thoát chương trình
#         Kết thúc

# Lưu dữ liệu dùng chung cho chương trình
product_description = ""
keyword_list = []


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPEE =====")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên shop")
    print("3. Kiểm tra mã giảm giá hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm")
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
        shop_name = input("Nhập tên shop: ")

        if shop_name.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        product_name = input("Nhập tên sản phẩm: ")
        product_description = input("Nhập mô tả sản phẩm: ")
        if product_description.strip() == "":
            print("Mô tả sản phẩm không được rỗng")
            continue

        category_name = input("Nhập danh mục sản phẩm: ")

        keywords = input("Nhập danh sách từ khóa (cách nhau bởi dấu phẩy): ")

        keyword_list = [
            item.strip() for item in keywords.split(",") if item.strip() != ""
        ]

        print("\n===== BÁO CÁO THỐNG KÊ =====")
        print("Tên shop:", shop_name.strip())
        print("Tên sản phẩm:", product_name.strip().title())
        print("Mô tả sản phẩm:", product_description.strip())
        print("Độ dài mô tả:", len(product_description.strip()))
        print("Danh mục:", category_name.strip().lower())
        print("Danh sách từ khóa:", keyword_list)
        print("Số lượng từ khóa:", len(keyword_list))
        print("Mô tả chữ thường:")
        print(product_description.strip().lower())
        print("Mô tả chữ hoa:")
        print(product_description.strip().upper())

    # Chức năng 2
    elif menu_choice == 2:
        shop_name = input("Nhập tên shop: ")

        if shop_name.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        shop_normalized = shop_name.strip().lower()

        shop_normalized = "-".join(shop_normalized.split())

        if not shop_normalized.startswith("shop-"):
            shop_normalized = "shop-" + shop_normalized

        print("Tên shop ban đầu:", shop_name)
        print("Tên shop chuẩn hóa:", shop_normalized)

    # Chức năng 3
    elif menu_choice == 3:
        discount_code = input("Nhập mã giảm giá: ")
        if discount_code == "":
            print("Mã giảm giá không được rỗng")
        elif " " in discount_code:
            print("Mã giảm giá không được chứa khoảng trắng")
        elif len(discount_code) < 6 or len(discount_code) > 12:
            print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
        elif discount_code != discount_code.upper():
            print("Mã giảm giá phải được viết hoa toàn bộ")
        elif not discount_code.isalnum():
            print("Mã giảm giá chỉ được chứa chữ cái và chữ số")
        elif not discount_code.startswith("SALE"):
            print("Mã giảm giá phải bắt đầu bằng SALE")
        else:
            print("Mã giảm giá hợp lệ")

    # Chức năng 4
    elif menu_choice == 4:
        if product_description.strip() == "":
            print("Chưa có mô tả sản phẩm để xử lý")
            continue
        find_keyword = input("Nhập từ khóa cần tìm: ")
        replace_keyword = input("Nhập từ khóa thay thế: ")
        count_keyword = product_description.count(find_keyword)
        if count_keyword > 0:
            new_description = product_description.replace(find_keyword, replace_keyword)
            print(f"Số lần xuất hiện của từ khóa: {count_keyword}")
            print("Mô tả sau khi thay thế:")
            print(new_description)

            product_description = new_description
        else:
            print("Không tìm thấy từ khóa trong mô tả sản phẩm")

    # Chức năng 5
    else:
        print("Thoát chương trình")
        break
