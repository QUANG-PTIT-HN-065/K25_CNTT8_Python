# 1) Phân tích & Clean Code
# 1. Đặt tên biến và hàm chuẩn PEP 8 (snake_case)

# | Không chuẩn     | Chuẩn PEP 8      |
# | --------------- | ---------------- |
# | matches         | matches          |
# | displayMatches  | display_matches  |
# | addMatch        | add_match        |
# | updateScore     | update_score     |
# | generateReport  | generate_report  |
# | determineWinner | determine_winner |
# | inputScore      | input_score      |
# | m               | match            |
# | id              | match_id         |
# | a               | team_a           |
# | b               | team_b           |




import logging

logging.basicConfig(
    filename="tournament_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s",
)

matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed",
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending",
    },
]


def display_matches(match_list):
    """Hiển thị danh sách trận đấu."""
    logging.info("User viewed the match list.")

    if not match_list:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print(f"{'Mã trận':10} | {'Đội A':15} | {'Đội B':15} | {'Tỷ số':7} | Trạng thái")

    for match in match_list:
        try:
            print(
                f"{match['match_id']:10} | "
                f"{match['team_a']:15} | "
                f"{match['team_b']:15} | "
                f"{match['score_a']}-{match['score_b']:5} | "
                f"{match['status']}"
            )
        except KeyError:
            logging.error("Missing score key.")


def calculate_bonus():
    pass


def add_match(match_list):
    """Thêm trận đấu mới."""
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")

    match_id = input("Nhập mã trận đấu: ").strip()

    if not match_id:
        print("Mã trận đấu không được để trống.")
        logging.warning("User tried to add a match with empty match ID.")
        return

    for match in match_list:
        if match["match_id"] == match_id:
            print(f"Lỗi: Mã trận đấu {match_id} đã tồn tại.")
            logging.warning(f"Match ID {match_id} already exists.")
            return

    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()

    if not team_a or not team_b:
        print("Tên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
        return

    match_list.append(
        {
            "match_id": match_id,
            "team_a": team_a,
            "team_b": team_b,
            "score_a": 0,
            "score_b": 0,
            "status": "Pending",
        }
    )

    logging.info(f"Match {match_id} added successfully")
    print(f"Thành công: Đã thêm trận đấu {match_id}.")


def input_score(team_name):
    """Nhập điểm hợp lệ."""
    while True:
        try:
            score = int(input(f"Nhập điểm {team_name}: "))

            if score < 0:
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                logging.error(f"Negative score input detected: {score}")
                continue

            return score

        except ValueError as error:
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(f"Invalid score input. Error: {error}")


def update_score(match_list):
    """Cập nhật tỷ số trận đấu."""
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")

    match_id = input("Nhập mã trận đấu cần cập nhật: ")

    for match in match_list:
        if match["match_id"] == match_id:
            print(
                f"\nTrận đấu: {match['team_a']} vs {match['team_b']} ({match['status']})"
            )

            score_a = input_score("Đội A")
            score_b = input_score("Đội B")

            match["score_a"] = score_a
            match["score_b"] = score_b

            if score_a == 0 and score_b == 0:
                confirm = input(
                    "Tỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): "
                ).lower()

                if confirm == "y":
                    match["status"] = "Completed"
                else:
                    match["status"] = "Pending"

            else:
                match["status"] = "Completed"

            logging.info(f"Match {match_id} score updated successfully")
            print(f"Thành công: Đã cập nhật tỷ số trận đấu {match_id}.")
            return

    print(f"Không tìm thấy trận đấu mang mã {match_id}.")
    logging.warning(f"User tried to update non-existing match {match_id}")


def determine_winner(match):
    """Trả về đội thắng."""
    if match["status"] == "Pending":
        return "Not Started"

    if match["score_a"] > match["score_b"]:
        return match["team_a"]

    if match["score_b"] > match["score_a"]:
        return match["team_b"]

    return "Draw"


def generate_report(match_list):
    """Báo cáo thống kê."""
    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")

    total = 0

    for match in match_list:
        if match["status"] == "Completed":
            winner = determine_winner(match)

            print(
                f"{match['match_id']}: "
                f"{match['team_a']} {match['score_a']}-{match['score_b']} {match['team_b']} "
                f"| Kết quả: {winner}"
            )

            total += 1

    if total == 0:
        print("Chưa có trận đấu nào hoàn thành.")

    print(f"\nTổng số trận đã hoàn thành: {total}")
    logging.info("User generated tournament report.")


def main():
    """Menu chính."""
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====")
        print("1. Hiển thị lịch thi đấu & Kết quả")
        print("2. Thêm trận đấu mới")
        print("3. Cập nhật tỷ số trận đấu")
        print("4. Báo cáo thống kê")
        print("5. Thoát chương trình")

        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            display_matches(matches)

        elif choice == "2":
            add_match(matches)

        elif choice == "3":
            update_score(matches)

        elif choice == "4":
            generate_report(matches)

        elif choice == "5":
            logging.info("Application closed.")
            break

        else:
            print("Lựa chọn không hợp lệ.")
            logging.warning("Invalid menu choice selected")


if __name__ == "__main__":
    main()
