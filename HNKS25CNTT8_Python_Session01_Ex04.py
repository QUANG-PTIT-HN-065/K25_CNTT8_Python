# Input / Output

# Input
# | Biến        | Ý nghĩa          | Kiểu dữ liệu |
# | ----------- | ---------------- | ------------ |
# | age         | Tuổi             | int          |
# | systolic_bp | Huyết áp tâm thu | int          |
# | blood_sugar | Đường huyết      | int          |

# Output
# Trường hợp	                          Kết quả
# Thỏa tất cả điều kiện	             ĐỦ ĐIỀU KIỆN PHẪU THUẬT
# Trượt bất kỳ điều kiện nào	     TỪ CHỐI PHẪU THUẬT
# Dữ liệu âm	                     Dữ liệu nhập vào không hợp lệ

# Đề xuất giải pháp
# Giải pháp 1: Gộp điều kiện (Flat Logic)
# Đặc điểm:
# + Code ngắn gọn
# + Ít thụt lề
# + Khó biết bệnh nhân trượt điều kiện nào

# Giải pháp 2: Điều kiện lồng nhau (Nested If)
# Đặc điểm:
# + Dễ tách từng bước kiểm tra
# + Có thể thông báo lỗi chi tiết
# + Code dài hơn

# Bảng so sánh
# | Tiêu chí               | Flat Logic | Nested If |
# | ---------------------- | ---------- | --------- |
# | Độ ngắn gọn            | Cao        | Thấp      |
# | Độ phức tạp thụt lề    | Thấp       | Cao       |
# | Dễ đọc logic y khoa    | Trung bình | Cao       |
# | Thông báo lỗi chi tiết | Khó        | Dễ        |
# | Trải nghiệm người dùng | Trung bình | Tốt hơn   |

# Chốt lựa chọn

# Chọn: Nested If
# Lý do
# Dễ kiểm tra từng tiêu chí y khoa.
# Có thể thông báo chính xác bệnh nhân bị từ chối vì lý do gì.
# Phù hợp môi trường bệnh viện cần tính minh bạch.

# Trade-off
# Code dài hơn.
# Nhiều khối thụt lề hơn.

age = int(input("Nhập tuổi bệnh nhân: "))
systolic_bp = int(input("Nhập huyết áp tâm thu (mmHg): "))
blood_sugar = int(input("Nhập đường huyết (mg/dL): "))


if age < 0 or systolic_bp < 0 or blood_sugar < 0:
    print("Dữ liệu nhập vào không hợp lệ")
else:
    if age < 75:
        if 90 <= systolic_bp <= 140:
            if blood_sugar < 150:
                print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
            else:
                print("TỪ CHỐI PHẪU THUẬT")
                print("- Lý do: Đường huyết quá cao")
        else:
            print("TỪ CHỐI PHẪU THUẬT")
            print("- Lý do: Huyết áp ngoài giới hạn an toàn")
    else:
        print("TỪ CHỐI PHẪU THUẬT")
        print("- Lý do: Tuổi vượt giới hạn cho phép")
