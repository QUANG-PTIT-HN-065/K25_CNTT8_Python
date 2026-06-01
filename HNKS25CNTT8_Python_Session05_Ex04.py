# Phân tích và thiết kế giải pháp
# Input

# | Biến          | Kiểu dữ liệu | Ý nghĩa                         |
# | ------------- | ------------ | ------------------------------- |
# | branch_count  | int          | Số lượng chi nhánh              |
# | student_count | int          | Số học viên đi học của từng lớp |

# Output
# Thông báo trạng thái lớp:
# Lớp học ổn định
# Lớp cần được nhắc nhở theo dõi
# Thông báo lỗi:
# Số học viên không hợp lệ. Vui lòng nhập lại.
# Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.

# Đề xuất giải pháp
# Nhập số lượng chi nhánh.
# Duyệt từng chi nhánh bằng vòng lặp for.
# Mỗi chi nhánh có 2 lớp học.
# Với mỗi lớp:
#   Dùng vòng lặp while để kiểm tra dữ liệu nhập.
#   Nếu số học viên < 0:
#        Báo lỗi.
#        Yêu cầu nhập lại.
# Nếu số học viên = 0:
#        Thông báo lớp vắng toàn bộ.
#        Bỏ qua đánh giá lớp.
# Nếu số học viên > 0:
#        Đánh giá trạng thái lớp.
# Quy tắc đánh giá:
# Từ 20 học viên trở lên -> Lớp học ổn định
# Dưới 20 học viên -> Lớp cần được nhắc nhở theo dõi

# Pseudocode
# Nhập branch_count
# Lặp branch từ 1 đến branch_count
#     In tên chi nhánh
#     Lặp classroom từ 1 đến 2
#         Lặp vô hạn
#             Nhập student_count
#             Nếu student_count < 0
#                 In thông báo lỗi
#                 Nhập lại
#             Ngược lại
#                 Thoát vòng lặp
#         Nếu student_count == 0
#             In "Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái."
#             continue
#         Nếu student_count >= 20
#             In "Lớp học ổn định"

#         Ngược lại
#             In "Lớp cần được nhắc nhở theo dõi"

# Nhập số lượng chi nhánh
branch_count = int(input("Nhập số lượng chi nhánh: "))

# Duyệt từng chi nhánh
for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}:")
    # Mỗi chi nhánh có 2 lớp
    for classroom in range(1, 3):

        # Kiểm tra dữ liệu hợp lệ
        while True:
            student_count = int(input(f"Nhập số học viên đi học của lớp {classroom}: "))

            if student_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
            else:
                break

        # Edge case: lớp vắng toàn bộ
        if student_count == 0:
            print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
            continue

        # Đánh giá trạng thái lớp
        if student_count >= 20:
            print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp học ổn định")
        else:
            print(
                f"Chi nhánh {branch} - Lớp {classroom}: Lớp cần được nhắc nhở theo dõi"
            )
