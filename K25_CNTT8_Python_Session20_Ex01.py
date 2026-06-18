# 1) Phân tích lỗi

# 1. ZeroDivisionError: division by zero

# Do deaths = 0
# Công thức (kills + assists) / deaths
# Chia cho 0 ⇒ ZeroDivisionError

# 2. Nếu bỏ ShowMaker, Chovy gây lỗi gì?

# ValueError
# Vì int("ba") không chuyển được sang số.

# 3. Đổi tên biến theo Clean Code
# | Cũ | Mới          |
# | -- | ------------ |
# | ds | player_stats |
# | x  | player       |
# | n  | name         |
# | k  | kills        |
# | d  | deaths       |
# | a  | assists      |

# 4. Lợi ích tách hàm calculate_kda()

# Tránh lặp code (DRY).
# Dễ sửa, tái sử dụng, kiểm thử.


player_stats = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5"),
]


def calculate_kda(kills, deaths, assists):
    return (kills + assists) / deaths


def process_players(player_stats):
    print("--- BẢNG XẾP HẠNG KDA ---")

    for player in player_stats:
        name, kills, deaths, assists = player

        try:
            kills = int(kills)
            deaths = int(deaths)
            assists = int(assists)

            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda}")

        except ZeroDivisionError:
            print(f"Tuyển thủ {name}: KDA Hoàn hảo (Perfect Game)!")
            continue

        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi dữ liệu không hợp lệ!")
            continue


process_players(player_stats)
