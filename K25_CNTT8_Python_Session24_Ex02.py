"""
1) Phân tích lỗi

Câu 1:
Nếu points là public, người dùng có thể gán giá trị âm hoặc chuỗi ⇒ dữ liệu sai lệch, các phép tính cộng/trừ điểm có thể lỗi hoặc crash chương trình.

Câu 2:
Dùng:

@property

và:

@points.setter

để kiểm tra dữ liệu trước khi gán.

Câu 3:
is_eligible_for_voucher() không sử dụng bất kỳ thuộc tính nào của đối tượng (self), nên truyền self là dư thừa và làm hàm phụ thuộc vào object một cách không cần thiết.

Câu 4:
Dùng:

@staticmethod

Khác với @classmethod:
| Decorator     | Tham số đầu tiên | Truy cập Class |
| ------------- | ---------------- | -------------- |
| @staticmethod | Không có         | Không          |
| @classmethod  | cls              | Có             |

"""


class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print("Dữ liệu điểm không hợp lệ!")

    def add_points(self, amount):
        if amount > 0:
            self.__points += amount

    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000


card1 = MemberCard("Le Van C", 100)

card1.points = -50  # bị từ chối

result = MemberCard.is_eligible_for_voucher(250000)

print(f"Khách hàng: {card1.customer_name} | Điểm hiện tại: {card1.points}")
print(f"Hóa đơn 250k có được tặng Voucher không? {result}")
