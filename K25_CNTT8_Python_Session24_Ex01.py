"""
(1) Phân tích lỗi

Câu 1:

Lỗi vì Warrior.__init__() không gọi hàm khởi tạo của lớp cha nên các thuộc tính name, hp, attack_power không được tạo.
Thiếu:
super().__init__(name, hp, attack_power)

Câu 2:
Có thể gọi trực tiếp:

Character.__init__(self, name, hp, attack_power)

Câu 3:

Lỗi:
TypeError
Vì Python không biết cách so sánh hai đối tượng Warrior bằng toán tử > nếu chưa định nghĩa.

Câu 4:
Cần thêm:

__gt__(self, other)
Nhận 2 tham số: self và other.

"""


# Lớp cha
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power


# Lớp con
class Warrior(Character):
    def __init__(self, name, hp, attack_power, bonus_armor):
        super().__init__(name, hp, attack_power)
        self.bonus_armor = bonus_armor

    def get_total_power(self):
        return self.attack_power + self.bonus_armor

    def __gt__(self, other):
        return self.get_total_power() > other.get_total_power()


# Tạo đối tượng
w1 = Warrior("Arthur", 1000, 150, 50)
w2 = Warrior("Lancelot", 900, 180, 10)

print(f"Chiến binh {w1.name} xuất trận!")

if w1 > w2:
    print(f"{w1.name} mạnh hơn {w2.name}!")
else:
    print(f"{w2.name} mạnh hơn hoặc hòa!")
