count = 0
total_money = 0
total_larage_invoices = 0
large_invoice_rate = 0
while True:
    money = float(input(f"Khác hàng {count + 1} - Nhập giá trị hoá đơn: "))
    count += 1
    total_money += money
    if money > 1000000:
        total_larage_invoices += 1
    continue_input = input("Bạn có muốn nhập thêm hoá đơn không? (C/K): ")
    if continue_input.lower() != 'c':
        break

if count > 0:
    large_invoice_rate = (total_larage_invoices / count) * 100

print(f"Tổng số hoá đơn: {count}")
print(f"Tổng giá trị hoá đơn: {total_money}")
print(f"Số hoá đơn lớn: {total_larage_invoices}")
print(f"Tỷ lệ hoá đơn lớn: {large_invoice_rate:.2f}%")