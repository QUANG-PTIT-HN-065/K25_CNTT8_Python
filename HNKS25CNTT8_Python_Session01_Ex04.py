# Phân tích và Đề xuất giải pháp
# a. Phân tích Input / Output
# Input (Dữ liệu đầu vào)

# Nhân viên nhập dữ liệu từ bàn phím bằng input():
# | Thông tin       | Ví dụ | Kiểu dữ liệu ban đầu |
# | --------------- | ----- | -------------------- |
# | Mã bệnh nhân    | BN999 | `str`                |
# | Nhiệt độ cơ thể | 37.5  | `str`                |
# | Nhịp tim        | 85    | `str`                |

# Output
# | Dữ liệu         | Kiểu dữ liệu mong muốn |
# | --------------- | ---------------------- |
# | Mã bệnh nhân    | `str`                  |
# | Nhiệt độ cơ thể | `float`                |
# | Nhịp tim        | `int`                  |

# Đề xuất 2 giải pháp ép kiểu dữ liệu
# Giải pháp 1: Ép kiểu ngay khi nhập dữ liệu

# Đặc điểm
# - Dữ liệu được chuyển kiểu ngay lập tức.
# - Biến lưu trữ luôn đúng kiểu dữ liệu.

# Giải pháp 2: Nhập dữ liệu dạng chuỗi rồi ép kiểu sau
# Đặc điểm
# - Giữ lại dữ liệu gốc để kiểm tra.
# - Dễ debug nếu nhập sai dữ liệu.

# Bảng so sánh 2 giải pháp
# | Tiêu chí             | Giải pháp 1 | Giải pháp 2 |
# | -------------------- | ----------- | ----------- |
# | Số lượng biến        | Ít hơn      | Nhiều hơn   |
# | Tốn bộ nhớ           | Ít          | Nhiều hơn   |
# | Độ ngắn gọn          | Ngắn gọn    | Dài hơn     |
# | Dễ đọc code          | Cao         | Trung bình  |
# | Khả năng debug       | Trung bình  | Cao         |
# | Kiểm tra dữ liệu gốc | Không giữ   | Có giữ      |

# lựa chọn
# Giải pháp phù hợp nhất trong môi trường bệnh viện:
# => Giải pháp 2

# Lý do:

# Hệ thống bệnh viện cần độ chính xác cao.
# Khi nhập sai dữ liệu có thể kiểm tra lại dữ liệu gốc.
# Dễ debug và truy vết lỗi nhập liệu.
# An toàn hơn cho hệ thống quản lý bệnh nhân.

print("======================================")
print("   HỆ THỐNG CHUẨN HÓA DỮ LIỆU Y TẾ")
print("======================================")


patientID = input("Nhập mã bệnh nhân: ")
temperatur = input("Nhập nhiệt độ cơ thể: ")

heart= input("Nhập nhịp tim: ")

temperature = float(temperatur)
heartRate = int(heart)

print("\n======================================")
print("      KẾT QUẢ CHUẨN HÓA DỮ LIỆU")
print("======================================")

print("Mã bệnh nhân:", patientID)

print("Nhiệt độ cơ thể:", temperature, "độ C")

print("-")
print("Kiểu dữ liệu hệ thống ghi nhận:")
print(type(temperature))

print("Nhịp tim:", heartRate, "nhịp/phút")

print("Kiểu dữ liệu hệ thống ghi nhận:")
print(type(heartRate))

print("\nThông báo: Dữ liệu hợp lệ.")
print("Màn hình Monitor đã sẵn sàng kết nối!")