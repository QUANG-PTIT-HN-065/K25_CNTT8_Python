# 1) Phân tích và thiết kế giải pháp
# Hàm phụ trợ 1: find_patient_index(patients, er_id)

# Input
# patients: List chứa các chuỗi bệnh nhân.
# er_id: Mã bệnh nhân cần tìm.

# Output
# int
# Trả về vị trí (index) nếu tìm thấy.
# Trả về -1 nếu không tìm thấy.

# Thuật toán
# B1: Chuẩn hóa er_id (strip + upper).
# B2: Duyệt từng phần tử trong patients.
# B3: Tách chuỗi bằng split("|").
# B4: So sánh phần tử đầu tiên với er_id.
# B5: Nếu trùng -> return index.
# B6: Hết vòng lặp -> return -1.

# Hàm phụ trợ 2: extract_vital_value(vital_string)

# Input
# vital_string: Chuỗi sinh hiệu.
# Ví dụ: "HR:115"
# Ví dụ: "TEMP:39.5"

# Output
# float

# Thuật toán (dùng split)
# B1: Tách chuỗi theo dấu ":".
# B2: Lấy phần tử thứ 2.
# B3: Ép kiểu float.
# B4: Return kết quả.

er_patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
    "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
    "ER03|Le Van Cuong|HR:130|TEMP:38.2",
]


def find_patient_index(patients, er_id):
    er_id = er_id.strip().upper()

    for index, patient in enumerate(patients):
        patient_data = patient.split("|")

        if patient_data[0] == er_id:
            return index

    return -1


def extract_vital_value(vital_string):
    return float(vital_string.split(":")[1])


def display_dashboard(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    print("\n--- BẢNG THEO DÕI CA CẤP CỨU ---")

    for i, patient in enumerate(patients, start=1):
        data = patient.split("|")

        print(
            f"{i}. [{data[0]}] {data[1]} | "
            f"Nhịp tim: {extract_vital_value(data[2]):.0f} bpm | "
            f"Nhiệt độ: {extract_vital_value(data[3]):.1f} °C"
        )


def admit_patient(patients):
    print("\n--- TIẾP NHẬN CA CẤP CỨU MỚI ---")

    er_id = input("Nhập mã ER: ").strip().upper()

    if not er_id:
        print("Mã ER không được để trống!")
        return

    if find_patient_index(patients, er_id) != -1:
        print("Mã ca cấp cứu đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip().title()

    if not name:
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        hr = input("Nhập nhịp tim HR: ").strip()

        if hr.isdigit() and int(hr) > 0:
            break

        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")

    while True:
        temp = input("Nhập nhiệt độ TEMP: ").strip()

        try:
            temp_value = float(temp)

            if temp_value >= 36.5:
                break

            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")

        except ValueError:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")

    record = f"{er_id}|{name}|HR:{hr}|TEMP:{temp}"
    patients.append(record)

    print("Tiếp nhận ca cấp cứu mới thành công!")


def update_vitals(patients):
    print("\n--- CẬP NHẬT LẠI SINH HIỆU ---")

    er_id = input("Nhập mã ER cần cập nhật: ").strip().upper()

    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    data = patients[index].split("|")

    print(f"Tìm thấy bệnh nhân: {data[1]}")
    print(f"Sinh hiệu hiện tại: {data[2]} | {data[3]}")

    print("1. Nhịp tim HR")
    print("2. Nhiệt độ TEMP")

    choice = input("Chọn loại sinh hiệu: ").strip()

    if choice == "1":
        value = input("Nhập nhịp tim mới: ").strip()

        if not (value.isdigit() and int(value) > 0):
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
            return

        data[2] = f"HR:{value}"
        print("Cập nhật nhịp tim thành công!")

    elif choice == "2":
        value = input("Nhập nhiệt độ mới: ").strip()

        try:
            if float(value) < 36.5:
                print(
                    "Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!"
                )
                return

        except ValueError:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")
            return

        data[3] = f"TEMP:{value}"
        print("Cập nhật nhiệt độ thành công!")

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")
        return

    patients[index] = "|".join(data)


def trigger_red_alert(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    critical_patients = []

    for patient in patients:
        data = patient.split("|")

        hr = extract_vital_value(data[2])
        temp = extract_vital_value(data[3])

        if hr > 100 or temp >= 39:
            critical_patients.append(patient)

    if len(critical_patients) == 0:
        print("Không có bệnh nhân nguy kịch tại thời điểm hiện tại.")
        return

    print("\n!!! BÁO ĐỘNG ĐỎ - DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!")

    for i, patient in enumerate(critical_patients, start=1):
        data = patient.split("|")

        print(
            f"{i}. [{data[0]}] {data[1]} | "
            f"HR: {extract_vital_value(data[2]):.0f} bpm | "
            f"TEMP: {extract_vital_value(data[3]):.1f} °C | "
            f"CẦN XỬ LÝ KHẨN CẤP"
        )

    print(f"Tổng số ca nguy kịch: {len(critical_patients)}")


def discharge_patient(patients):
    print("\n--- XUẤT VIỆN / CHUYỂN KHOA ---")

    er_id = input("Nhập mã ER cần xóa khỏi hệ thống: ").strip().upper()

    if not er_id:
        print("Mã ER không được để trống!")
        return

    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    patient_name = patients[index].split("|")[1]

    patients.pop(index)

    print(f"Đã chuyển khoa thành công cho bệnh nhân {patient_name}!")


def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====")
        print("1. Bảng theo dõi bệnh nhân")
        print("2. Tiếp nhận ca cấp cứu mới")
        print("3. Cập nhật lại sinh hiệu")
        print("4. BÁO ĐỘNG ĐỎ")
        print("5. Xuất viện / Chuyển khoa")
        print("6. Thoát chương trình")

        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            display_dashboard(er_patients)

        elif choice == "2":
            admit_patient(er_patients)

        elif choice == "3":
            update_vitals(er_patients)

        elif choice == "4":
            trigger_red_alert(er_patients)

        elif choice == "5":
            discharge_patient(er_patients)

        elif choice == "6":
            print("Kết thúc ca trực.")
            break

        else:
            print("Lựa chọn không hợp lệ!")


main()
