
# Phân tích và thiết kế giải pháp
# Input

# | Biến       | Kiểu dữ liệu | Ý nghĩa               |
# | ---------- | ------------ | --------------------- |
# | room_count | int          | Số lượng phòng học    |
# | row_count  | int          | Số hàng ghế của phòng |
# | seat_count | int          | Số ghế trên mỗi hàng  |

# Output
# In sơ đồ chỗ ngồi của từng phòng bằng dấu *
# Hoặc các thông báo lỗi:
# Số lượng phòng học không hợp lệ
# Dữ liệu phòng học không hợp lệ Bỏ qua phòng này
# Phòng quá lớn Dừng nhập dữ liệu

# Đề xuất giải pháp
# Nhập số lượng phòng học

# Nếu số lượng phòng <= 0:
#    Hiển thị thông báo lỗi
#    Kết thúc chương trình

# Duyệt từng phòng bằng vòng lặp for
# Nhập số hàng và số ghế

# Kiểm tra:
#   Nếu số hàng hoặc số ghế <= 0
#        Báo lỗi
#        continue
#   Nếu số hàng hoặc số ghế > 10
#        Báo lỗi
#        break
# Nếu dữ liệu hợp lệ:
# Dùng vòng lặp lồng nhau để in hình chữ nhật bằng dấu *

# Pseudocode
# Nhập room_count

# Nếu room_count <= 0
#     In "Số lượng phòng học không hợp lệ"
#     Kết thúc

# Lặp từ phòng 1 đến room_count

#     Nhập row_count
#     Nhập seat_count

#     Nếu row_count <= 0 hoặc seat_count <= 0
#         In "Dữ liệu phòng học không hợp lệ Bỏ qua phòng này"
#         continue

#     Nếu row_count > 10 hoặc seat_count > 10
#         In "Phòng quá lớn Dừng nhập dữ liệu"
#         break

#     In tiêu đề phòng học

#     Lặp row_count lần
#         In "*" lặp lại seat_count lần

# Nhập số lượng phòng học
room_count = int(input("Nhập số lượng phòng học: "))

# Edge case 1
if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
    for room in range(1, room_count + 1):

        row_count = int(input(f"Nhập số hàng ghế của phòng {room}: "))
        seat_count = int(input(f"Nhập số ghế mỗi hàng của phòng {room}: "))

        # Edge case 2
        if row_count <= 0 or seat_count <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        # Edge case 3
        if row_count > 10 or seat_count > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        print(f"\nSơ đồ phòng học {room}:")

        for _ in range(row_count):
            print("*" * seat_count)

        print()
