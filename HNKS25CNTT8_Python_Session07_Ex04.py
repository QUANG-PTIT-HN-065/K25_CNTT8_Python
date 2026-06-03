# 1 Phân tích và thiết kế

# Input

# number_of_forms: int
# registration_data: str

# Output

# Thông tin học viên đã chuẩn hóa
# Mã xác nhận
# Thông báo lỗi cho dữ liệu không hợp lệ

# Giải pháp
# split("|") để tách 4 phần dữ liệu
# strip() để xóa khoảng trắng thừa
# title() chuẩn hóa họ tên và khóa học
# upper() chuẩn hóa mã học viên
# lower() chuẩn hóa email
# Kiểm tra:
# Số lượng phiếu > 0
# Chuỗi có đúng 4 phần
# Email chứa @
# Mã học viên có độ dài ≥ 5

# Pseudocode
# Nhập số lượng phiếu

# Nếu số lượng <= 0
#     Thông báo lỗi
#     Kết thúc

# Lặp theo số lượng phiếu
#     Nhập chuỗi đăng ký

#     Tách theo dấu |

#     Nếu không đủ 4 phần
#         Báo lỗi
#         Bỏ qua

#     Chuẩn hóa dữ liệu

#     Nếu email không chứa @
#         Báo lỗi
#         Bỏ qua

#     Nếu mã học viên < 5 ký tự
#         Báo lỗi
#         Bỏ qua

#     Tạo mã xác nhận

#     In thông tin chuẩn hóa

number_of_forms = int(input("Nhập số lượng phiếu đăng ký: "))

if number_of_forms <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
else:
    for i in range(number_of_forms):
        registration_data = input(f"Nhập phiếu đăng ký {i + 1}: ")

        parts = registration_data.split("|")

        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        student_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_code = parts[2].strip().upper()
        email = parts[3].strip().lower()

        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        confirmation_code = student_code + "_" + course_name.upper().replace(" ", "-")

        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print("Học viên:", student_name)
        print("Khóa học:", course_name)
        print("Mã học viên:", student_code)
        print("Email:", email)
        print("Mã xác nhận:", confirmation_code)
