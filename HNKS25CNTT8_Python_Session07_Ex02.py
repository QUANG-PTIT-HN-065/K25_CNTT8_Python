# 1 Phân tích lỗi
# transaction.strip() không làm thay đổi chuỗi gốc vì string trong Python là bất biến, cần gán lại kết quả.
# Chuỗi giao dịch được phân tách bằng ký tự |.
# transaction.split("-") sai vì - không phải dấu phân cách giữa các trường dữ liệu.
# Tách bằng - làm dữ liệu trong parts bị sai vị trí, không lấy đúng tên, mã khóa học, số tiền và trạng thái.
# Cần strip() từng phần sau split() để loại bỏ khoảng trắng thừa.
# Cần chuyển amount từ chuỗi sang số (int) để định dạng tiền bằng dấu phẩy.

transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

transaction = transaction.strip()

parts = transaction.split("|")

student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = int(parts[2].strip())
status = parts[3].strip().upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", format(amount, ",") + " VND")
print("Trạng thái:", status)