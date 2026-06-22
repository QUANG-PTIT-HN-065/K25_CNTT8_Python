import logging

PRICE_PER_KWH = 3000
OVERLOAD_LIMIT = 5000
DISCOUNT_RATE = 3

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def show_devices(devices_list):
    if len(devices_list) == 0:
        print("Hệ thống hiện chưa có thiết bị giám sát nào!")
        return

    print(
        f"{'MÃ TB':<10}"
        f"{'VỊ TRÍ PHÂN XƯỞNG':<25}"
        f"{'CHỈ SỐ CŨ':<15}"
        f"{'CHỈ SỐ MỚI':<15}"
        f"{'TRẠNG THÁI'}"
    )

    for dev in devices_list:
        print(
            f"{dev['id']:<10}"
            f"{dev['location']:<25}"
            f"{dev['old_index']:<15}"
            f"{dev['new_index']:<15}"
            f"{dev['status']}"
        )


def update_indices(devices_list):

    device_id = input("Nhập mã thiết bị cần cập nhật chỉ số: ")

    target_device = None

    for dev in devices_list:
        if dev["id"] == device_id:
            target_device = dev
            break

    if target_device is None:
        print("[Lỗi] (ERR-E01): Mã thiết bị không tồn tại!")
        return

    while True:
        try:
            old_index = float(input("Nhập chỉ số cũ: "))

            if old_index < 0:
                print("[Lỗi] (ERR-E03)")
                continue

            break

        except ValueError:
            print("[Lỗi] (ERR-E03)")

    while True:
        try:
            new_index = float(input("Nhập chỉ số mới: "))

            if new_index < 0:
                print("[Lỗi] (ERR-E03)")
                continue

            if new_index < old_index:
                print("[Lỗi] (ERR-E02): Chỉ số mới phải >= chỉ số cũ!")
                continue

            break

        except ValueError:
            print("[Lỗi] (ERR-E03)")

    target_device["old_index"] = old_index
    target_device["new_index"] = new_index

    logging.info(f"Cập nhật dữ liệu cho thiết bị {device_id}")
    print("[Thành công]: Cập nhật dữ liệu hoàn tất.")


def trigger_overload_alert(devices_list):

    device_id = input("Nhập mã thiết bị cần duyệt cảnh báo: ")

    target_device = None

    for dev in devices_list:
        if dev["id"] == device_id:
            target_device = dev
            break

    if target_device is None:
        print("[Lỗi] (ERR-E01): Mã thiết bị không tồn tại!")
        return

    if target_device["status"] == "Overload":
        print("[Lỗi] (ERR-E04): Thiết bị đã ở trạng thái OVERLOAD!")
        return

    consumption = target_device["new_index"] - target_device["old_index"]

    if consumption > OVERLOAD_LIMIT:
        target_device["status"] = "Overload"

        logging.warning(f"Thiết bị {device_id} vượt quá {OVERLOAD_LIMIT} kWh.")

        print("[Thành công]: Đã chuyển sang trạng thái OVERLOAD.")
    else:
        print("Thiết bị đang hoạt động bình thường.")


def calculate_energy_financials(devices_list):

    if len(devices_list) == 0:
        return (0.0, 0.0, 0.0)

    total_kwh = 0

    for dev in devices_list:
        total_kwh += dev["new_index"] - dev["old_index"]

    total_money = total_kwh * PRICE_PER_KWH

    if total_kwh >= 50000:
        discount = DISCOUNT_RATE
    else:
        discount = 0

    total_money_after_discount = total_money * (100 - discount) / 100

    return total_kwh, discount, total_money_after_discount


def main():

    devices = [
        {
            "id": "M01",
            "location": "Mechanical Shop A",
            "old_index": 1200,
            "new_index": 4500,
            "status": "Normal",
        },
        {
            "id": "M02",
            "location": "Assembly Line B",
            "old_index": 2300,
            "new_index": 8500,
            "status": "Overload",
        },
    ]

    while True:

        print("\n===== SMART ENERGY MONITOR =====")
        print("1. Xem danh sách thiết bị")
        print("2. Cập nhật chỉ số điện")
        print("3. Kích hoạt cảnh báo quá tải")
        print("4. Tính tổng lượng điện & chi phí")
        print("5. Thoát")

        try:
            choice = int(input("Mời chọn chức năng: "))

        except ValueError:
            print("[Lỗi] Vui lòng nhập số từ 1-5!")
            continue

        if choice == 1:
            show_devices(devices)

        elif choice == 2:
            update_indices(devices)

        elif choice == 3:
            trigger_overload_alert(devices)

        elif choice == 4:

            total_kwh, discount, total_money = calculate_energy_financials(devices)

            print(f"Tổng điện tiêu thụ: {total_kwh} kWh")
            print(f"Chiết khấu áp dụng: {discount}%")
            print(f"Tổng tiền sau chiết khấu: {total_money:,.0f} VND")

        elif choice == 5:
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break

        else:
            print("[Lỗi] Vui lòng nhập từ 1 đến 5!")


if __name__ == "__main__":
    main()
