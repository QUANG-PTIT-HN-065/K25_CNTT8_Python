# Phân tích và thiết kế giải pháp
# A Phân tích Input / Output
# Input (Dữ liệu đầu vào)
# Hệ thống yêu cầu nhân viên lễ tân nhập:

# | Thông tin           | Biến           | Kiểu dữ liệu |
# | ------------------- | -------------- | ------------ |
# | Họ và tên bệnh nhân |  Name          |  str         |
# | Mã bệnh án          |  id            |  str         |
# | Khoa / Phòng khám   |  department    |  str         |

# Output (Dữ liệu đầu ra)
# Hệ thống hiển thị:
# Phiếu khám bệnh điện tử
# Thông tin bệnh nhân
# Thông báo xác nhận đăng ký thành 

# B. Đề xuất giải pháp
# Ý tưởng xử lý
# Hiển thị tiêu đề hệ thống
# Dùng hàm input() để nhận thông tin bệnh nhân
# Lưu dữ liệu vào các biến
# Sử dụng print() để hiển thị phiếu khám theo định dạng đẹp mắt
# Căn chỉnh dữ liệu bằng:
# dấu :
# khoảng trắng
# ký tự = và -

# input() Nhập dữ liệu từ bàn phím       
# print() Hiển thị thông tin ra màn hình 

# C. Thiết kế thuật toán

# Bắt đầu chương trình

# Hiển thị tiêu đề hệ thống

# Nhập họ tên bệnh nhân
# Lưu vào patient_name

# Nhập mã bệnh án
# Lưu vào medical_code

# Nhập khoa/phòng khám
# Lưu vào department

# Hiển thị phiếu khám bệnh:
#     - Tiêu đề phiếu
#     - Họ tên bệnh nhân
#     - Mã bệnh án
#     - Khoa khám
#     - Trạng thái xác nhận

# Kết thúc chương trình 


print("   HỆ THỐNG TIẾP NHẬN BỆNH NHÂN")

Name = input("Nhập họ và tên bệnh nhân: ")
id = input("Nhập mã bệnh án: ")
department = input("Nhập khoa/phòng khám: ")


print("\n========================================")
print("       PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("========================================")
print("Họ tên bệnh nhân :", Name)
print("Mã bệnh án       :", id)
print("Khoa khám        :", department)
print("----------------------------------------")
print("Trạng thái       : Đăng ký thành công")
print("========================================")