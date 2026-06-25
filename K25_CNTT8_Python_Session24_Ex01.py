"""
1) Phân tích lỗi

Câu 1:
order_table1.total_amount = 0 vi phạm tính Đóng gói (Encapsulation).

Câu 2:
Đổi:

self.total_amount

thành:

self.__total_amount

để kích hoạt Name Mangling.

Câu 3:
Dùng decorator:

@property

để chỉ cho phép đọc.

Câu 4:
Dòng:

self.vat_rate = new_rate

không sửa biến class mà tạo ra biến instance vat_rate riêng cho đối tượng hiện tại.

Câu 5:
Dùng:

@classmethod

và thay self bằng:

cls

"""

class CoffeeOrder:
    vat_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0

    def add_item(self, price):
        if price > 0:
            self.__total_amount += price

    @property
    def total_amount(self):
        return self.__total_amount

    def calculate_final_bill(self):
        return self.__total_amount * (1 + CoffeeOrder.vat_rate)

    @classmethod
    def update_vat_rate(cls, new_rate):
        cls.vat_rate = new_rate


# Test
order1 = CoffeeOrder("Bàn 1")
order2 = CoffeeOrder("Bàn 2")

order1.add_item(50000)
order2.add_item(30000)

# Không thể sửa trực tiếp __total_amount
order1.total_amount = 0  # lỗi

CoffeeOrder.update_vat_rate(0.08)

print("Tiền bàn 1:", order1.total_amount)
print("VAT bàn 1:", order1.vat_rate)
print("VAT bàn 2:", order2.vat_rate)
