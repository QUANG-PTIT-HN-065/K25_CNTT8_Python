"""
# (1) Phân tích Thiết kế Hệ thống

1. Abstract Base Class

 Equipment là lớp trừu tượng chứa các thuộc tính và phương thức chung của mọi trang bị.
 @abstractmethod bắt buộc các lớp con (như Weapon, MagicSword, Bow) phải tự cài đặt calculate_total_damage(), tránh quên định nghĩa công thức tính sát thương.

2. Multiple Inheritance & MRO

 Thứ tự MRO của MagicSword:


MagicSword -> Weapon -> MagicMixin -> Equipment -> ABC -> object

 Trong __init__(), gọi Weapon.__init__() để khởi tạo thông tin vũ khí và MagicMixin.__init__() để khởi tạo magic_power.

3. Polymorphism

 Khi duyệt inventory, chỉ cần gọi item.calculate_total_damage().
 Mỗi loại vũ khí sẽ tự tính sát thương theo công thức riêng mà không cần dùng if/else.

4. Operator Overloading (__add__)

Pseudocode:


Nhận tham số other

Nếu other là Equipment:
    Tạo Weapon mới
    base_damage = tổng base_damage
    upgrade_level = tổng upgrade_level
    Trả về Weapon mới

Ngược lại:
    Thông báo chỉ có thể dung hợp giữa các trang bị


 Tham số: other (đối tượng Equipment).
 Giá trị trả về: một đối tượng Weapon mới sau khi dung hợp.


"""

from manager import BlacksmithManager


def main():
    """
    Hàm chính điều khiển chương trình.
    """
    manager = BlacksmithManager()

    while True:
        print("\n===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS =====")
        print("1. Xem kho vũ khí & Sát thương tổng")
        print("2. Rèn Vũ khí Vật lý")
        print("3. Rèn Kiếm Ma Thuật")
        print("4. Thẩm định vũ khí")
        print("5. Dung hợp vũ khí")
        print("6. Thoát game")
        print("========================================")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            manager.show_inventory()

        elif choice == "2":
            manager.forge_weapon()

        elif choice == "3":
            manager.forge_magic_sword()

        elif choice == "4":
            manager.compare_weapon()

        elif choice == "5":
            manager.fusion_weapon()

        elif choice == "6":
            print("\nThoát Lò Rèn. Hẹn gặp lại Anh hùng!")
            break

        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()
