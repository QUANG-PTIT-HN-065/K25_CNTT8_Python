"""
PHẦN 1: Phân tích thiết kế
Cấu trúc thư mục
rikkei_dungeon/
├── main.py
├── data/
│   └── players.py
├── utils/
│   ├── __init__.py
│   ├── player_utils.py
│   ├── battle_utils.py
│   └── item_utils.py
└── reports/
    ├── __init__.py
    └── dungeon_report.py

Vai trò các module
- main.py: menu điều hướng.
- data/players.py: lưu dữ liệu người chơi.
- utils/player_utils.py: tìm kiếm người chơi.
- utils/item_utils.py: mở rương, mua vật phẩm.
- utils/battle_utils.py: chiến đấu với quái vật.
- reports/dungeon_report.py: hiển thị danh sách và bảng xếp hạng.

| Hàm                             | Input     | Output   | Module         |
| ------------------------------- | --------- | -------- | -------------- |
| find_player(records, player_id) | list, str | index/-1 | player_utils   |
| display_players(records)        | list      | None     | dungeon_report |
| open_treasure_chest(records)    | list      | None     | item_utils     |
| buy_item(records)               | list      | None     | item_utils     |
| fight_monster(records)          | list      | None     | battle_utils   |
| show_leaderboard(records)       | list      | None     | dungeon_report |
| main()                          | None      | None     | main           |

Pseudocode find_player()
Chuẩn hóa player_id bằng upper()
Duyệt records
Nếu tìm thấy trả về vị trí
Không tìm thấy trả về -1

Pseudocode mua vật phẩm
Nhập mã người chơi
Tìm người chơi
Nhập tên vật phẩm
Kiểm tra có trong shop không
Kiểm tra đủ vàng
Trừ vàng và thêm vật phẩm

Pseudocode chiến đấu
Nhập mã người chơi
Tìm người chơi
Nếu hp <=0 thì dừng
Random quái vật
Trừ hp
Nếu hp >0 cộng vàng thưởng
"""

from data.players import player_records
from utils.item_utils import *
from utils.battle_utils import fight_monster
from reports.dungeon_report import display_players, show_leaderboard

while True:
    print("1. Danh sách")
    print("2. Mở rương")
    print("3. Mua đồ")
    print("4. Chiến đấu")
    print("5. Bảng xếp hạng")
    print("6. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        display_players(player_records)

    elif choice == "2":
        open_treasure_chest(player_records)

    elif choice == "3":
        buy_item(player_records)

    elif choice == "4":
        fight_monster(player_records)

    elif choice == "5":
        show_leaderboard(player_records)

    elif choice == "6":
        print("Cảm ơn bạn đã tham gia Rikkei Dungeon!")
        break
