# 1 Phân tích lỗi
# Sau:
# express_orders.insert(0, "GE100-FAST")

# Danh sách trở thành:

# ['GE100-FAST', 'GE101', 'GE102-WRONG', 'GE103-CANCEL', 'GE104']
# Dòng:
# express_orders[1] = "GE102-UPDATED"

# sửa nhầm "GE101" vì sau khi insert(0, ...), các phần tử cũ bị dịch sang phải 1 vị trí.

# Sau khi chèn "GE100-FAST", "GE102-WRONG" nằm ở index 2.
# Dòng:
# express_orders.pop(3)

# không phù hợp vì đang xóa theo vị trí, không xóa trực tiếp đơn hàng bị hủy.

# Muốn xóa đúng "GE103-CANCEL":
# express_orders.remove("GE103-CANCEL")
# pop() không truyền index sẽ lấy phần tử cuối cùng trong danh sách.
# Dòng:
# current_order = express_orders.pop()

# lấy "GE104" thay vì đơn hàng đầu tiên.

# Muốn lấy đơn hàng đầu tiên:
# current_order = express_orders.pop(0)
# Cần sửa các dòng:
# express_orders[1] -> express_orders[2]
# express_orders.pop(3) -> express_orders.remove("GE103-CANCEL")
# express_orders.pop() -> express_orders.pop(0)


express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]
express_orders.append("GE104")
express_orders.insert(0, "GE100-FAST")
express_orders[2] = "GE102-UPDATED"
express_orders.remove("GE103-CANCEL")
current_order = express_orders.pop(0)
print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)