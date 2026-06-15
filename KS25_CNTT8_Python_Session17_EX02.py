# 1) Phân tích và thiết kế

# Cơ chế key trong sort()

# sort() sẽ gọi hàm key cho từng phần tử và dùng giá trị trả về để so sánh
# Nếu key trả về tuple (-rating, price):
# -rating giúp Rating lớn hơn đứng trước (giảm dần)
# Nếu Rating bằng nhau, Python tiếp tục so sánh phần tử thứ hai là price
# price giữ nguyên nên giá nhỏ hơn đứng trước (tăng dần)

# Cơ chế accumulator của reduce()

# reduce() nhận lần lượt từng phần tử trong danh sách
# Biến tích lũy (accumulator) lưu kết quả tạm thời
# Mỗi lần lặp sẽ cộng thêm phần tử mới vào accumulator
# Kết quả cuối cùng là tổng toàn bộ danh sách

import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5",
]


def display_labels():
    print("\n--- DANH SÁCH TEM NHÃN ---")

    for product in product_list:
        try:
            code, name, price, rating = product.split("-")

            if not price.isdigit():
                raise ValueError

            data = {
                "code": f"{code:<10}",
                "name": f"{name:<20}",
                "price": f"{int(price):,}",
                "rating": rating,
            }

            template = "Mã: {code} | Tên: {name} | Giá: {price} VND | Rating: {rating}*"
            print(template.format_map(data))

        except IndexError:
            code = product.split("-")[0]
            print(f"Bỏ qua sản phẩm {code} do sai cấu trúc dữ liệu")

        except ValueError:
            print(f"Dữ liệu giá không hợp lệ: {product}")


def product_key(product):
    try:
        parts = product.split("-")

        if len(parts) < 4:
            raise IndexError

        rating = float(parts[3])
        price = int(parts[2])

        return (-rating, price)

    except (IndexError, ValueError):
        return (float("inf"), float("inf"))


def sort_products():
    product_list.sort(key=product_key)

    print("\n--- SẮP XẾP SẢN PHẨM ---")
    print("Đã sắp xếp thành công! Cập nhật danh sách:")

    for index, product in enumerate(product_list, start=1):
        print(f"{index}. {product}")


def calculate_total():
    prices = []

    for product in product_list:
        try:
            parts = product.split("-")

            if len(parts) < 4:
                raise IndexError

            if not parts[2].isdigit():
                raise ValueError

            prices.append(int(parts[2]))

        except IndexError:
            code = parts[0]
            print(f"Bỏ qua sản phẩm {code} do sai cấu trúc dữ liệu")

        except ValueError:
            print(f"Dữ liệu giá không hợp lệ: {product}")

    total = functools.reduce(lambda acc, x: acc + x, prices, 0)

    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND.")


def main():
    while True:
        print("\n============= E-COMMERCE ANALYTICS =============")
        print("1. Hiển thị tem nhãn sản phẩm (format_map & F-String)")
        print("2. Sắp xếp sản phẩm thông minh (sort key)")
        print("3. Tính tổng giá trị kho hàng (reduce)")
        print("4. Đóng hệ thống")
        print("================================================")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            display_labels()

        elif choice == "2":
            sort_products()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            print("Đóng hệ thống thành công!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


main()
