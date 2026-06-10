# 1) Phân tích lỗi
# Câu 1

# Hàm được định nghĩa:

# def calculate_final_price(price, discount, shipping_fee):

# Lời gọi:

# calculate_final_price(100000, 15000, 0.1)
# price = 100000
# discount = 15000
# shipping_fee = 0.1
# Câu 2

# Công thức thực tế đang tính:

# 100000 - (100000 * 15000) + 0.1

# Kết quả:

# 100000 - 1500000000 + 0.1
# = -1499900000 + 0.1
# = -1499899999.9

# Do 15000 bị gán nhầm vào discount nên phép nhân:

# 100000 * 15000

# tạo ra giá trị rất lớn làm kết quả bị âm.

# Câu 3

# Dòng:

# final_payment = order_total + 5000

# gây lỗi vì order_total có giá trị None, không thể cộng với số nguyên.

# Câu 4

# Biến order_total mang giá trị:

# None

# Vì hàm không có lệnh return, Python tự động trả về None

# Câu 5
# print(total)
# Chỉ hiển thị kết quả ra màn hình
# Không trả kết quả cho nơi gọi hàm
# return total
# Trả kết quả về cho nơi gọi hàm
# Có thể lưu vào biến và tiếp tục tính toán
# Câu 6

# Cần sửa:

# return total

# thay cho:

# print("Đã tính xong tổng tiền:", total)

# để order_total nhận được kết quả tính toán


def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total


order_total = calculate_final_price(100000, 0.1, 15000)

final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)
