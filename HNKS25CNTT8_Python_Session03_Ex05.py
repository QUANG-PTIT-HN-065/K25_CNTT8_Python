
# Thiết kế dữ liệu
# | Tên biến          | Input                    | Kiểu dữ liệu | Validation |
# | ----------------- | ------------------------ | ------------ | ---------- |
# | employee_id       | Enter Employee ID        | str          | Không rỗng |
# | employee_name     | Enter Full Name          | str          | Không rỗng |
# | current_salary    | Enter Current Salary     | float        | > 0        |
# | performance_score | Enter Performance Score  | float        | 1.0 → 5.0  |
# | experience_years  | Enter Year of Experience | int          | >= 0       |

# Luồng chương trình
# Bắt đầu chương trình

# Lặp vô hạn:
#     Nhập employee_id
#     Kiểm tra không rỗng

#     Nhập employee_name
#     Kiểm tra không rỗng

#     Nhập current_salary
#     Nếu <= 0:
#         bắt nhập lại
#     Nhập performance_score
#     Nếu ngoài khoảng 1.0 → 5.0:
#         bắt nhập lại
#     Nhập experience_years
#     Nếu < 0:
#         bắt nhập lại
#     In Hồ sơ Điện tử
#     In Log hệ thống
#     Hỏi tiếp tục (y/n)
#     Nếu n:
#         kết thúc

# câu hỏi input()
# input("Enter Employee ID (Example: DEV01): ")
# input("Enter Full Name: ")
# input("Enter Current Salary in VND (Number > 0): ")
# input("Enter Performance Score (1.0 to 5.0): ")
# input("Enter Year of Experience (Integer >= 0): ")

print("================================================")
print("      KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI")
print("================================================")

# Vòng lặp nhập nhiều nhân viên
while True:
    print("\n[Nhập thông tin nhân viên]")
    # Nhập mã nhân viên
    while True:
        employee_id = input("1. Enter Employee ID (Example: DEV01): ").strip()
        if employee_id != "":
            break

        print("[!] Lỗi: Employee ID không được để trống!")
    # Nhập họ tên
    while True:
        employee_name = input("2. Enter Full Name: ").strip()

        if employee_name != "":
            break
        print("[!] Lỗi: Họ tên không được để trống!")
    # Nhập lương
    while True:
        current_salary = float(input("3. Enter Current Salary in VND (Number > 0): "))
        if current_salary > 0:
            break
        print("[!] Lỗi: Lương không thể là số âm hoặc bằng 0. Vui lòng nhập lại!")
    # Nhập điểm KPI
    while True:
        performance_score = float(input("4. Enter Performance Score (1.0 to 5.0): "))
        if 1.0 <= performance_score <= 5.0:
            break
        print("[!] Lỗi: Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0!")
    while True:
        experience_years = int(input("5. Enter Year of Experience (Integer >= 0): "))
        if experience_years >= 0:
            break
        print("[!] Lỗi: Số năm kinh nghiệm không hợp lệ!")

    # In Hồ sơ Điện tử
    print("\n================================================")
    print("              E-PROFILE CẬP NHẬT")
    print("================================================")

    print(f"- ID: {employee_id}")
    print(f"- Name: {employee_name}")
    print(f"- Salary: {current_salary} VND")
    print(f"- KPI Score: {performance_score} / 5.0")
    print(f"- Experience: {experience_years} years")
    # In Log hệ thống
    print("\n================================================")
    print("                 IT SYSTEM LOG")
    print("================================================")

    print("employee_id        |", type(employee_id))
    print("employee_name      |", type(employee_name))
    print("current_salary     |", type(current_salary))
    print("performance_score  |", type(performance_score))
    print("experience_years   |", type(experience_years))
    # Hỏi tiếp tục
    continue_choice = input(
        "\nDo you want to enter another employee? (y/n): "
    ).lower()

    if continue_choice == "n":
        print("\nĐang tắt kiosk... Tạm biệt!")
        break