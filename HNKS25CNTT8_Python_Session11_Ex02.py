# 1) Phân tích lỗi
# - Dictionary employee gồm các key:
#   + employee_id
#   + full_name
#   + department
#   + status
# - employee_id = employee[0] gây lỗi vì dictionary truy cập bằng key, không phải index
# - Dictionary không truy cập phần tử bằng index giống list
# - Muốn lấy mã nhân viên cần truy cập bằng key employee_id
# - full_name = employee["name"] gây lỗi vì không tồn tại key name
# - Key đúng để lấy họ tên nhân viên là full_name
# - employee["employee_status"] = "official" chưa cập nhật đúng vì tạo key mới employee_status thay vì cập nhật key status
# - Muốn cập nhật trạng thái nhân viên cần dùng key status
# - employee.append("base_salary", 15000000) gây lỗi vì dictionary không có phương thức append()
# - Dictionary không hỗ trợ append()
# - Muốn thêm lương cơ bản cần tạo key mới base_salary và gán giá trị 15000000
# - del employee["team"] gây lỗi vì không tồn tại key team
# - Muốn xóa thông tin phòng ban cần dùng key department


employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

employee_id = employee["employee_id"]
full_name = employee["full_name"]
employee["status"] = "official"
employee["base_salary"] = 15000000
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)