# Phân tích lỗi

# Nguyên nhân nhập dữ liệu là số nhưng lại trả ra là chuỗi là do hàm input() trong py mặc định trả về kiểu dữ liệu string:
# Đặc điểm của hàm input() trong Python
# Hàm input():
# Dùng để nhận dữ liệu từ bàn phím.
# Giá trị trả về của input() luôn có kiểu str (chuỗi).

print("- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN -")

name_patient = input("Nhập tên bệnh nhân: ")
weight = float(input("Nhập cân nặng bệnh nhân: "))

print("- KIỂM TRA DỮ LIỆU LƯU TRỮ -")
print("Bệnh nhân:", name_patient)
print("Cân nặng đã nhập:", weight)
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là:")
print(type(weight))
