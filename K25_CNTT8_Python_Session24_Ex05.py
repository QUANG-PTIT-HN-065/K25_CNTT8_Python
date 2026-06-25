"""
===================================================================
TÀI LIỆU THIẾT KẾ LỚP BISTROTABLE
===================================================================

1. Class Attributes (Thuộc tính Lớp):
   - _vat_rate : float
     Ý nghĩa: Thuế suất VAT áp dụng chung cho toàn bộ bàn ăn.

2. Instance Attributes (Thuộc tính Đối tượng):
   Public:
   - capacity : int
     Ý nghĩa: Sức chứa tối đa của bàn.

   Private:
   - __table_id : str
     Ý nghĩa: Mã định danh bàn ăn.

   - __current_bill : int
     Ý nghĩa: Tổng tiền món ăn hiện tại.

3. Methods (Các Phương thức):

   - __init__(self, table_id, capacity)
     Khởi tạo mã bàn, sức chứa.
     Hóa đơn mặc định = 0.

   - @property table_id
     Trả về mã bàn.

   - @property current_bill
     Trả về hóa đơn hiện tại.

   - @property status
     Nếu current_bill == 0:
         "Đang trống"
     Ngược lại:
         "Có khách"

   - @property final_total
     Tính tổng thanh toán gồm VAT.

   - order_dish(self, amount)
     Cộng thêm tiền món ăn.

   - cancel_dish(self, amount)
     Giảm trừ hóa đơn.
     Không được vượt quá hóa đơn hiện tại.

   - checkout(self)
     Thanh toán.
     Reset hóa đơn về 0.

   - @classmethod update_vat_rate(cls, new_rate)
     Cập nhật VAT toàn hệ thống.

   - @staticmethod validate_id(table_id)
     Kiểm tra định dạng mã bàn.
     Phải bắt đầu bằng "TB".
===================================================================
"""


class BistroTable:
    _vat_rate = 0.08

    def __init__(self, table_id, capacity):
        self.__table_id = table_id.upper()
        self.capacity = capacity
        self.__current_bill = 0

    @property
    def table_id(self):
        return self.__table_id

    @property
    def current_bill(self):
        return self.__current_bill

    @property
    def status(self):
        return "Đang trống" if self.__current_bill == 0 else "Có khách"

    @property
    def final_total(self):
        return int(self.__current_bill * (1 + BistroTable._vat_rate))

    def order_dish(self, amount):
        if amount <= 0:
            print("Vui lòng nhập số tiền là một số nguyên dương!")
            return

        self.__current_bill += amount

    def cancel_dish(self, amount):
        if amount <= 0:
            print("Vui lòng nhập số tiền là một số nguyên dương!")
            return False

        if amount > self.__current_bill:
            print("Lỗi: Số tiền giảm trừ vượt quá giá trị hóa đơn hiện tại!")
            return False

        self.__current_bill -= amount
        return True

    def checkout(self):
        if self.__current_bill == 0:
            print("Lỗi: Bàn này hiện đang trống, không có hóa đơn để thanh toán!")
            return False

        print(f"\n--- HÓA ĐƠN THANH TOÁN BÀN {self.__table_id} ---")
        print(f"Số tiền món ăn: {self.__current_bill:,}đ")
        print(f"Thuế suất VAT áp dụng: {BistroTable._vat_rate*100:.0f}%")
        print(f"Tổng tiền cần thanh toán: {self.final_total:,}đ")

        self.__current_bill = 0
        return True

    @classmethod
    def update_vat_rate(cls, new_rate):
        cls._vat_rate = new_rate

    @staticmethod
    def validate_id(table_id):
        table_id = table_id.upper()
        return table_id.startswith("TB") and len(table_id) >= 3


table_records = [BistroTable("TB01", 4), BistroTable("TB02", 2), BistroTable("TB03", 8)]


def find_table(table_id):
    table_id = table_id.upper()

    for table in table_records:
        if table.table_id == table_id:
            return table

    return None


def main():
    while True:
        print("\n===== HỆ THỐNG ĐIỀU PHỐI BÀN ĂN - RIKKEI BISTRO =====")
        print("1. Hiển thị sơ đồ & Trạng thái bàn ăn")
        print("2. Gọi món mới")
        print("3. Hủy món / Giảm trừ hóa đơn")
        print("4. Cập nhật thuế suất VAT")
        print("5. Thanh toán hóa đơn")
        print("6. Thoát chương trình")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            print("\n--- SƠ ĐỒ BÀN ĂN RIKKEI BISTRO ---")

            for i, table in enumerate(table_records, start=1):
                print(
                    f"{i}. Mã bàn: {table.table_id} | "
                    f"Sức chứa: {table.capacity} người | "
                    f"Tạm tính: {table.current_bill:,}đ | "
                    f"Trạng thái: {table.status}"
                )

        elif choice == "2":
            print("\n--- GỌI MÓN MỚI ---")

            table_id = input("Nhập mã bàn gọi món: ").upper()

            if not BistroTable.validate_id(table_id):
                print("Mã bàn không hợp lệ!")
                continue

            table = find_table(table_id)

            if not table:
                print("Không tìm thấy bàn!")
                continue

            try:
                amount = int(input("Nhập giá tiền món ăn mới: "))
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
                continue

            table.order_dish(amount)

            print(
                f">> Thành công: Đã ghi nhận món ăn "
                f"{amount:,}đ vào Bàn '{table.table_id}'."
            )

            print(f">> Số tiền tạm tính hiện tại: " f"{table.current_bill:,}đ.")

        elif choice == "3":
            print("\n--- HỦY MÓN / GIẢM TRỪ HÓA ĐƠN ---")

            table_id = input("Nhập mã bàn: ").upper()

            table = find_table(table_id)

            if not table:
                print("Không tìm thấy bàn!")
                continue

            try:
                amount = int(input("Nhập số tiền giảm trừ: "))
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
                continue

            if table.cancel_dish(amount):
                print(
                    f">> Thành công: Đã giảm trừ "
                    f"{amount:,}đ khỏi Bàn '{table.table_id}'."
                )

                print(f">> Số tiền tạm tính còn lại: " f"{table.current_bill:,}đ.")

                if table.status == "Đang trống":
                    print(
                        f">> Bàn '{table.table_id}' hiện đã chuyển "
                        f"về trạng thái Đang trống."
                    )

        elif choice == "4":
            print("\n--- CẬP NHẬT THUẾ SUẤT VAT ---")

            print(f"VAT hiện tại: " f"{BistroTable._vat_rate*100:.0f}%")

            try:
                new_rate = float(input("Nhập VAT mới: "))
            except ValueError:
                print("Tỷ lệ thuế không hợp lệ!")
                continue

            if not (0 <= new_rate <= 0.2):
                print("Tỷ lệ thuế không hợp lệ!")
                continue

            BistroTable.update_vat_rate(new_rate)

            print(f">> Cập nhật VAT " f"{new_rate*100:.0f}% thành công!")

        elif choice == "5":
            print("\n--- THANH TOÁN HÓA ĐƠN ---")

            table_id = input("Nhập mã bàn: ").upper()

            table = find_table(table_id)

            if not table:
                print("Không tìm thấy bàn!")
                continue

            if table.checkout():
                print(
                    f">> Thanh toán thành công! "
                    f"Bàn '{table.table_id}' đã được dọn sạch."
                )

        elif choice == "6":
            print("\nCảm ơn bạn đã sử dụng hệ thống " "điều phối bàn ăn Rikkei Bistro!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
