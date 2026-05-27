
# Input
# | Dữ liệu          | Kiểu ban đầu |
# | ---------------- | ------------ |
# | patient_name     | str          |
# | patient_code     | str          |
# | body_temperature | str          |
# | heart_rate       | str          |
# | body_weight      | str          |

# Output
# | Dữ liệu          | Kiểu mong muốn |
# | ---------------- | -------------- |
# | patient_name     | str            |
# | patient_code     | str            |
# | body_temperature | float          |
# | heart_rate       | int            |
# | body_weight      | float          |

# Giải pháp xử lý
# Dùng input() để thu thập dữ liệu.
# Ép kiểu:
# float() cho nhiệt độ và cân nặng.
# int() cho nhịp tim.
# Dùng print() hiển thị:
# Phiếu khám bệnh điện tử.
# Log kiểm tra kiểu dữ liệu.

# Thuật toán

# Bắt đầu
# Hiển thị tiêu đề hệ thống

# Nhập thông tin bệnh nhân
# Nhập chỉ số sinh hiệu

# Ép kiểu dữ liệu:
#     nhiệt độ -> float
#     nhịp tim -> int
#     cân nặng -> float

# Hiển thị phiếu khám bệnh
# Hiển thị log kiểm tra kiểu dữ liệu

# Kết thúc

print("==========================================")
print("    KIOSK KHAI BÁO TỰ PHỤC VỤ Y TẾ")
print("==========================================")

Name = input("Nhập họ và tên bệnh nhân (Ví dụ: Nguyen Van A): ")
patientID = input("Nhập mã bệnh nhân (Ví dụ: BN1024): ")
temperature = input("Nhập nhiệt độ cơ thể dạng số thập phân (Ví dụ: 37.5): ")
heartRate = input("Nhập nhịp tim dạng số nguyên (Ví dụ: 85): ")
weight = input("Nhập cân nặng dạng số thập phân (Ví dụ: 65.5): ")


body_temperature = float(temperature)
heart_rate = int(heartRate)
body_weight = float(weight)


print("\n==========================================")
print("       PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("==========================================")

print("Mã bệnh nhân: ", patientID)
print("Họ tên      :", Name)
print("Nhiệt độ    :", body_temperature, "độ C")
print("Nhịp tim    :", heart_rate, "nhịp/phút")
print("Cân nặng    :", body_weight, "kg")

print("------------------------------------------")
print("Trạng thái   : Dữ liệu hợp lệ")
print("==========================================")

print("\n========== SYSTEM LOG ==========")

print("body_temperature =", type(body_temperature))
print("heart_rate       =", type(heart_rate))
print("body_weight      =", type(body_weight))
