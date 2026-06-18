# 1) Phân tích lỗi

# 1. Lỗi IndexError: tuple index out of range

# Levi = ("Levi", 120, 2500) có 3 phần tử nên p[2] hợp lệ.
# SofM = ("SofM", 150) chỉ có 2 phần tử nên p[2] không tồn tại ⇒ IndexError.

# 2. Nếu sửa SofM thành ( "SofM", 150, 2800 )

# Chương trình sập ở:

# b = (m * 10) + (int(r) * 0.5)

# Lỗi:

# ValueError

# Vì:

# int("N/A")

# không chuyển được sang số.

# 3. Ý nghĩa của

# print("Đang xử lý:", p)
# Xác định bản ghi nào gây lỗi trước khi chương trình sập.

# 4. Đổi tên biến

# | Cũ | Mới            |
# | -- | -------------- |
# | ds | player_records |
# | p  | record         |
# | t  | name           |
# | m  | matches        |
# | r  | mmr            |
# | b  | bonus          |


player_records = [("Levi", 120, 2500), ("SofM", 150), ("Optimus", 100, "N/A")]


def calculate_bonus(matches, mmr):
    return (matches * 10) + (mmr * 0.5)


def process_players(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:
        name = record[0]

        try:
            matches = record[1]
            mmr = int(record[2])

            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus} RP")

        except IndexError:
            print(f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue

        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue


process_players(player_records)
