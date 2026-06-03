# 1 Phân tích lỗi
# String trong Python là immutable (bất biến).
# Các hàm strip(), title(), upper(), lower() không thay đổi chuỗi gốc, mà trả về một chuỗi mới.
# Trong code hiện tại, lập trình viên chỉ gọi hàm mà không gán lại kết quả, nên dữ liệu không thay đổi.

student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)