# 1) Phân tích và thiết kế giải pháp
# 1. Phân tích Input/Output cho từng hàm
# Hàm display_patients(patient_list)

# Input:

# patient_list: List chứa danh sách bệnh nhân.

# Output:

# None (chỉ in dữ liệu ra màn hình).
# Hàm validate_gender(gender_input)

# Input:

# gender_input: Chuỗi giới tính người dùng nhập.

# Output:

# True nếu là "nam" hoặc "nu".
# False nếu không hợp lệ.
# Hàm find_patient_index(patient_list, patient_id)

# Input:

# patient_list: Danh sách bệnh nhân.
# patient_id: Mã bệnh nhân cần tìm.

# Output:

# Trả về index của bệnh nhân nếu tìm thấy.
# Trả về -1 nếu không tìm thấy.
# Hàm add_patient(patient_list)

# Input:

# patient_list: Danh sách bệnh nhân.

# Output:

# None.
# Thêm bệnh nhân mới vào danh sách nếu hợp lệ.
# Hàm update_diagnosis(patient_list)

# Input:

# patient_list: Danh sách bệnh nhân.

# Output:

# None.
# Cập nhật chẩn đoán bệnh.
# Hàm search_by_disease(patient_list)

# Input:

# patient_list: Danh sách bệnh nhân.

# Output:

# None.
# In danh sách bệnh nhân phù hợp và thống kê số lượng.
# 2. Đề xuất giải pháp
# Sự tương tác giữa String và List
# Thông tin bệnh nhân được lưu trong các List con.
# Các dữ liệu chuỗi như:
# Mã bệnh nhân
# Tên bệnh nhân
# Giới tính
# Chẩn đoán bệnh

# được xử lý bằng:

# .strip()
# .upper()
# .title()
# .capitalize()
# .lower()

# trước khi lưu vào List.

# Truyền List vào hàm

# Khi truyền:

# add_patient(patients)

# Python truyền tham chiếu (reference) của List.

# Do đó:

# patient_list.append(...)

# bên trong hàm sẽ làm thay đổi trực tiếp danh sách gốc patients.

# Không cần return lại danh sách.

patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"],
]


def validate_gender(gender_input):
    """
    Kiểm tra giới tính hợp lệ.
    """
    gender = gender_input.strip().lower()
    return gender in ["nam", "nu"]


def find_patient_index(patient_list, patient_id):
    """
    Tìm vị trí bệnh nhân theo mã.
    """
    patient_id = patient_id.strip().upper()

    for index, patient in enumerate(patient_list):
        if patient[0] == patient_id:
            return index

    return -1


def display_patients(patient_list):
    """
    Hiển thị danh sách bệnh nhân.
    """
    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return

    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")

    for i, patient in enumerate(patient_list, start=1):
        print(
            f"{i}. Mã: {patient[0]} | "
            f"Tên: {patient[1]} | "
            f"Giới tính: {patient[2]} | "
            f"Bệnh: {patient[3]}"
        )


def add_patient(patient_list):
    """
    Tiếp nhận bệnh nhân mới.
    """
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip()

    if len(name) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    name = name.title()

    while True:
        gender = input("Nhập giới tính Nam/Nu: ")

        if validate_gender(gender):
            gender = gender.strip().lower().capitalize()
            break

        print("Giới tính không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán bệnh: ").strip()

    if len(diagnosis) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    diagnosis = diagnosis.capitalize()

    patient = [patient_id, name, gender, diagnosis]

    patient_list.append(patient)

    print("Tiếp nhận bệnh nhân thành công!")


def update_diagnosis(patient_list):
    """
    Cập nhật chẩn đoán bệnh.
    """
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    index = find_patient_index(patient_list, patient_id)

    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id}!")
        return

    print(f"Tìm thấy bệnh nhân: " f"{patient_list[index][1]}")

    print(f"Chẩn đoán hiện tại: " f"{patient_list[index][3]}")

    diagnosis = input("Nhập chẩn đoán mới: ").strip()

    if len(diagnosis) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient_list[index][3] = diagnosis.capitalize()

    print("Cập nhật chẩn đoán bệnh thành công!")


def search_by_disease(patient_list):
    """
    Tìm kiếm bệnh nhân theo tên bệnh.
    """
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")

    keyword = input("Nhập từ khóa tên bệnh: ").strip()

    if len(keyword) == 0:
        print("Từ khóa tìm kiếm không được để trống!")
        return

    count = 0

    print("Kết quả tìm kiếm:")

    for patient in patient_list:
        if keyword.lower() in patient[3].lower():
            count += 1

            print(
                f"{count}. Mã: {patient[0]} | "
                f"Tên: {patient[1]} | "
                f"Giới tính: {patient[2]} | "
                f"Bệnh: {patient[3]}"
            )

    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(f"\nCó tổng cộng {count} bệnh nhân " f"mắc bệnh liên quan đến '{keyword}'.")


def main():
    """
    Chương trình chính.
    """
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
        print("1. Hiển thị danh sách bệnh nhân")
        print("2. Tiếp nhận bệnh nhân mới")
        print("3. Cập nhật chẩn đoán bệnh theo mã BN")
        print("4. Tìm kiếm và thống kê theo tên bệnh")
        print("5. Thoát chương trình")
        print("===========================================")

        choice = input("Nhập lựa chọn của bạn: ").strip()

        if choice == "1":
            display_patients(patients)

        elif choice == "2":
            add_patient(patients)

        elif choice == "3":
            update_diagnosis(patients)

        elif choice == "4":
            search_by_disease(patients)

        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break

        else:
            print("Lựa chọn không hợp lệ, " "vui lòng nhập số từ 1-5!")


main()
