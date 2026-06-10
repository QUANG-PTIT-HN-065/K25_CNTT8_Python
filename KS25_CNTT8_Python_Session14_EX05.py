# 1) Phân tích và thiết kế giải pháp
# Hàm find_student(records, student_id)

# Input:

# records (list)
# student_id (str)

# Output:

# index của học viên nếu tìm thấy.
# -1 nếu không tìm thấy.

# Lợi ích:

# Tránh lặp code tìm kiếm ở nhiều chức năng.
# Dễ bảo trì.
# Dễ tái sử dụng.
# Chỉ cần sửa một nơi nếu thay đổi cách tìm kiếm.
# Hàm display_statements(records)

# Input:

# records (list)

# Output:

# None

# Luồng xử lý:

# Duyệt danh sách.
# Xác định trạng thái theo current_points.
# Hiển thị thông tin.
# Hàm redeem_rewards(records)

# Input:

# records (list)

# Output:

# None

# Luồng dữ liệu:

# Giảm current_points.
# Tăng spent_points.
# Hàm appeal_score(records)

# Input:

# records (list)

# Output:

# None

# Luồng dữ liệu:

# Tăng current_points.
# Giảm spent_points.
# Tăng refunded_points.
# Hàm activate_multiplier(records)

# Input:

# records (list)

# Output:

# None

# Luồng dữ liệu:

# Cập nhật multiplier.
# Hàm grade_assignment(records)

# Input:

# records (list)

# Output:

# None

# Luồng dữ liệu:

# Tính điểm thực nhận.
# Cộng vào current_points

# Pseudocode chức năng 2

# Nhập mã học viên
# Chuẩn hóa mã

# Tìm học viên

# Nếu không tìm thấy
#     Thông báo lỗi
#     Kết thúc

# Nhập số điểm cần tiêu

# Nếu điểm <= 0
#     Báo lỗi

# Nếu điểm > current_points
#     Báo lỗi

# current_points -= điểm
# spent_points += điểm

# Thông báo thành công

# Pseudocode chức năng 5

# Nhập mã học viên
# Chuẩn hóa mã

# Tìm học viên

# Nếu không tìm thấy
#     Báo lỗi
#     Kết thúc

# Nhập điểm gốc

# Nếu điểm <= 0
#     Báo lỗi

# actual_points = điểm_gốc * multiplier

# current_points += actual_points

# Thông báo điểm thực nhận
# Thông báo cộng điểm thành công

student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0,
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5,
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0,
    },
]


def find_student(records, student_id):
    """Tìm học viên theo mã"""
    for index, student in enumerate(records):
        if student["student_id"] == student_id:
            return index
    return -1


def input_positive_int(message):
    """Nhập số nguyên dương"""

    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Vui lòng nhập số nguyên dương!")

        except ValueError:
            print("Vui lòng nhập số nguyên dương!")


def display_statements(records):
    """Hiển thị sao kê"""

    print("\n--- SAO KÊ ĐIỂM SỐ ---")

    for index, student in enumerate(records, start=1):

        points = student["current_points"]

        if points < 500:
            status = "Cần tích lũy thêm"
        elif points <= 1500:
            status = "Thành viên tiềm năng"
        else:
            status = "Thành viên ưu tú"

        print(
            f"{index}. Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"Hiện có: {student['current_points']} | "
            f"Đã tiêu: {student['spent_points']} | "
            f"Hoàn trả: {student['refunded_points']} | "
            f"Hệ số: x{student['multiplier']} | "
            f"Trạng thái: {status}"
        )

    print("----------------------")


def redeem_rewards(records):
    """Đổi điểm lấy quà"""

    student_id = input("Nhập mã học viên đổi quà: ").strip().upper()

    index = find_student(records, student_id)

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    student = records[index]

    points = input_positive_int("Nhập số điểm cần tiêu: ")

    if points > student["current_points"]:
        print("Số dư điểm không đủ để thực hiện giao dịch!")
        return

    student["current_points"] -= points
    student["spent_points"] += points

    print(
        f"Giao dịch thành công! "
        f"'{student['name']}' đã tiêu {points} điểm. "
        f"Số dư còn lại: {student['current_points']} điểm."
    )


def appeal_score(records):
    """Hoàn điểm"""

    student_id = input("Nhập mã học viên cần phúc khảo: ").strip().upper()

    index = find_student(records, student_id)

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    student = records[index]

    points = input_positive_int("Nhập số điểm hoàn lại: ")

    if points > student["spent_points"]:
        print("Không thể hoàn số điểm lớn hơn " "tổng điểm đã tiêu!")
        return

    student["spent_points"] -= points
    student["current_points"] += points
    student["refunded_points"] += points

    print(
        f"Hoàn điểm thành công! "
        f"'{student['name']}' được cộng lại "
        f"{points} điểm."
    )


def activate_multiplier(records):
    """Kích hoạt hệ số"""

    student_id = input("Nhập mã học viên nhận hệ số: ").strip().upper()

    index = find_student(records, student_id)

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    while True:
        try:
            multiplier = float(input("Nhập hệ số nhân mới (1.0 - 3.0): "))

            if 1.0 <= multiplier <= 3.0:
                break

            print("Hệ số nhân không hợp lệ. " "Chỉ chấp nhận số từ 1.0 đến 3.0")

        except ValueError:
            print("Hệ số nhân không hợp lệ. " "Chỉ chấp nhận số từ 1.0 đến 3.0")

    records[index]["multiplier"] = multiplier

    print(
        f"Đã kích hoạt hệ số x{multiplier} "
        f"cho học viên "
        f"'{records[index]['name']}'."
    )


def grade_assignment(records):
    """Chấm bài"""

    student_id = input("Nhập mã học viên vừa nộp bài: ").strip().upper()

    index = find_student(records, student_id)

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    student = records[index]

    base_points = input_positive_int("Nhập số điểm gốc đạt được: ")

    actual_points = base_points * student["multiplier"]

    student["current_points"] += actual_points

    print(
        f"Hệ số hiện tại của " f"'{student['name']}' là " f"x{student['multiplier']}."
    )

    print(f"Điểm thực nhận: {actual_points}.")

    print(f"Đã cộng {actual_points} điểm " f"vào tài khoản!")


def display_menu():
    print("\n===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====")
    print("1. Hiển thị sao kê điểm số")
    print("2. Đổi điểm lấy phần thưởng")
    print("3. Phúc khảo bài thi (Hoàn điểm)")
    print("4. Kích hoạt (Hệ số nhân điểm)")
    print("5. Chấm bài (thêm điểm)")
    print("6. Thoát chương trình")
    print("=====================================================")


def main():

    while True:

        display_menu()

        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            display_statements(student_records)

        elif choice == "2":
            redeem_rewards(student_records)

        elif choice == "3":
            appeal_score(student_records)

        elif choice == "4":
            activate_multiplier(student_records)

        elif choice == "5":
            grade_assignment(student_records)

        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
