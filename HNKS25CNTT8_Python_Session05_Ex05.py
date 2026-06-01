# Phân tích và thiết kế giải pháp
# Input

# | Biến          | Kiểu dữ liệu | Ý nghĩa                  |
# | ------------- | ------------ | ------------------------ |
# | choice        | int          | Lựa chọn menu            |
# | branch_count  | int          | Số lượng chi nhánh       |
# | class_count   | int          | Số lớp của một chi nhánh |
# | student_count | int          | Số học viên của một lớp  |

# Output
# Tổng số học viên từng chi nhánh
# Chi nhánh có tổng số học viên cao nhất
# Danh sách lớp có sĩ số dưới 10 học viên
# Thông báo nếu không có lớp nào dưới 10 học viên
# Hướng dẫn sử dụng
# Thông báo thoát chương trình

# Đề xuất giải pháp
# Sử dụng vòng lặp while True để hiển thị menu
# Người dùng chọn chức năng
# Nếu chọn:
# 1: Nhập dữ liệu và thống kê
# 2: Hiển thị hướng dẫn
# 3: Thoát chương trình
# Nếu nhập lựa chọn khác:
# Thông báo không hợp lệ
# Quay lại menu

# Trong chức năng thống kê:

# Nhập số lượng chi nhánh
# Với mỗi chi nhánh:
# Nhập số lớp
# Tính tổng học viên
# Kiểm tra các lớp dưới 10 học viên
# Theo dõi chi nhánh có tổng học viên lớn nhất
# Không cho phép nhập số học viên âm

# Pseudocode
# Lặp vô hạn
#     Hiển thị menu
#     Nhập choice
#     Nếu choice == 1
#         Nhập branch_count
#         max_students = -1
#         max_branch = 0
#         Lặp từng chi nhánh
#             Nhập class_count
#             branch_total = 0
#             low_classes = []
#             Lặp từng lớp
#                 Nhập student_count
#                 Nếu student_count < 0
#                     nhập lại
#                 Cộng vào branch_total
#                 Nếu student_count < 10
#                     lưu lớp vào low_classes
#             In tổng học viên chi nhánh
#             Nếu branch_total > max_students
#                 cập nhật chi nhánh lớn nhất
#             Nếu low_classes rỗng
#                 thông báo không có lớp dưới 10
#             Ngược lại
#                 in danh sách lớp dưới 10
#         In chi nhánh có số học viên lớn nhất
#     Nếu choice == 2
#         In hướng dẫn
#     Nếu choice == 3
#         In thông báo thoát
#         break
#     Ngược lại
#         Báo lựa chọn không hợp lệ

while True:
    print("\n===== MENU =====")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Xem hướng dẫn sử dụng")
    print("3. Thoát chương trình")

    choice = int(input("Nhập lựa chọn: "))

    if choice == 1:

        branch_count = int(input("Nhập số lượng chi nhánh: "))

        max_students = -1
        max_branch = 0

        for branch in range(1, branch_count + 1):

            print(f"\n--- Chi nhánh {branch} ---")

            class_count = int(input("Nhập số lớp học của chi nhánh: "))

            branch_total = 0
            low_classes = []

            for classroom in range(1, class_count + 1):

                while True:
                    student_count = int(input(f"Nhập số học viên lớp {classroom}: "))

                    if student_count < 0:
                        print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                    else:
                        break

                branch_total += student_count

                if student_count < 10:
                    low_classes.append(classroom)

            print(f"Tổng số học viên chi nhánh {branch}: {branch_total}")

            if branch_total > max_students:
                max_students = branch_total
                max_branch = branch

            if len(low_classes) == 0:
                print("Không có lớp nào dưới 10 học viên")
            else:
                print("Các lớp dưới 10 học viên:")

                for classroom in low_classes:
                    print(f"Lớp {classroom}")

        print(f"\nChi nhánh có tổng số học viên cao nhất: Chi nhánh {max_branch}")

    elif choice == 2:

        print("\n===== HƯỚNG DẪN SỬ DỤNG =====")
        print("- Chọn chức năng từ menu.")
        print("- Nhập số lượng chi nhánh.")
        print("- Nhập số lớp học của từng chi nhánh.")
        print("- Nhập số học viên của từng lớp.")
        print("- Hệ thống sẽ thống kê tự động.")

    elif choice == 3:

        print("Thoát chương trình")
        break

    else:

        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
