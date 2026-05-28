# Phân tích và thiết kế giải pháp
# Phân tích Input / Output

# Input
# | Dữ liệu       | Kiểu   |
# | ------------- | ------ |
# | employee_id   | string |
# | employee_name | string |
# | department    | string |

# Output
# Nếu dữ liệu hợp lệ:
# In Phiếu Hồ sơ Điện tử.
# Nếu:
# Mã nhân viên rỗng
# Họ tên rỗng
# Chỉ chứa khoảng trắng

# => Hiển thị: [CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.

# Đề xuất giải pháp
# Dùng vòng lặp for chạy đúng 3 lần.
# Dùng .strip() để loại bỏ khoảng trắng.
# Nếu dữ liệu không hợp lệ:
# In cảnh báo
# continue để chuyển sang nhân viên tiếp theo.
# Nếu hợp lệ:
 # In Phiếu Hồ sơ.

# Pseudocode
# Lặp từ 1 đến 3

#     Nhập mã nhân viên
#     Nhập họ tên
#     Nhập phòng ban

#     Xóa khoảng trắng dư bằng strip()

#     Nếu mã hoặc tên rỗng:
#         In cảnh báo
#         Chuyển sang nhân viên tiếp theo

#     Ngược lại:
#         In phiếu hồ sơ điện tử

# In thông báo hoàn tất

print("===== HỆ THỐNG TẠO HỒ SƠ NHÂN VIÊN =====")

# Vòng lặp xử lý đúng 3 nhân viên
for employee_number in range(1, 4):
    print(f"\n--- Nhập thông tin nhân viên số {employee_number} ---")
    employee_id = input("Nhập mã nhân viên: ")
    employee_name = input("Nhập họ và tên: ")
    department = input("Nhập phòng ban: ")
    if employee_id.strip() == "" or employee_name.strip() == "":

        print("\n[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ!")
        print("Hủy bỏ tạo hồ sơ cho nhân viên này.")
        continue
    print("\n========== PHIẾU HỒ SƠ ĐIỆN TỬ ==========")
    print("Mã nhân viên :", employee_id)
    print("Họ và tên    :", employee_name)
    print("Phòng ban    :", department)
    print("=========================================")
print("\nĐã hoàn tất xử lý hồ sơ cho 3 nhân viên!")