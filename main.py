from test import *


def main():
    current_vehicle = None

    while True:
        print("\n===== SMART TRANSIT MENU =====")
        print("1. Khởi tạo và đăng ký xe lái mới")
        print("2. Giả lập vận hành và kiểm tra hiệu suất")
        print("3. Thoát")

        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            print("\n--- KHỞI TẠO XE LÁI ROBOBUS ---")

            while True:
                plate = input("Nhập biển số xe (9 ký tự, bắt đầu bằng 29): ")

                if BaseVehicle.validate_license_plate(plate):
                    current_vehicle = RoboBus()

                    print("[Thành công]: Khởi tạo phương tiện RoboBus thành công!")

                    print("\n[MRO Architecture]:")
                    for cls in RoboBus.__mro__:
                        print(cls.__name__)

                    break
                else:
                    print("[Lỗi]: Biển số không hợp lệ. Vui lòng nhập lại!")

        elif choice == "2":
            print("\n--- GIẢ LẬP VẬN HÀNH PHƯƠNG TIỆN ---")

            if current_vehicle is None:
                print("[Lỗi]: Chưa có phương tiện nào được khởi tạo!")
                continue

            try:
                distance = float(input("Nhập số km di chuyển mới phát sinh: "))

                current_vehicle.drive(distance)

                efficiency = current_vehicle.calculate_efficiency()

                print("[Thành công]: Cập nhật lộ trình xe chạy thành công.")
                print(
                    f"Tổng quãng đường tích lũy (Odometer): {current_vehicle.odometer:.1f} km"
                )
                print(f"Hiệu suất tiêu thụ năng lượng tích hợp: {efficiency:.1f}%")

            except ValueError as e:
                print("[Lỗi]:", e)

        elif choice == "3":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!")


main()
