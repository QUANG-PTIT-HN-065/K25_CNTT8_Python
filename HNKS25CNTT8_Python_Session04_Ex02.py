daily_revenue = 0
number_days = 0
count = 0
for day in range(1,8):
    print(f"Nhập doanh thu ngày {day}: ") 
    revenue = float(input())
    daily_revenue += revenue
    number_days +=1
    if revenue > 5000000:
        count += 1
AVG_daily_revenue = daily_revenue /  number_days
print(f"Tổng doanh thu trong tuần là: {daily_revenue} VND")
print(f"Doanh thu trung bình mỗi ngày là: {AVG_daily_revenue} VND")
print(f"Số ngày có doanh thu trên 5.000.000 VND là: {count}")