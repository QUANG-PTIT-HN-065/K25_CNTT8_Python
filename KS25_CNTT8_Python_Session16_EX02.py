# 1) Phân tích lỗi
# Câu 1

# Dòng lệnh:

# new_prescription = old_prescription

# không tạo ra danh sách mới.

# new_prescription và old_prescription cùng tham chiếu đến một List trong bộ nhớ.

# Vì vậy:

# new_prescription.append("Oresol")

# sẽ làm thay đổi chính List gốc, nên yesterday_prescription cũng bị thêm "Oresol".

# Câu 2

# Một số cách tạo bản sao độc lập của List:

# new_prescription = old_prescription.copy()
# new_prescription = old_prescription[:]
# new_prescription = list(old_prescription)
# Câu 3

# Lệnh:

# new_prescription[0].replace("Panadol", "Paracetamol")

# không có tác dụng vì replace() tạo ra một chuỗi mới nhưng không tự cập nhật lại phần tử trong List.

# String trong Python là kiểu dữ liệu bất biến (Immutable).

# Câu 4

# Cần gán kết quả trả về của replace() vào lại vị trí index 0:

# new_prescription[0] = new_prescription[0].replace(
#     "Panadol",
#     "Paracetamol"
# )

yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]


def update_prescription(old_prescription):
    new_prescription = old_prescription.copy()

    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")

    new_prescription.append("Oresol")

    return new_prescription


today_prescription = update_prescription(yesterday_prescription)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)
