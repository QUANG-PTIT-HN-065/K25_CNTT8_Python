# phần tích lỗi

# nguyên nhần lỗi hiển thị sao dự liệu là do
# Dòng print('Tên bệnh nhân:', symptom); -> In ra Triệu chứng thay vì Tên.
# Dòng print('Tuổi:', name_patient); -> In ra Tên bệnh nhân thay vì Tuổi.
# Dòng print('Triệu chứng:', age); -> In ra Tuổi thay vì Triệu chứng.

# sửa lại code

print(" --- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ")
name_patient = input("Nhập tên bệnh nhân: ")
age = int(input("Mời bạn nhập tuổi: "))
symptom = input("Mời bạn nhập triệu chứng bênh: ")
print(" PHIẾU KHÁM BỆNH --")
print("Tên bệnh nhân:", name_patient)
print("Tuổi:", age)
print("Triệu chứng:", symptom)
