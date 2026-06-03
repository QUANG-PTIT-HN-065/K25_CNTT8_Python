# 1 Phân tích và thiết kế
# Input
# raw_data: str
# choice: int
# employee_id: str
# Output
# Chuỗi dữ liệu gốc
# Danh sách nhân viên đã chuẩn hóa
# Kết quả tìm kiếm nhân viên theo ID
# Thông báo lỗi khi nhập sai
# Giải pháp
# split("|") -> tách từng nhân viên
# split(";") -> tách thông tin nhân viên
# strip() -> xóa khoảng trắng thừa
# upper() -> chuẩn hóa ID và phòng ban
# title() -> chuẩn hóa họ tên
# replace("-", "") -> xóa dấu - trong số điện thoại
# isdigit() -> kiểm tra số điện thoại hợp lệ
# Dùng try-except xử lý nhập menu

# Pseudocode
# Lặp vô hạn
#     Hiển thị menu
#     Nhập lựa chọn

#     Nếu lựa chọn không hợp lệ
#         Báo lỗi

#     Nếu chọn 1
#         In raw_data

#     Nếu chọn 2
#         Tách dữ liệu nhân viên
#         Chuẩn hóa dữ liệu
#         In bảng báo cáo

#     Nếu chọn 3
#         Nhập mã nhân viên
#         Chuẩn hóa mã tìm kiếm
#         Tìm trong danh sách
#         In kết quả

#     Nếu chọn 4
#         Thoát chương trình

raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

def get_employee_list():
    employee_list = []
    for employee in raw_data.split("|"):
        info = employee.split(";")
        employee_id = info[0].strip().upper()
        employee_name = info[1].strip().title()
        phone = info[2].strip().replace("-", "")
        if phone.isdigit():
            phone = "******" + phone[-4:]
        else:
            phone = "Invalid Format"
        department = info[3].strip().upper()
        employee_list.append(
            {
                "id": employee_id,
                "name": employee_name,
                "phone": phone,
                "department": department
            }
        )

    return employee_list


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    try:
        choice = int(input("Nhập lựa chọn: "))
        if choice < 1 or choice > 4:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
            continue

    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
    if choice == 1:
        print(raw_data)
    elif choice == 2:
        employee_list = get_employee_list()
        print(f"\n{'ID':<12}{'HỌ TÊN':<20}{'SĐT':<15}{'PHÒNG BAN'}")

        for employee in employee_list:
            print(
                f"{employee['id']:<12}"
                f"{employee['name']:<20}"
                f"{employee['phone']:<15}"
                f"{employee['department']}"
            )

    elif choice == 3:
        search_id = input("Nhập mã nhân viên: ").strip().upper()
        employee_list = get_employee_list()
        found = False
        for employee in employee_list:
            if employee["id"] == search_id:
                print("\nThông tin nhân viên:")
                print("ID:", employee["id"])
                print("Họ tên:", employee["name"])
                print("SĐT:", employee["phone"])
                print("Phòng ban:", employee["department"])
                found = True
                break
        if not found:
            print("Không tìm thấy nhân viên")
    else:
        print("Thoát chương trình")
        break