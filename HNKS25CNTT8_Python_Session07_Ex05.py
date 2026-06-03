# 1 Phân tích và thiết kế

# Input
# choice: int
# serial_suffix: str
# raw_batch: str

# Output
# Chuỗi dữ liệu gốc
# Báo cáo kiểm kê sản phẩm
# Kết quả tra cứu serial
# Thông báo lỗi khi nhập sai
# Giải pháp
# split(";") -> tách từng sản phẩm
# strip() -> xóa khoảng trắng
# upper() -> chuẩn hóa mã
# split("-") -> tách thành 4 phần
# isdigit() -> kiểm tra serial hợp lệ
# Dùng try-except xử lý menu

# Pseudocode
# Lặp vô hạn
#     Hiển thị menu

#     Nhập lựa chọn

#     Nếu không hợp lệ
#         Báo lỗi

#     Nếu chọn 1
#         In dữ liệu gốc

#     Nếu chọn 2
#         Tách và chuẩn hóa dữ liệu
#         Kiểm tra serial
#         In báo cáo
#         In tổng kết

#     Nếu chọn 3
#         Nhập đuôi serial
#         Tìm sản phẩm phù hợp
#         In kết quả

#     Nếu chọn 4
#         Thoát chương trình

raw_batch = (
    " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "
)


def get_product_list():
    product_list = []

    for product in raw_batch.split(";"):
        product = product.strip().upper()

        parts = product.split("-")

        product_code = parts[0]
        country = parts[1]
        year = "20" + parts[2]
        serial = parts[3]

        if serial.isdigit():
            status = "Pass"
        else:
            status = "Lỗi Serial - Reject"

        product_list.append(
            {
                "code": product_code,
                "country": country,
                "year": year,
                "serial": serial,
                "status": status,
            }
        )

    return product_list


while True:
    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")

    try:
        choice = int(input("Nhập lựa chọn của bạn (1-4): "))

        if choice < 1 or choice > 4:
            print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
            continue

    except ValueError:
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
        continue

    if choice == 1:
        print(raw_batch)

    elif choice == 2:
        product_list = get_product_list()

        valid_count = 0

        print(
            f"\n{'MÃ SP':<10}"
            f"{'XUẤT XỨ':<10}"
            f"{'NĂM SX':<10}"
            f"{'SERIAL':<10}"
            f"{'TRẠNG THÁI'}"
        )

        for product in product_list:
            print(
                f"{product['code']:<10}"
                f"{product['country']:<10}"
                f"{product['year']:<10}"
                f"{product['serial']:<10}"
                f"{product['status']}"
            )

            if product["status"] == "Pass":
                valid_count += 1

        print(
            f"\nĐã giải mã thành công {valid_count} sản phẩm hợp lệ / Tổng số {len(product_list)} sản phẩm."
        )

    elif choice == 3:
        serial_suffix = input("Nhập 2 số cuối của Serial: ").strip()

        product_list = get_product_list()

        found = False

        for product in product_list:
            if product["serial"][-2:] == serial_suffix:
                print("\nThông tin sản phẩm:")
                print("Mã SP:", product["code"])
                print("Xuất xứ:", product["country"])
                print("Năm SX:", product["year"])
                print("Serial:", product["serial"])
                print("Trạng thái:", product["status"])
                found = True

        if not found:
            print("Không tìm thấy sản phẩm phù hợp")

    else:
        print("Đóng ca kiểm kho. Chào tạm biệt!")
        break
