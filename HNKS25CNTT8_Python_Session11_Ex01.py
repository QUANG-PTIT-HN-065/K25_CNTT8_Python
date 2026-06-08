# 1) Phân tích lỗi
# - Tuple product_info có 4 phần tử
# - "SP001" nằm ở index 0
# - product_code = product_info[1] sai vì index 1 là tên sản phẩm, không phải mã sản phẩm
# - "Áo polo nam" nằm ở index 1
# - product_name = product_info[2] sai vì index 2 là kích cỡ sản phẩm, không phải tên sản phẩm
# - product_length = product_info.length() gây lỗi vì tuple không có phương thức length()
# - Muốn đếm số phần tử trong tuple dùng len()
# - product_info[3] = 279000 không hợp lệ vì tuple là immutable (không thể thay đổi trực tiếp phần tử)
# - Tuple không cho phép sửa trực tiếp phần tử
# - Muốn cập nhật giá bán cần tạo một tuple mới với giá trị giá bán đã thay đổi

product_info = ("SP001", "Áo polo nam", "Size L", 299000)
product_code = product_info[0]
product_name = product_info[1]
product_length = len(product_info)
product_info = (
    product_info[0],
    product_info[1],
    product_info[2],
    279000
)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)