from champions import Warrior, Mage


class ChampionManager:
    """
    Quản lý danh sách quân cờ.
    """

    def __init__(self):
        """Khởi tạo bể tướng mặc định."""
        self.champion_pool = [
            Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
            Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
            Mage("MAG01", "Rikkei Wizard", 800, 500, 1.5),
        ]

    def find_champion(self, champion_id):
        """
        Tìm quân cờ theo mã.
        """
        for champion in self.champion_pool:
            if champion.champion_id.upper() == champion_id.upper():
                return champion
        return None

    def show_champions(self):
        """
        Hiển thị danh sách quân cờ.
        """
        if not self.champion_pool:
            print("Bể tướng đang trống!")
            return

        print("\n--- DANH SÁCH QUÂN CỜ ---")
        print("-" * 90)
        for champion in self.champion_pool:
            print(champion)
        print("-" * 90)

    def add_champion(self):
        """
        Thêm quân cờ mới.
        """
        print("\n1. Warrior")
        print("2. Mage")

        choice = input("Chọn hệ: ")

        champion_id = input("Nhập mã tướng: ").upper()

        if self.find_champion(champion_id):
            print("Lỗi: Mã tướng đã tồn tại!")
            return

        name = input("Nhập tên tướng: ")

        try:
            hp = int(input("Nhập HP: "))
            atk = int(input("Nhập ATK: "))
        except ValueError:
            print("Dữ liệu không hợp lệ!")
            return

        if choice == "1":
            try:
                armor = int(input("Nhập Armor: "))
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                return

            champion = Warrior(champion_id, name, hp, atk, armor)

        elif choice == "2":
            try:
                ap = float(input("Nhập Ability Power: "))
            except ValueError:
                print("Dữ liệu không hợp lệ!")
                return

            champion = Mage(champion_id, name, hp, atk, ap)

        else:
            print("Lựa chọn không hợp lệ!")
            return

        self.champion_pool.append(champion)

        print("\nThêm tướng thành công!")
        print(f"Mã: {champion.champion_id}")
        print(f"Tên: {champion.name}")
        print(f"Chiến lực: {champion.get_combat_power():.0f}")

    def compare_champions(self):
        """
        So sánh hai quân cờ.
        """
        print("\n--- SO SÁNH QUÂN CỜ ---")

        id1 = input("Nhập mã tướng thứ nhất: ").upper()
        id2 = input("Nhập mã tướng thứ hai: ").upper()

        champion1 = self.find_champion(id1)
        champion2 = self.find_champion(id2)

        if champion1 is None:
            print(f"Mã tướng {id1} không hợp lệ!")
            return

        if champion2 is None:
            print(f"Mã tướng {id2} không hợp lệ!")
            return

        print(champion1)
        print(champion2)

        if champion1 > champion2:
            print(f"\n{champion1.name} mạnh hơn {champion2.name}.")
        elif champion2 > champion1:
            print(f"\n{champion2.name} mạnh hơn {champion1.name}.")
        else:
            print("\nHai quân cờ có sức mạnh bằng nhau.")

    def team_power(self):
        """
        Tính tổng chiến lực đội hình.
        """
        ids = input("\nNhập danh sách mã tướng (cách nhau bằng dấu phẩy): ").split(",")

        total = 0

        print("\nĐội hình:")

        for champion_id in ids:
            champion = self.find_champion(champion_id.strip().upper())

            if champion:
                print(champion)
                total += champion
            else:
                print(f"Mã tướng {champion_id.strip()} không hợp lệ, bỏ qua!")

        print(f"\nTổng chiến lực: {total:.0f}")
