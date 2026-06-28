"""
1) Phân tích lỗi

Câu 1:
Vòng lặp:

for hero in team_heroes:
    hero.use_ultimate()

thể hiện tính đa hình vì mọi đối tượng đều gọi use_ultimate(), mỗi lớp tự thực hiện theo cách riêng.

Câu 2:

Lỗi NotImplementedError xảy ra khi chạy:
hero.use_ultimate()

đến đối tượng Assassin.

Báo lỗi muộn vì game chỉ crash khi đang giao tranh.

Câu 3:
Nếu dùng ABC và @abstractmethod, lỗi xảy ra ngay khi tạo đối tượng Assassin() (lúc loading trận đấu).

Câu 4:
Fail Fast: Phát hiện và báo lỗi ngay khi khởi tạo đối tượng, không đợi đến lúc chương trình đang chạy.
"""

from abc import ABC, abstractmethod


# Lớp cha
class Hero(ABC):
    @abstractmethod
    def use_ultimate(self):
        pass


# Lớp con 1
class Mage(Hero):
    def use_ultimate(self):
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")


# Lớp con 2
class Assassin(Hero):
    def use_ultimate(self):
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


print("--- LOADING TRẬN ĐẤU ---")
team_heroes = [Mage(), Assassin()]
print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")
for hero in team_heroes:
    hero.use_ultimate()
