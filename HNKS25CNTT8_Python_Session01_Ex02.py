# Phân tích lỗi

# a. Toán tử logic đang bị sử dụng sai

# Code hiện tại dùng: or

# Trong khi bài toán yêu cầu:

# Người hiến máu phải đủ tuổi
# Và đủ cân nặng

# => Phải dùng: and

# Dò luồng thực thi với: donor_age = 16 , donor_weight = 55

# Điều kiện hiện tại: if donor_age >= 18 or donor_weight >= 50:

# Kiểm tra:

# 16 >= 18 -> False
# 55 >= 50 -> True

# Vì toán tử or:

# Chỉ cần 1 điều kiện đúng
# Kết quả toàn bộ biểu thức sẽ là True

# => Chương trình in: ELIGIBLE

# => Sai nghiệp vụ vì người hiến chưa đủ 18 tuổi.

# Khác biệt giữa and và or
# and	Tất cả điều kiện phải đúng
# or	Chỉ cần một điều kiện đúng

print("--- BLOOD DONOR SCREENING SYSTEM ---")

donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE - Donor meets all requirements.")

else:
    print("Result: NOT ELIGIBLE")
    if donor_age < 18:
        print("- Reason: Donor is under 18 years old.")
    if donor_weight < 50:
        print("- Reason: Donor weight is below 50 kg.")
