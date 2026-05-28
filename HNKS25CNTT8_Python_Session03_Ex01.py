# Phân tích lỗi
# Biến total_budget được đặt bên trong vòng lặp.

# Điều này làm cho mỗi lần lặp:

# total_budget bị gán lại thành 0
# Giá trị cũ bị mất hoàn toàn

# Dò luồng thực thi

# Lần lặp 1
# total_budget = 0
# salary = 5000000
# total_budget = total_budget + salary

# Kết quả: total_budget = 5000000

# Lần lặp 2 
# Vòng lặp chạy lại: total_budget = 0
# Giá trị 5000000 bị xóa.

# Kết quả: total_budget = 4000000

# lần lắp tiếp theo logic trên, kết quả vẫn vậy total_budget = 0

# Sau đó:

# salary = 6000000
# total_budget = 0 + 6000000

# Kết quả cuối:

# total_budget = 6000000

# Lỗi logic kinh điển : Khởi tạo biến tích lũy bên trong vòng lặp
for i in range(5):
    total = 0
    total += i

# Biến total sẽ luôn bị reset.


# Sửa lỗi
print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")
total_budget = 0
for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    salary = int(input("Nhập mức lương (VND): "))
    total_budget += salary
print("→ KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:",
    total_budget, "VND")