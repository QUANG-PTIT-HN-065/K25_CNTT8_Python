# Bảng thiết kế dữ liệu
# | Tên biến      | Câu hỏi input                                   | Kiểu dữ liệu |
# | ------------- | ----------------------------------------------- | ------------ |
# | patient_name  | Nhập họ và tên bệnh nhân                        | str          |
# | patient_age   | Nhập tuổi bệnh nhân dạng                        | int          |
# | spo2_level    | Nhập chỉ số SpO2 dạng số nguyên %               | int          |
# | heart_rate    | Nhập nhịp tim dạng số nguyên bpm                | int          |
# | has_insurance | Bạn có thẻ BHYT không?                          | str          |

# Pseudocode
# Bắt đầu

# Hiển thị tiêu đề hệ thống

# Nhập thông tin bệnh nhân

# Phân luồng y khoa:
#     Nếu spo2_level < 90 hoặc heart_rate > 120
#         RED

#     Ngược lại nếu spo2_level từ 90-95
#     hoặc heart_rate từ 100-120
#         YELLOW

#     Ngược lại
#         GREEN

# Tính viện phí:
#     Nếu tuổi < 6 hoặc tuổi >= 80
#         fee = 0

#     Ngược lại nếu có BHYT
#         fee = 250000

#     Ngược lại
#         fee = 500000

# In Phiếu Khám Bệnh Điện Tử

# In Log hệ thống:
#     type() của các biến

# Kết thúc


print("==========================================")
print("     SMART MEDICAL KIOSK SYSTEM")
print("==========================================")

# KHỐI THU THẬP DỮ LIỆU

patient_name = input("Nhập họ và tên bệnh nhân (Ví dụ: Nguyen Van A): ")
patient_age = int(input("Nhập tuổi bệnh nhân dạng số nguyên (Ví dụ: 25): "))
spo2_level = int(input("Nhập chỉ số SpO2 dạng số nguyên % (Ví dụ: 98): "))
heart_rate = int(input("Nhập nhịp tim dạng số nguyên bpm (Ví dụ: 75): "))
has_insurance = input("Bạn có thẻ BHYT không? (Chỉ nhập yes hoặc no): ").lower()

# KHỐI PHÂN LUỒNG Y KHOA

if spo2_level < 90 or heart_rate > 120:
    triage_result = "RED ALERT - CẤP CỨU KHẨN"
elif 90 <= spo2_level <= 95 or 100 <= heart_rate <= 120:
    triage_result = "YELLOW ALERT - THEO DÕI SÁT"
else:
    triage_result = "GREEN - KHÁM THƯỜNG"


# KHỐI TÍNH VIỆN PHÍ
base_fee = 500000

if patient_age < 6 or patient_age >= 80:
    hospital_fee = 0
elif has_insurance == "yes":
    hospital_fee = 250000
else:
    hospital_fee = 500000

# KHỐI HIỂN THỊ PHIẾU KHÁM
print("\n==========================================")
print("      PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("==========================================")
print("Họ tên bệnh nhân :", patient_name)
print("Tuổi             :", patient_age)
print("SpO2             :", spo2_level, "%")
print("Nhịp tim         :", heart_rate, "bpm")
print("Có BHYT          :", has_insurance)
print("------------------------------------------")
print("KẾT QUẢ PHÂN LUỒNG:")
print(triage_result)
print("------------------------------------------")
print("TẠM ỨNG VIỆN PHÍ:")
print(format(hospital_fee, ","), "VNĐ")

print("==========================================")

# KHỐI LOG HỆ THỐNG
print("\n============= SYSTEM LOG =============")

print("patient_name   =", type(patient_name))
print("patient_age    =", type(patient_age))
print("spo2_level     =", type(spo2_level))
print("heart_rate     =", type(heart_rate))
print("has_insurance  =", type(has_insurance))