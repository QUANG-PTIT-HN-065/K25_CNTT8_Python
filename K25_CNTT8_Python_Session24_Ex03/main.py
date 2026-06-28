"""
1) Phân tích và thiết kế giải pháp

Sơ đồ kế thừa

Champion (ABC)
├── Warrior
└── Mage

- Champion là lớp trừu tượng chứa thuộc tính và phương thức chung
- Warrior và Mage kế thừa Champion và cài đặt riêng hàm calculate_skill_damage()

Phân tích đa hình (Polymorphism)

- Các lớp Warrior và Mage cùng sử dụng tên hàm calculate_skill_damage() nhưng mỗi lớp có cách tính sát thương khác nhau
- Khi thêm hệ mới như Assassin hoặc Ranger, chỉ cần kế thừa Champion và ghi đè hàm này, không cần sửa mã nguồn cũ

Phân tích nạp chồng toán tử (__add__)

- Phương thức __add__ cho phép cộng chiến lực của hai quân cờ hoặc cộng với một số (int/float)
- Nhờ đó có thể dùng total += champion để cộng dồn chiến lực đội hình bắt đầu từ 0
"""

from manager import ChampionManager

def main():
    """
    Hàm chính của chương trình.
    """
    manager = ChampionManager()

    while True:
        print("\n========== RIKKEI RPG - AUTO BATTLER ==========")
        print("1. Hiển thị bể tướng")
        print("2. Thêm quân cờ mới")
        print("3. So sánh 2 quân cờ")
        print("4. Tính tổng chiến lực đội hình")
        print("5. Thoát")

        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            manager.show_champions()

        elif choice == "2":
            manager.add_champion()

        elif choice == "3":
            manager.compare_champions()

        elif choice == "4":
            manager.team_power()

        elif choice == "5":
            print("\nCảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
            break

        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()
