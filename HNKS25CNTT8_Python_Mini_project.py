employer = []
next_id = 101
while True:

    print("\n===== Quản lý nhân sự - STAFF MANAGER =====")
    print("1. Thêm nhân viên mới")
    print("2. Danh sách nhân viên ")
    print("3. xoá nhân viên khỏi hệ thống")
    print("7. Thoát")

    try:
        choice = int(input("Nhập lựa chọn: "))

        if choice == 1:
            name = input("Nhập tên nhân viên: ")
            salary = float(input("Nhập lương nhân viên: "))

            if salary <= 0:
                print("Lương không hợp lệ.")
                continue

            employee = {"id": next_id, "name": name, "salary": salary}
            employer.append(employee)
            print(f"Đã thêm Thàng công nhân viên với ID: {next_id}")
            next_id += 1

        elif choice == 2:
            if not employer:
                print("Chưa có nhân viên nào trong hệ thống.")
            else:
                print("\nDanh sách nhân viên:")
                for emp in employer:
                    print("ID     | Tên Nhân Viên       | mức lương")
                    print(f"{emp['id']} | {emp['name']} | {emp['salary']}")

        elif choice == 3:
            delete_id = int(input("Nhập ID nhân viên cần xoá: "))
            delete_found = False
            for emp in employer:
                if emp["id"] == delete_id:
                    employer.remove(emp)
                    print(f"Đã xoá nhân viên với ID: {delete_id}")
                    delete_found = True
                    break
            if not delete_found:
                print("Không tìm thấy nhân viên với ID đã nhập.")

        elif choice == 4:
            break

    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
