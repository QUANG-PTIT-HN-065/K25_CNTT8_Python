# 1) Phân tích và thiết kế giải pháp
# 1. Hàm validate_score(score_input)

# Input:

# score_input (str)

# Output:

# True nếu điểm hợp lệ.
# False nếu điểm không hợp lệ.
# 2. Hàm find_student_by_id(student_list, student_id)

# Input:

# student_list (list)
# student_id (str)

# Output:

# Trả về vị trí (index) của học viên nếu tìm thấy.
# Trả về -1 nếu không tìm thấy.
# 3. Hàm display_students(student_list)

# Input:

# student_list (list)

# Output:

# Không trả về dữ liệu.
# Hiển thị danh sách học viên.
# 4. Hàm add_student(student_list)

# Input:

# student_list (list)

# Output:

# Không trả về dữ liệu.
# Thêm học viên mới vào danh sách.
# 5. Hàm update_score(student_list)

# Input:

# student_list (list)

# Output:

# Không trả về dữ liệu.
# Cập nhật điểm học viên.
# 6. Hàm get_rank(average_score)

# Input:

# average_score (float)

# Output:

# "Giỏi"
# "Khá"
# "Trung bình"
# "Yếu"
# 7. Hàm evaluate_students(student_list)

# Input:

# student_list (list)

# Output:

# Không trả về dữ liệu.
# Hiển thị kết quả đánh giá học lực.
# Lý do tách thành nhiều hàm
# Dễ đọc và dễ bảo trì.
# Dễ kiểm tra và sửa lỗi.
# Tái sử dụng được logic.
# Tránh lặp code.
# Dễ mở rộng chức năng sau này.

students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0,
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5,
    },
]


def display_menu():
    """Hiển thị menu"""
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")


def validate_score(score_input):
    """Kiểm tra điểm hợp lệ"""
    try:
        score = float(score_input)
        return 0 <= score <= 10
    except ValueError:
        return False


def input_score(message):
    """Nhập điểm hợp lệ"""
    while True:
        score_input = input(message)

        if validate_score(score_input):
            return float(score_input)

        print("Điểm không hợp lệ, phải là số từ 0 đến 10")


def find_student_by_id(student_list, student_id):
    """Tìm học viên theo mã"""
    for index, student in enumerate(student_list):
        if student["student_id"] == student_id:
            return index
    return -1


def display_students(student_list):
    """Hiển thị danh sách học viên"""
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return

    for index, student in enumerate(student_list, start=1):
        print(
            f"{index}. Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"Toán: {student['math_score']} | "
            f"Anh: {student['english_score']}"
        )


def add_student(student_list):
    """Thêm học viên mới"""

    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()

        if find_student_by_id(student_list, student_id) != -1:
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
        else:
            break

    while True:
        name = input("Nhập tên học viên: ").strip()

        if name:
            name = name.title()
            break

        print("Tên học viên không được để trống!")

    math_score = input_score("Nhập điểm Toán: ")
    english_score = input_score("Nhập điểm Anh: ")

    student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score,
    }

    student_list.append(student)

    print("Thêm học viên thành công!")


def update_score(student_list):
    """Cập nhật điểm học viên"""

    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()

    index = find_student_by_id(student_list, student_id)

    if index == -1:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return

    math_score = input_score("Nhập điểm Toán mới: ")
    english_score = input_score("Nhập điểm Anh mới: ")

    student_list[index]["math_score"] = math_score
    student_list[index]["english_score"] = english_score

    print("Cập nhật điểm thành công!")


def get_rank(average_score):
    """Xếp loại học lực"""

    if average_score >= 8:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5:
        return "Trung bình"
    else:
        return "Yếu"


def evaluate_students(student_list):
    """Đánh giá học lực"""

    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return

    for student in student_list:
        average = (student["math_score"] + student["english_score"]) / 2
        rank = get_rank(average)

        print(
            f"Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"ĐTB: {average:.2f} | "
            f"Xếp loại: {rank}"
        )


while True:
    display_menu()

    choice = input("Nhập lựa chọn: ").strip()

    if choice == "1":
        display_students(students)

    elif choice == "2":
        add_student(students)

    elif choice == "3":
        update_score(students)

    elif choice == "4":
        evaluate_students(students)

    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
