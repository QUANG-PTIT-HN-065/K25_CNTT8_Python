# nguyên nhân lỗi đặt sai vị trí khởi tạo biến total_students 
# làm cho khi tính tổng của 1 chi nhánh xong không reset lại mà cứ tiếp tục cộng dồn gây sai lệnh

# Trace code

# Ban đầu:

# total_students = 0
# Chi nhánh 1
# Quá trình cộng:

# 
# lớp 1(30):	0 + 30 = 30
# lớp 2(25):	30 + 25 = 55
# lớp 3(28):	55 + 28 = 83
# Kết quả:

# Chi nhánh 1: 83 học viên

# Hiển thị đúng vì total_students ban đầu bằng 0.

# Chi nhánh 2
# Sau Chi nhánh 1:

# total_students = 83

# Biến không được reset về 0.

# Quá trình cộng:

# Lớp 1(20):	83 + 20 = 103
# Lớp 2(22):	103 + 22 = 125
# Lớp 3(18):	125 + 18 = 143
# Kết quả:

# Chi nhánh 2: 143 học viên
# Trong khi tổng thực tế của Chi nhánh 2 là:
# 20 + 22 + 18 = 60

# Sau Chi nhánh 2:

# total_students = 143

# Biến tiếp tục không được reset.

# Lớp 1(35):	143 + 35 = 178
# Lớp 2(32):	178 + 32 = 210
# Lớp 3(30):	210 + 30 = 240

# Kết quả:

# Chi nhánh 3: 240 học viên

# Trong khi tổng thực tế của Chi nhánh 3 là:

# 35 + 32 + 30 = 97

# Hệ thống hiển thị 240 vì đang cộng dồn:

# 83 + 60 + 97 = 240

branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):
    total_students = 0

    print(f"\nChi nhánh {branch}")

    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        total_students += student_count

    print(f"Chi nhánh {branch}: {total_students} học viên")