number = 1


class Product:
    def __init__(self, id, name, price, quantity_sold, discount):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount
        self.total_revenue = 0
        self.revenue_type = ""

    def calculate_revenue(self):
        self.total_revenue = self.price * self.quantity_sold - self.discount
        return self.total_revenue

    def classify_revenue(self):
        if self.total_revenue < 5000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 20000000:
            self.revenue_type = "Trung Bình"
        elif self.total_revenue < 50000000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"

        return self.revenue_type


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self):
        global number
        print("\n===== THÊM SẢN PHẨM =====")
        id = f"P{number:03d}"

        name = validate_str("Nhập tên sản phẩm: ")
        price = float(validate_number("Nhập giá: "))
        quantity_sold = int(validate_number("Nhập số lượng bán: "))
        discount = float(validate_number("Nhập giảm giá: "))

        product = Product(id, name, price, quantity_sold, discount)

        product.calculate_revenue()
        product.classify_revenue()

        self.products.append(product)

        print("Thêm sản phẩm thành công!")
        number += 1

    def show_all(self):
        if not self.products:
            print("Danh sách sản phẩm trống!")
            return

        print("-" * 110)
        print(
            f"{'ID':<10}"
            f"{'Tên sản phẩm':<25}"
            f"{'Giá':>12}"
            f"{'SL bán':>10}"
            f"{'Giảm giá':>15}"
            f"{'Doanh thu':>18}"
            f"{'Phân loại':>15}"
        )
        print("-" * 110)

        for product in self.products:
            print(
                f"{product.id:<10}"
                f"{product.name:<25}"
                f"{product.price:>12,.0f}"
                f"{product.quantity_sold:>10}"
                f"{product.discount:>15,.0f}"
                f"{product.total_revenue:>18,.0f}"
                f"{product.revenue_type:>15}"
            )

        print("-" * 110)

    def update_product(self):
        pass

    def delete_product(self):
        pass

    def search_product(self):
        if not self.products:
            print("Danh sách sản phẩm trống!")
            return

        keyword = input("Nhập tên hoặc ID cần tìm: ").lower()

        found = False

        print("-" * 110)
        print(
            f"{'ID':<10}"
            f"{'Tên sản phẩm':<25}"
            f"{'Giá':>12}"
            f"{'SL bán':>10}"
            f"{'Giảm giá':>15}"
            f"{'Doanh thu':>18}"
            f"{'Phân loại':>15}"
        )
        print("-" * 110)

        for product in self.products:
            if keyword in product.id.lower() or keyword in product.name.lower():
                found = True
                print(
                    f"{product.id:<10}"
                    f"{product.name:<25}"
                    f"{product.price:>12,.0f}"
                    f"{product.quantity_sold:>10}"
                    f"{product.discount:>15,.0f}"
                    f"{product.total_revenue:>18,.0f}"
                    f"{product.revenue_type:>15}"
                )

        print("-" * 110)

        if not found:
            print("Không tìm thấy sản phẩm!")


def validate_number(message, number_type=float):
    while True:
        try:
            number = number_type(input(message))

            if number < 0:
                print("Không được nhỏ hơn 0!")
                continue

            return number

        except ValueError:
            print("Vui lòng nhập số!")


def validate_str(message):
    while True:
        value = input(message)
        if not value:
            print("không đc để trống:")
            continue
        else:
            return value
