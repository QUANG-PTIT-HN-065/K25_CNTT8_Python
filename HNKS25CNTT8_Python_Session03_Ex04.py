
# Phân tích & Đề xuất giải pháp

# Phân tích Input / Output
# Input
# Dữ liệu	
# Số lượng nhân sự mới:	int

# Output
# Nếu số lượng <= 0: [LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.
# Nếu số lượng > 0: [THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản.


# Đề xuất 2 giải pháp
# Giải pháp 1 — Dùng while True
# while True:
# Lặp vô hạn
# Khi dữ liệu đúng -> dùng break
# Ưu điểm: 
#   + Ngắn gọn
#   + Phổ biến
# Nhược điểm: 
#   + Người mới học khó hiểu hơn


# Giải pháp 2 — Dùng điều kiện kiểm tra trực tiếp

# while employee_count <= 0:
# Chỉ lặp khi dữ liệu sai
# Ưu điểm: 
#    + Dễ đọc
#    + Gần ngôn ngữ tự nhiên
# Nhược điểm
#    + Cần khởi tạo biến trước vòng lặp

# Bảng so sánh
# | Tiêu chí              | while True | while condition |
# | --------------------- | ---------- | --------------- |
# | Độ ngắn gọn           | Cao        | Trung bình      |
# | Dễ hiểu               | Trung bình | Cao             |
# | Gần ngôn ngữ tự nhiên | Thấp       | Cao             |
# | Phù hợp validation    | Tốt        | Tốt             |


print("----- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI -----")
employee_count = 0
while employee_count <= 0:
    employee_count = int(
        input("Vui lòng nhập số lượng nhân sự mới trong tháng này: ")
    )
    if employee_count <= 0:
        print("[LỖI] Số lượng không hợp lệ!")
        print("Vui lòng nhập một con số lớn hơn 0.\n")
print(f"\n[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {employee_count} nhân sự mới!")
print("CHƯƠNG TRÌNH KẾT THÚC")