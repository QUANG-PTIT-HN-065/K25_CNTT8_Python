"""
1) Thiết kế lớp MenuItem
Class Attributes
service_charge = 0.0
Thuộc tính dùng chung cho toàn bộ đồ uống.
Được cập nhật bằng @classmethod.
Instance Attributes
Public
item_id
item_name
Private (Encapsulation)
__base_price
__is_available
__base_price: giá gốc của đồ uống.
__is_available: trạng thái bán.
Không được truy cập trực tiếp từ bên ngoài Class.
Methods
Constructor
__init__(self, item_id, item_name, base_price)

Khởi tạo:

Mã món
Tên món
Giá gốc
Trạng thái mặc định:
self.__is_available = True

(Đang bán)

Getters / Setters
Getter
@property
def base_price(self)
@property
def is_available(self)
Setter
@base_price.setter

Kiểm tra:

price > 0

Nếu không hợp lệ:

Giá đồ uống phải lớn hơn 0!
Giá cũ được giữ nguyên.
Instance Methods
Đảo trạng thái bán
toggle_availability(self)
Có self
Đổi:
True <-> False
Tính giá niêm yết
calculate_selling_price(self)

Công thức:

Giá niêm yết =
Giá gốc + Giá gốc * service_charge
Class Method
@classmethod
update_service_charge(cls, new_rate)
Nhận cls
Cập nhật:
cls.service_charge
Static Method
@staticmethod
is_valid_item_id(item_id)

Kiểm tra:

2 chữ cái in hoa + 2 chữ số

Ví dụ hợp lệ:

CF01
TE99
JU12
"""

import re


class MenuItem:
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name.title()
        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, new_price):
        if new_price > 0:
            self.__base_price = new_price
        else:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")

    @property
    def is_available(self):
        return self.__is_available

    def toggle_availability(self):
        self.__is_available = not self.__is_available

    def calculate_selling_price(self):
        return int(self.__base_price + self.__base_price * MenuItem.service_charge)

    @classmethod
    def update_service_charge(cls, new_rate):
        cls.service_charge = new_rate

    @staticmethod
    def is_valid_item_id(item_id):
        return re.fullmatch(r"[A-Z]{2}\d{2}", item_id) is not None


menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000),
]


def find_item(item_id):
    for item in menu_db:
        if item.item_id == item_id:
            return item
    return None


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
    print("1. Xem thực đơn & Giá niêm yết")
    print("2. Thêm món mới vào menu")
    print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
    print("4. Điều chỉnh giá gốc của món")
    print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
    print("6. Thoát chương trình")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")

        for i, item in enumerate(menu_db, start=1):
            status = "Đang bán" if item.is_available else "Hết hàng"

            print(
                f"{i}. Mã: {item.item_id} | "
                f"Tên: {item.item_name:<15} | "
                f"Trạng thái: {status:<10} | "
                f"Giá niêm yết: "
                f"{item.calculate_selling_price():,} VNĐ"
            )

    elif choice == "2":
        print("\n--- THÊM MÓN MỚI VÀO MENU ---")

        item_id = input("Nhập mã món: ")

        if not MenuItem.is_valid_item_id(item_id):
            print("\nMã món không hợp lệ!")
            print("Mã món phải gồm 2 chữ cái " "in hoa và 2 chữ số.")
            continue

        if find_item(item_id):
            print("\nMã món đã tồn tại!")
            continue

        name = input("Nhập tên món: ")
        price = int(input("Nhập giá gốc: "))

        if price <= 0:
            print("Giá không hợp lệ!")
            continue

        menu_db.append(MenuItem(item_id, name, price))

        print("\nThêm món mới thành công!")

    elif choice == "3":
        print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")

        item_id = input("Nhập mã món cần cập nhật: ")

        item = find_item(item_id)

        if not item:
            print("Không tìm thấy món.")
            continue

        item.toggle_availability()

        if item.is_available:
            print(f">> Đã cập nhật " f"{item.item_name} thành ĐANG BÁN!")
        else:
            print(f">> Đã cập nhật " f"{item.item_name} thành HẾT HÀNG!")

    elif choice == "4":
        print("\n--- ĐIỀU CHỈNH GIÁ GỐC ---")

        item_id = input("Nhập mã món cần đổi giá: ")

        item = find_item(item_id)

        if not item:
            print("Không tìm thấy món.")
            continue

        new_price = int(input("Nhập giá tiền mới: "))

        old_price = item.base_price

        item.base_price = new_price

        if item.base_price != old_price:
            print("Cập nhật giá gốc thành công!")

    elif choice == "5":
        print("\n--- CẬP NHẬT PHỤ PHÍ " "DỊCH VỤ TOÀN HỆ THỐNG ---")

        print(f"Phụ phí hiện tại: " f"{MenuItem.service_charge * 100:.0f}%")

        rate = float(input("Nhập phụ phí mới " "(VD: 0.1): "))

        MenuItem.update_service_charge(rate)

        print("Cập nhật phụ phí dịch vụ " "thành công!")

    elif choice == "6":
        print("\nCảm ơn bạn đã sử dụng " "hệ thống Rikkei Coffee!")
        break

    else:
        print("Lựa chọn không hợp lệ!")
