from equipment import Weapon, MagicSword


class BlacksmithManager:
    """
    Quản lý kho vũ khí.
    """

    def __init__(self):
        self.inventory = []

    def show_inventory(self):
        """
        Hiển thị kho vũ khí.
        """
        print("\n--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---")

        if not self.inventory:
            print("Kho vũ khí hiện đang trống.")
            print("Vui lòng rèn vũ khí bằng Chức năng 2 hoặc Chức năng 3.")
            return

        print("-" * 80)

        for i, item in enumerate(self.inventory, start=1):
            print(
                f"{i}. {item.name} | "
                f"{type(item).__name__} | "
                f"Cấp: {item.upgrade_level} | "
                f"Sát thương: {item.calculate_total_damage()}"
            )

    def forge_weapon(self):
        """
        Tạo Weapon.
        """
        print("\n--- RÈN VŨ KHÍ VẬT LÝ ---")

        name = input("Nhập tên vũ khí: ").title()

        try:
            base_damage = int(input("Nhập sát thương gốc: "))
            if base_damage <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

            level = int(input("Nhập cấp cường hóa: "))
            if level <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

        except ValueError:
            print("Dữ liệu không hợp lệ!")
            return

        weapon = Weapon(name, base_damage, level)
        self.inventory.append(weapon)

        print("\n>> Rèn vũ khí vật lý thành công!")
        print(f"Tên: {weapon.name}")
        print(f"Loại: Weapon")
        print(f"Cấp: {weapon.upgrade_level}")
        print(f"Sát thương tổng: {weapon.calculate_total_damage()}")

    def forge_magic_sword(self):
        """
        Tạo MagicSword.
        """
        print("\n--- RÈN KIẾM MA THUẬT ---")

        name = input("Nhập tên kiếm: ").title()

        try:
            base_damage = int(input("Nhập sát thương gốc: "))
            if base_damage <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

            level = int(input("Nhập cấp cường hóa: "))
            if level <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

            magic = int(input("Nhập sức mạnh phép thuật: "))
            if magic <= 0:
                print("Giá trị phải lớn hơn 0!")
                return

        except ValueError:
            print("Dữ liệu không hợp lệ!")
            return

        sword = MagicSword(name, base_damage, level, magic)
        self.inventory.append(sword)

        print("\n>> Rèn kiếm ma thuật thành công!")
        print(f"Tên: {sword.name}")
        print(f"Loại: MagicSword")
        print(f"Cấp: {sword.upgrade_level}")
        print(f"Sát thương gốc: {sword.base_damage}")
        print(f"Sức mạnh phép thuật: {sword.magic_power}")
        print(f"Sát thương tổng: {sword.calculate_total_damage()}")

    def compare_weapon(self):
        """
        So sánh hai vũ khí đầu tiên.
        """
        print("\n--- THẨM ĐỊNH VŨ KHÍ ---")

        if len(self.inventory) < 2:
            print("Cần ít nhất 2 vũ khí trong kho để thẩm định!")
            return

        w1 = self.inventory[0]
        w2 = self.inventory[1]

        print(
            f"Vũ khí thứ nhất:\n"
            f"{w1.name} | {type(w1).__name__} | "
            f"Sát thương: {w1.calculate_total_damage()}"
        )

        print(
            f"\nVũ khí thứ hai:\n"
            f"{w2.name} | {type(w2).__name__} | "
            f"Sát thương: {w2.calculate_total_damage()}"
        )

        if w1 > w2:
            print(f"\nKết quả: {w1.name} mạnh hơn {w2.name}.")
        elif w2 > w1:
            print(f"\nKết quả: {w2.name} mạnh hơn {w1.name}.")
        else:
            print("\nKết quả: Hai vũ khí có sức mạnh ngang nhau.")

    def fusion_weapon(self):
        """
        Dung hợp hai vũ khí đầu tiên.
        """
        print("\n--- DUNG HỢP VŨ KHÍ ---")

        if len(self.inventory) < 2:
            print("Cần ít nhất 2 vũ khí trong kho để dung hợp!")
            return

        w1 = self.inventory.pop(0)
        w2 = self.inventory.pop(0)

        print("Đang dung hợp 2 vũ khí đầu tiên trong kho...")

        print(
            f"\nVũ khí 1: {w1.name} | "
            f"Cấp: {w1.upgrade_level} | "
            f"Sát thương: {w1.calculate_total_damage()}"
        )

        print(
            f"Vũ khí 2: {w2.name} | "
            f"Cấp: {w2.upgrade_level} | "
            f"Base damage: {w2.base_damage}"
        )

        new_weapon = w1 + w2

        self.inventory.append(new_weapon)

        print("\n>> Dung hợp vũ khí thành công!")
        print(f"Đã xóa: {w1.name}")
        print(f"Đã xóa: {w2.name}")

        print(f"\nVũ khí mới: {new_weapon.name}")
        print("Loại: Weapon")
        print(f"Cấp cường hóa: {new_weapon.upgrade_level}")
        print(f"Sát thương tổng: {new_weapon.calculate_total_damage()}")
