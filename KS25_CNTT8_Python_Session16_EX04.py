# 1) Phân tích thiết kế hàm
# Hàm 1: display_records(records)

# Input (Tham số):

# records: List chứa các chuỗi hồ sơ bệnh nhân.

# Output (Trả về):

# None (chỉ hiển thị dữ liệu ra màn hình).

# Pseudocode:

# Nếu records rỗng:
#     In "Hệ thống hiện chưa có hồ sơ nào."
#     Kết thúc

# In tiêu đề bảng

# Duyệt từng hồ sơ trong records:
#     split chuỗi theo dấu "-"
#     lấy mã BN, tên, năm sinh, chẩn đoán
#     in dữ liệu ra màn hình

# In dòng kết thúc bảng

# Hàm 2: find_patient_index(records, patient_id)

# Input (Tham số):

# records: List hồ sơ bệnh nhân.
# patient_id: Mã bệnh nhân cần tìm.

# Output (Trả về):

# int: vị trí của bệnh nhân trong danh sách.
# -1 nếu không tìm thấy.

# Pseudocode:

# Chuẩn hóa patient_id

# Duyệt từng phần tử trong records:
#     split chuỗi
#     lấy mã bệnh nhân

#     Nếu mã bệnh nhân trùng:
#         return vị trí

# return -1
# Hàm 3: add_patient(records)

# Input (Tham số):

# records: List hồ sơ bệnh nhân.

# Output (Trả về):

# None

# Pseudocode:

# Nhập mã bệnh nhân
# Chuẩn hóa mã

# Nếu mã rỗng:
#     báo lỗi
#     kết thúc

# Nếu mã đã tồn tại:
#     báo lỗi
#     kết thúc

# Nhập tên
# Chuẩn hóa tên
# Thay dấu "-" thành khoảng trắng

# Nếu tên rỗng:
#     báo lỗi
#     kết thúc

# Nhập năm sinh

# Lặp:
#     kiểm tra là số
#     kiểm tra từ 1900 đến năm hiện tại
#     nếu sai báo lỗi

# Nhập chẩn đoán
# Thay "-" thành khoảng trắng
# Capitalize()

# Ghép thành chuỗi:
#     MA-TEN-NAMSINH-CHANDOAN

# append vào records

# Thông báo thành công
# Hàm 4: update_diagnosis(records)

# Input (Tham số):

# records: List hồ sơ bệnh nhân.

# Output (Trả về):

# None

# Pseudocode:

# Nhập mã bệnh nhân

# Tìm vị trí bằng find_patient_index()

# Nếu không tìm thấy:
#     báo lỗi
#     kết thúc

# split hồ sơ thành list

# Hiển thị tên và chẩn đoán hiện tại

# Nhập chẩn đoán mới
# Chuẩn hóa dữ liệu

# Cập nhật phần tử cuối của list

# join lại bằng dấu "-"

# Gán đè vào records[index]

# Thông báo thành công
# Hàm 5: generate_age_report(records)

# Input (Tham số):

# records: List hồ sơ bệnh nhân.

# Output (Trả về):

# None

# Pseudocode:

# Khởi tạo:
#     children = 0
#     adult = 0
#     elderly = 0

# Lấy năm hiện tại

# Duyệt từng hồ sơ:
#     split chuỗi
#     lấy năm sinh

#     tuổi = năm hiện tại - năm sinh

#     Nếu tuổi < 16:
#         children += 1
#     Nếu 16 <= tuổi <= 60:
#         adult += 1
#     Nếu tuổi > 60:
#         elderly += 1

# In báo cáo

from datetime import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan",
]


def find_patient_index(records, patient_id):
    """
    Tìm vị trí bệnh nhân theo mã BN.
    Trả về index nếu tìm thấy, ngược lại trả về -1.
    """
    patient_id = patient_id.strip().upper()

    for index, record in enumerate(records):
        parts = record.split("-")

        if parts[0].upper() == patient_id:
            return index

    return -1


def display_records(records):
    """
    Hiển thị danh sách hồ sơ bệnh án.
    """
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print(
        "\n--- DANH SÁCH BỆNH NHÂN --------------------------------------------------"
    )

    for index, record in enumerate(records, start=1):
        patient_id, name, birth_year, diagnosis = record.split("-")

        print(
            f"{index}. [{patient_id}] {name:<20} | "
            f"Năm sinh: {birth_year} | "
            f"Chẩn đoán: {diagnosis}"
        )

    print("--------------------------------------------------------------------------")


def add_patient(records):
    """
    Thêm hồ sơ bệnh nhân mới.
    """
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if patient_id == "":
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(records, patient_id) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip()

    if name == "":
        print("Tên bệnh nhân không được để trống!")
        return

    name = name.replace("-", " ").title()

    current_year = datetime.now().year

    birth_year = input("Nhập năm sinh: ").strip()

    if (
        not birth_year.isdigit()
        or int(birth_year) < 1900
        or int(birth_year) > current_year
    ):
        print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")
        return

    diagnosis = input("Nhập chẩn đoán: ").strip()

    if diagnosis == "":
        print("Chẩn đoán không được để trống!")
        return

    diagnosis = diagnosis.replace("-", " ").capitalize()

    new_record = "-".join([patient_id, name, birth_year, diagnosis])

    records.append(new_record)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print("Dữ liệu được lưu:")
    print(new_record)


def update_diagnosis(records):
    """
    Cập nhật chẩn đoán theo mã BN.
    """
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    data = records[index].split("-")

    print(f"\nTìm thấy bệnh nhân: {data[1]}")
    print(f"Chẩn đoán hiện tại: {data[3]}")

    new_diagnosis = input("Nhập chẩn đoán mới: ").strip()

    if new_diagnosis == "":
        print("Chẩn đoán không được để trống!")
        return

    new_diagnosis = new_diagnosis.replace("-", " ").capitalize()

    data[3] = new_diagnosis

    records[index] = "-".join(data)

    print("\nCập nhật chẩn đoán thành công!")
    print("Dữ liệu mới được lưu:")
    print(records[index])


def generate_age_report(records):
    """
    Báo cáo phân loại bệnh nhân theo độ tuổi.
    """
    children = 0
    adult = 0
    elderly = 0

    current_year = datetime.now().year

    for record in records:
        parts = record.split("-")

        age = current_year - int(parts[2])

        if age < 16:
            children += 1
        elif age <= 60:
            adult += 1
        else:
            elderly += 1

    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adult} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
        print("1. Xem danh sách hồ sơ bệnh án")
        print("2. Thêm hồ sơ bệnh nhân mới")
        print("3. Cập nhật chẩn đoán theo Mã BN")
        print("4. Báo cáo phân loại theo độ tuổi")
        print("5. Thoát chương trình")
        print("==================================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_records(patient_records)

        elif choice == "2":
            add_patient(patient_records)

        elif choice == "3":
            update_diagnosis(patient_records)

        elif choice == "4":
            generate_age_report(patient_records)

        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập từ 1 đến 5!")


if __name__ == "__main__":
    main()
