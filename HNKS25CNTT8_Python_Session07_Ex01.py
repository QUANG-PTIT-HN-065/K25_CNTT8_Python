# 1 Phân tích lỗi
# Sau delivery_orders.insert(0, "GE000"):

# delivery_orders[1] = "GE002-UPDATED" sửa sai vì sau khi chèn "GE000" vào đầu, index 1 là "GE001"

# Sau khi chèn "GE000", "GE002" nằm ở index 2
# delivery_orders.remove(3) gây lỗi vì remove() xóa theo giá trị, không phải theo vị trí. Trong danh sách không có phần tử 3.
# Muốn xóa "GE003-CANCEL":

# delivery_orders.remove("GE003-CANCEL")

# pop() xóa phần tử khỏi danh sách và trả về phần tử vừa xóa
# Chương trình lỗi khi in transferred_order vì biến này chưa được tạo.
# Muốn lưu đơn hàng vừa lấy ra:

# transferred_order = delivery_orders.pop()

delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]
delivery_orders.append("GE004")
delivery_orders.insert(0, "GE000")
delivery_orders[2] = "GE002-UPDATED"
delivery_orders.remove("GE003-CANCEL")
transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)