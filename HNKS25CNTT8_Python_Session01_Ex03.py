# Phân tích và thiết kế giải pháp

# Input

# patient_name	str
# patient_age	    int

# Output
# Nếu dữ liệu hợp lệ:
# - In Phiếu khám bệnh điện tử gồm:
#   + Họ tên
#   + Tuổi
#   + Kết quả phân luồng
# Nếu dữ liệu không hợp lệ:
#   + In thông báo lỗi
#   + Không in phiếu khám

# Đề xuất giải pháp
# Kiểm tra lỗi dữ liệu

# Dùng: strip() để kiểm tra tên rỗng hoặc toàn khoảng trắng.
# Toán tử logic:
# patient_age < 0
# patient_age > 150

# Phân luồng bệnh nhân

# Dùng if-elif-else:


# Pseudocode
# Bắt đầu

# Nhập tên bệnh nhân
# Nhập tuổi bệnh nhân

# Kiểm tra dữ liệu:
#     Nếu tên rỗng
#         Báo lỗi
#         Kết thúc

#     Nếu tuổi < 0 hoặc > 150
#         Báo lỗi
#         Kết thúc

# Phân luồng:
#     Nếu tuổi < 6
#         Ưu tiên bệnh nhi

#     Ngược lại nếu tuổi >= 80
#         Ưu tiên người cao tuổi

#     Ngược lại
#         Khám thường

# In phiếu khám bệnh

# Kết thúc


print("========================================")
print("   HỆ THỐNG PHÂN LUỒNG BỆNH NHÂN")
print("========================================")

patient_name = input("Nhập họ và tên bệnh nhân: ")
patient_age = int(input("Nhập tuổi bệnh nhân: "))


if patient_name.strip() == "" or patient_age < 0 or patient_age > 150:

    print("\nLỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
else:
    if patient_age < 6:

        triage_result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
    elif patient_age >= 80:

        triage_result = (
            "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
        )
    else:

        triage_result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."
    print("\n========================================")
    print("      PHIẾU KHÁM BỆNH ĐIỆN TỬ")
    print("========================================")

    print("Họ tên bệnh nhân :", patient_name)
    print("Tuổi bệnh nhân   :", patient_age)

    print("----------------------------------------")
    print("Kết quả phân luồng:")
    print(triage_result)

    print("========================================")
