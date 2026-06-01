# Phân tích lỗi
# Lỗi do vòng lặp ngoài đang duyệt theo tháng, nên dữ liệu được nhóm theo tháng thay vì theo chi nhánh.
# Theo yêu cầu nghiệp vụ, vòng lặp ngoài phải duyệt theo chi nhánh.
# Vòng lặp trong phải duyệt theo tháng.

branch_count = int(input("Nhập số lượng chỉ nhánh: "))
month_count = 3
result = ""
for  branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        result += f"Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng\n"
        
print(result)
