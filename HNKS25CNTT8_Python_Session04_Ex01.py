
total_money = int(input("Nhap tong so tien: "))
if total_money > 500000:
    discount = total_money*0.1
else:
    discount = 0

price = total_money - discount
print(f"so tien sau khi duoc giam la: {discount}")
print(f"so tien khach phai tra la: {price} VND")