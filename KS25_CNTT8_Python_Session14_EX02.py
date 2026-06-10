# 1) Phân tích lỗi
# Câu 1

# total_points là biến toàn cục (Global Variable) vì được khai báo bên ngoài hàm.

# Câu 2

# Lỗi:

# UnboundLocalError: local variable 'total_points' referenced before assignment

# Xảy ra vì trong hàm có phép gán:

# total_points = total_points + points_earned

# Khi thấy phép gán này, Python coi total_points trong hàm là biến cục bộ. Tuy nhiên biến đó chưa có giá trị trước khi được sử dụng ở vế phải nên phát sinh lỗi.

# Câu 3

# Không bị lỗi nếu chỉ đọc giá trị của total_points bên trong hàm mà không thực hiện phép gán.

# Câu 4

# Từ khóa cần dùng là:

# global total_points

# Câu 5

# Hàm nên sử dụng:

# return

# để trả về tổng điểm mới sau khi cộng.

def add_reward_points(current_points, points_earned):
    print("Đã cộng thêm", points_earned, "điểm.")
    return current_points + points_earned

total_points = 100

total_points = add_reward_points(total_points, 50)

print("Tổng điểm hiện tại của khách hàng:", total_points)