total_invoices = int(input("Enter the total number of invoices: "))
max = float('-inf')
min = float('inf')
for i in range(1, total_invoices + 1):
    money = float(input(f"nhập giá trị cho hoán đơn thứ {i}: "))
    if money > max:
        max = money
    if money < min:
        min = money
        
print(f"Giá trị hóa đơn lớn nhất là: {max} VND")
print(f"Giá trị hóa đơn nhỏ nhất là: {min} VND")