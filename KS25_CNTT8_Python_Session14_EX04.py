# 1) Phân tích thiết kế hàm
# Hàm: calculate_average(student)

# Input:

# student (dict)

# Output:

# float: Điểm trung bình

# Pseudocode:

# Lấy điểm Toán, Lý, Hóa
# Tính tổng
# Chia cho 3
# Trả về kết quả
# Hàm: get_rank(average)

# Input:

# average (float)

# Output:

# str: Học lực

# Pseudocode:

# Nếu ĐTB ≥ 8 -> Giỏi
# Nếu ĐTB ≥ 65 -> Khá
# Nếu ĐTB ≥ 5 -> Trung bình
# Ngược lại -> Yếu
# Hàm: display_grades(records)

# Input:

# records (list)

# Output:

# None

# Pseudocode:

# Kiểm tra danh sách rỗng
# Duyệt từng sinh viên
# Gọi calculate_average
# Gọi get_rank
# Hiển thị bảng điểm
# Hàm: update_student_score(records)

# Input:

# records (list)

# Output:

# None

# Pseudocode:

# Nhập mã sinh viên
# Chuẩn hóa mã
# Tìm sinh viên
# Nếu không thấy -> thông báo lỗi
# Chọn môn học
# Nhập điểm mới
# Kiểm tra hợp lệ
# Cập nhật điểm
# Thông báo thành công
# Hàm: generate_report(records)

# Input:

# records (list)

# Output:

# None

# Pseudocode:

# Kiểm tra danh sách rỗng
# Duyệt danh sách
# Tính ĐTB từng sinh viên
# Đếm số lượng đỗ và trượt
# Tính tỷ lệ phần trăm
# In báo cáo
# Hàm: find_valedictorian(records)

# Input:

# records (list)

# Output:

# None

# Pseudocode:

# Kiểm tra danh sách rỗng
# Tìm sinh viên có ĐTB cao nhất
# Hiển thị thông tin thủ khoa

student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0,
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0,
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5,
    },
]


def calculate_average(student):
    """Tính điểm trung bình"""
    return (student["math"] + student["physics"] + student["chemistry"]) / 3


def get_rank(average):
    """Xếp loại học lực"""
    if average >= 8:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5:
        return "Trung bình"
    return "Yếu"


def display_grades(records):
    """Hiển thị bảng điểm"""

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):
        average = calculate_average(student)
        rank = get_rank(average)

        print(
            f"{index}. [{student['student_id']}] "
            f"{student['name']} | "
            f"Toán: {student['math']} | "
            f"Lý: {student['physics']} | "
            f"Hóa: {student['chemistry']} | "
            f"ĐTB: {average:.2f} - {rank}"
        )

    print("---------------------------")


def find_student_by_id(records, student_id):
    """Tìm sinh viên theo mã"""

    for student in records:
        if student["student_id"] == student_id:
            return student

    return None


def input_score():
    """Nhập điểm hợp lệ"""

    while True:
        try:
            score = float(input("Nhập điểm mới: "))

            if 0 <= score <= 10:
                return score

            print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")

        except ValueError:
            print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")


def update_student_score(records):
    """Cập nhật điểm sinh viên"""

    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()

    student = find_student_by_id(records, student_id)

    if student is None:
        print(f"Không tìm thấy sinh viên mang mã " f"{student_id} trong hệ thống!")
        return

    while True:
        print("1. Toán")
        print("2. Lý")
        print("3. Hóa")

        choice = input("Chọn môn học (1-Toán, 2-Lý, 3-Hóa): ")

        if choice in ("1", "2", "3"):
            break

        print("Lựa chọn không hợp lệ!")

    score = input_score()

    if choice == "1":
        student["math"] = score
        subject = "Toán"
    elif choice == "2":
        student["physics"] = score
        subject = "Lý"
    else:
        student["chemistry"] = score
        subject = "Hóa"

    print(
        f"Đã cập nhật điểm {subject} của sinh viên "
        f"'{student['name']}' thành {score}."
    )


def generate_report(records):
    """Báo cáo học vụ"""

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total = len(records)
    passed = 0
    failed = 0

    for student in records:
        average = calculate_average(student)

        if average >= 5:
            passed += 1
        else:
            failed += 1

    passed_percent = (passed / total) * 100
    failed_percent = (failed / total) * 100

    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(
        f"Số lượng qua môn (ĐTB >= 5.0): "
        f"{passed} sinh viên "
        f"(Chiếm {passed_percent:.2f}%)"
    )
    print(
        f"Số lượng trượt (ĐTB < 5.0): "
        f"{failed} sinh viên "
        f"(Chiếm {failed_percent:.2f}%)"
    )
    print("----------------------")


def find_valedictorian(records):
    """Tìm thủ khoa"""

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    top_student = max(records, key=calculate_average)

    average = calculate_average(top_student)

    print("\n--- VINH DANH THỦ KHOA ---")
    print(f"Sinh viên: {top_student['name']} " f"(Mã: {top_student['student_id']})")
    print(f"Điểm Trung Bình: {average:.2f}")
    print("Chúc mừng sinh viên đã đạt " "thành tích xuất sắc nhất khóa!")
    print("--------------------------")


def display_menu():
    """Hiển thị menu"""

    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực")
    print("2. Cập nhật điểm thi sinh viên")
    print("3. Báo cáo thống kê (Đỗ/Trượt)")
    print("4. Tìm sinh viên Thủ khoa")
    print("5. Thoát chương trình")
    print("======================================================")


def main():
    """Hàm chính"""

    while True:
        display_menu()

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_grades(student_records)

        elif choice == "2":
            update_student_score(student_records)

        elif choice == "3":
            generate_report(student_records)

        elif choice == "4":
            find_valedictorian(student_records)

        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


main()
