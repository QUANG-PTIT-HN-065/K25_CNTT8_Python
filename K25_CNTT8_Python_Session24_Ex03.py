"""
1) Phân tích thiết kế
Câu 1

point_value_vnd là Class Attribute vì toàn bộ hệ thống dùng chung một tỷ giá quy đổi điểm.

Nếu khai báo trong __init__:

self.point_value_vnd = 1000

thì mỗi thẻ sẽ có một bản sao riêng. Khi cập nhật tỷ giá ở chức năng 5, phải sửa từng object, rất khó đồng bộ.

Câu 2

is_valid_card_id() chỉ kiểm tra định dạng chuỗi mã thẻ, không sử dụng dữ liệu của object (self) hay class (cls).

Vì vậy nên dùng:

@staticmethod

Có thể gọi trực tiếp:

MemberCard.is_valid_card_id("RC01")

không cần tạo object trước.

Câu 3

Đóng gói bằng:

self.__points

giúp ngăn việc sửa điểm trực tiếp:

card.__points = 1000

Điểm chỉ được thay đổi thông qua:

earn_points()
redeem_points()

=> tránh gian lận điểm và bảo vệ dữ liệu.
"""

import re


class MemberCard:
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()
        self.__points = 0
        self.__tier = "Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    def earn_points(self, bill_amount):
        earned = bill_amount // 10000
        self.__points += earned

        upgraded = False
        if self.__points >= 100 and self.__tier != "VIP":
            self.__tier = "VIP"
            upgraded = True

        return earned, upgraded

    def redeem_points(self, points_to_use):
        if points_to_use <= 0 or points_to_use > self.__points:
            return False, 0

        self.__points -= points_to_use
        discount = points_to_use * MemberCard.point_value_vnd
        return True, discount

    @classmethod
    def update_point_value(cls, new_value):
        cls.point_value_vnd = new_value

    @staticmethod
    def is_valid_card_id(card_id):
        return re.fullmatch(r"RC\d{2}", card_id) is not None


cards_database = [MemberCard("RC01", "Nguyen Van A"), MemberCard("RC02", "Tran Thi B")]

cards_database[0].earn_points(1500000)
cards_database[1].earn_points(200000)


def find_card(card_id):
    for card in cards_database:
        if card.card_id == card_id:
            return card
    return None


while True:
    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm")
    print("6. Thoát chương trình")
    print("================================================")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")

        if not cards_database:
            print("Chưa có dữ liệu.")
        else:
            for i, card in enumerate(cards_database, 1):
                print(
                    f"{i}. Mã: {card.card_id} | "
                    f"Tên: {card.name:<20} | "
                    f"Điểm: {card.points:<4} | "
                    f"Hạng: {card.tier}"
                )

    elif choice == "2":
        print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")

        card_id = input("Nhập mã thẻ: ").strip()

        if not MemberCard.is_valid_card_id(card_id):
            print("Mã thẻ không hợp lệ!")
            continue

        if find_card(card_id):
            print("\nMã thẻ đã tồn tại trong hệ thống!")
            print("Vui lòng kiểm tra lại.")
            continue

        name = input("Nhập tên khách hàng: ")

        card = MemberCard(card_id, name)
        cards_database.append(card)

        print("\nĐăng ký thẻ thành viên thành công!")
        print(f"Mã thẻ: {card.card_id}")
        print(f"Tên khách hàng: {card.name}")
        print(f"Điểm ban đầu: {card.points}")
        print(f"Hạng thẻ: {card.tier}")

    elif choice == "3":
        print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")

        card_id = input("Nhập mã thẻ: ")
        card = find_card(card_id)

        if not card:
            print("Không tìm thấy thẻ.")
            continue

        bill = int(input("Nhập tổng tiền hóa đơn: "))

        earned, upgraded = card.earn_points(bill)

        print(f"\nKhách hàng: {card.name}")
        print(f"Hóa đơn: {bill:,} VNĐ")
        print(f"Số điểm được tích: {earned}")
        print(f"Tổng điểm hiện tại: {card.points}")

        if upgraded:
            print("\nChúc mừng! Khách hàng đã được nâng hạng lên VIP.")

        print(f"Hạng thẻ hiện tại: {card.tier}")

    elif choice == "4":
        print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")

        card_id = input("Nhập mã thẻ: ")
        card = find_card(card_id)

        if not card:
            print("Không tìm thấy thẻ.")
            continue

        use_points = int(input("Nhập số điểm muốn sử dụng: "))

        success, discount = card.redeem_points(use_points)

        if success:
            print(f"\nĐã trừ {use_points} điểm.")
            print(f"Khách hàng được giảm giá " f"{discount:,} VNĐ vào hóa đơn!")
            print(f"Số điểm còn lại: {card.points}")
            print(f"Hạng thẻ hiện tại: {card.tier}")
        else:
            print("\nKhông thể đổi điểm!")
            print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
            print(f"Điểm hiện tại của khách: {card.points}")
            print("Điểm cũ được giữ nguyên.")
            print(f"Số điểm sau giao dịch: {card.points}")

    elif choice == "5":
        print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")

        print(f"Tỷ giá hiện tại: " f"1 điểm = {MemberCard.point_value_vnd:,} VNĐ")

        new_value = int(input("Nhập tỷ giá mới cho 1 điểm: "))

        MemberCard.update_point_value(new_value)

        print("\nCập nhật tỷ giá thành công!")
        print(f"Tỷ giá mới: " f"1 điểm = {MemberCard.point_value_vnd:,} VNĐ")

    elif choice == "6":
        print("\nCảm ơn bạn đã sử dụng hệ thống " "thẻ thành viên Rikkei Coffee!")
        break

    else:
        print("Lựa chọn không hợp lệ!")
