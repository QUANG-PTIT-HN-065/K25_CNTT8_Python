# Phân tích lỗi
# Trace code khi working_days = 0
# working_days = 0

# Đi vào điều kiện:

# if working_days == 0:
#     print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")

# Sau khi in cảnh báo, chương trình vẫn chạy tiếp:

# bonus_amount = working_days * 200000

# Kết quả: bonus_amount = 0

# Tiếp tục gửi email: print("→ Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VND tiền thưởng!")

# Nguyên nhân lỗi

# if working_days == 0:

# chỉ in cảnh báo nhưng không dừng vòng lặp hoặc bỏ qua phần phía dưới.

print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")
for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số", employee_number, "---")
    working_days = int(input("Nhập số ngày công trong tháng: "))
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        print("--------------------------------------------------\n")
        continue
    bonus_amount = working_days * 200000
    print("-> Đã gửi Email: Chúc mừng nhận được",
          bonus_amount, "VND tiền thưởng!")
    print("--------------------------------------------------\n")
print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")