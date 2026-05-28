# phần tích lỗi
  
# Dò luồng thực thi với heart_rate = 135

# Khi nhập: heart_rate = 135

# Luồng chạy: 135 > 100  -> True

# => Chương trình thực hiện ngay khối:

# print("Priority: YELLOW - Abnormal. Monitor closely.")

# Sau đó toàn bộ chuỗi if-elif-else kết thúc.

# Điều kiện:

# elif heart_rate > 120
# không bao giờ được kiểm tra nữa.
  
  
  
# Khái niệm “luồng thực thi từ trên xuống dưới”
# Trong cấu trúc:

# if
# elif
# elif
# else

# Python kiểm tra điều kiện theo thứ tự từ trên xuống dưới.
# Khi gặp điều kiện đúng đầu tiên:
# chương trình thực thi khối lệnh đó
# bỏ qua toàn bộ các nhánh còn lại.

# Nguyên nhân khối RED bị bỏ qua
# Điều kiện: heart_rate > 100

# đã bao phủ luôn trường hợp: heart_rate = 135

# nên nhánh YELLOW chạy trước.

# Trong khi: heart_rate > 120
# phải được kiểm tra trước vì mức RED nguy hiểm hơn.

print("- EMERGENCY TRIAGE SYSTEM -")

heart_rate = int(input("Enter patient's heart rate (bpm): "))
if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")

elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")

elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")

else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")
