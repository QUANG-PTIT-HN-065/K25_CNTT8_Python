# 1) Phân tích thiết kế
# Refactoring Plan
# Đặt tên theo snake_case.
# Mỗi hàm chỉ thực hiện 1 nhiệm vụ.
# Thêm docstring cho các hàm.
# Logging Strategy
# File log: roster_app.log
# Format:
# [%(asctime)s] - [%(levelname)s] - %(message)s
# Hàm update_player_status(roster_list)

# Input:

# roster_list: danh sách tuyển thủ.

# Output:

# Cập nhật lương hoặc trạng thái tuyển thủ.

# Exceptions:

# Player ID không tồn tại.
# Lương nhập không hợp lệ.
# Lương âm hoặc bằng 0.

# Pseudocode:

# Nhập player_id
# Chuẩn hóa ID bằng strip().upper()

# Tìm tuyển thủ
# Nếu không tồn tại:
#     thông báo lỗi
#     ghi log warning

# Hiển thị thông tin tuyển thủ

# Chọn:
# 1. Cập nhật lương
#     nhập lương mới
#     nếu sai -> nhập lại
#     cập nhật
#     ghi log info

# 2. Cập nhật trạng thái
#     chọn Active hoặc Benched
#     cập nhật
#     ghi log info

import logging

logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s",
)


def calculate_actual_pay(player_dict):
    if player_dict["status"] == "Benched":
        return player_dict["salary"] * 0.5
    return player_dict["salary"]


roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active",
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active",
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched",
    },
]


def generate_payroll_report(roster_list):
    try:
        total = 0

        for player in roster_list:
            actual_pay = calculate_actual_pay(player)
            total += actual_pay

        print("Tổng quỹ lương:", total)

        logging.info(f"Generated monthly payroll report. Total: {total}")

    except KeyError as e:
        logging.error(f"Missing key while generating payroll report: {e}")


if __name__ == "__main__":
    generate_payroll_report(roster)
