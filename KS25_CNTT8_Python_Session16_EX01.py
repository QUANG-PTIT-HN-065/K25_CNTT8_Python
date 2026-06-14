# 1) Phân tích lỗi
# Câu 1

# String trong Python là kiểu dữ liệu bất biến (Immutable).

# Vì vậy:

# raw_diagnosis.strip()
# raw_diagnosis.title()

# không làm thay đổi giá trị của raw_diagnosis, mà chỉ tạo ra một chuỗi mới rồi bỏ đi.

# Câu 2

# Phải gán lại kết quả cho biến:

# raw_diagnosis = raw_diagnosis.strip()
# raw_diagnosis = raw_diagnosis.title()

# Hoặc viết gọn:

# raw_diagnosis = raw_diagnosis.strip().title()
# Câu 3

# extend() sẽ duyệt từng phần tử của đối tượng truyền vào và thêm từng phần tử đó vào list.

# Khi truyền vào một chuỗi:

# current_list.extend("Viem Phe Quan")

# Python xem chuỗi là tập hợp các ký tự:

# 'V'
# 'i'
# 'e'
# 'm'
# ' '
# 'P'
# 'h'
# 'e'
# ...

# nên từng ký tự được thêm riêng lẻ vào list.

# Đó là lý do kết quả xuất hiện:

# 'v', 'i', 'E', 'm', ...
# Câu 4

# Cần thay:

# current_list.extend(raw_diagnosis)

# bằng:

# current_list.append(raw_diagnosis)

# append() sẽ thêm nguyên vẹn chuỗi như một phần tử duy nhất của list.

# Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
patient_diagnoses = ["Sốt Xuất Huyết"]

def add_diagnosis(raw_diagnosis, current_list):
    raw_diagnosis = raw_diagnosis.strip().title()
    current_list.append(raw_diagnosis)
    return current_list

new_diagnosis = "  viEm phE QUan  "

updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)
