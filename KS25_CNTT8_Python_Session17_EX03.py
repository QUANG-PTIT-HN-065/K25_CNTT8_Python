# 1) Phân tích và thiết kế

# Sự khác nhau giữa combinations và permutations

# itertools.combinations(iterable, 2)
# Không quan tâm thứ tự.
# (T1, GEN.G) và (GEN.G, T1) được xem là một cặp.
# Công thức: n! / (r! * (n-r)!)
# itertools.permutations(iterable, 2)
# Có quan tâm thứ tự.
# (T1, GEN.G) và (GEN.G, T1) là hai kết quả khác nhau.
# Công thức: n! / (n-r)!

# Lý do phải dùng combinations

# Thi đấu vòng tròn một lượt yêu cầu mỗi cặp đội chỉ gặp nhau đúng 1 lần.
# Nếu dùng permutations sẽ sinh ra cả:
# T1 vs GEN.G
# GEN.G vs T1
# Dẫn đến trùng trận đấu.
# Vì vậy phải dùng combinations.

# Luồng sinh Match ID

# Tách chuỗi trận đấu bằng:
# team_a, team_b = match.split(" vs ")
# Lấy 3 ký tự đầu:
# team_a[:3]
# team_b[:3]
# Nếu tên đội ngắn hơn 3 ký tự:
# f"{team_a[:3]:X<3}"

# Ví dụ:

# T1 -> T1X
# Đánh số trận:
# f"{index:02d}"

# Kết quả:

# 1  -> 01
# 2  -> 02
# 10 -> 10
# Ghép thành:
# M01-T1X-GEN

import itertools

teams_list = []
match_schedule = []


def input_teams():
    """
    Nhập và chuẩn hóa danh sách đội tuyển.
    """
    global teams_list

    print("\n--- NHẬP DANH SÁCH ---")

    teams = input("Nhập các đội (cách nhau bởi dấu phẩy): ")

    temp_list = [team.strip().upper() for team in teams.split(",") if team.strip()]

    unique_teams = []

    for team in temp_list:
        if team not in unique_teams:
            unique_teams.append(team)

    teams_list = unique_teams

    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")


def create_schedule():
    """
    Tạo lịch thi đấu vòng tròn một lượt.
    """
    global match_schedule

    if len(teams_list) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        return []

    matches = itertools.combinations(teams_list, 2)

    match_schedule = [f"{team_a} vs {team_b}" for team_a, team_b in matches]

    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")

    for index, match in enumerate(match_schedule, start=1):
        print(f"{index}. {match}")

    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")

    return match_schedule


def generate_match_ids():
    """
    Sinh mã định danh cho các trận đấu.
    """
    if not match_schedule:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return

    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")

    for index, match in enumerate(match_schedule, start=1):
        team_a, team_b = match.split(" vs ")

        code_a = f"{team_a[:3]:X<3}"
        code_b = f"{team_b[:3]:X<3}"

        match_id = f"M{index:02d}-{code_a}-{code_b}"

        print(f"Trận {index} ({match}) -> ID: {match_id}")


def main():
    """
    Hàm điều khiển chương trình.
    """
    while True:
        print("\n============= ESPORTS MATCHMAKER =============")
        print("1. Nhập danh sách Đội tuyển")
        print("2. Tạo lịch thi đấu (Combinations)")
        print("3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)")
        print("4. Đóng hệ thống")
        print("==============================================")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            input_teams()

        elif choice == "2":
            create_schedule()

        elif choice == "3":
            generate_match_ids()

        elif choice == "4":
            print("Đóng hệ thống thành công!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


main()
